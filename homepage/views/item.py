from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from django.forms import ModelChoiceField
import homepage.models as hmod
from django import forms

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	items = hmod.Item.objects.all().order_by('id')
	
	params['items'] = items

	return templater.render_to_response(request, 'item.html', params)

@view_function
@permission_required('homepage.add_item', login_url='/homepage/login.notAuthorized/')
def create(request):
	item = hmod.Item()
	item.name = ""
	item.value = '0.0'
	item.standard_rental_price = '0.00'
	item.legal_entity_id = hmod.LegalEntity.objects.first().id
	item.save()

	return HttpResponseRedirect('/homepage/item.edit/{}/'.format(item.id))

@view_function
@permission_required('homepage.delete_item', login_url='/homepage/login.notAuthorized/')
def delete(request):
	'''delete an rental'''

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/item/')

	item.delete()

	return HttpResponseRedirect('/homepage/item/'.format(item.id))

@view_function
@permission_required('homepage.change_item', login_url='/homepage/login.notAuthorized/') 
def edit(request):
	params = {}

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/item/')

	class MyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, obj):
			return str(obj.id) + " - " + obj.given_name


	class ItemEditForm(forms.Form):
		id = forms.CharField(required=True, max_length=100)
		name = forms.CharField(required=True)
		description = forms.CharField(required=True) 
		value = forms.CharField(required=True, max_length=100)
		standard_rental_price = forms.CharField(required=True)
		legal_entity_id = MyModelChoiceField(
			queryset= hmod.LegalEntity.objects.all(), empty_label=None,
		)
		
	form = ItemEditForm(initial={
	'id': item.id,
	'name': item.name,
	'description': item.description,
	'value': item.value,
	'standard_rental_price': item.standard_rental_price,
	'legal_entity_id': item.legal_entity_id,

	})
	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		if form.is_valid():
			item.id = form.cleaned_data['id']
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.legal_entity_id = form.cleaned_data['legal_entity_id']
			item.save()
			return HttpResponseRedirect('/homepage/item/')

	params['form'] = form
	return templater.render_to_response(request, 'item.edit.html', params)
