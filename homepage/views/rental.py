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

	rentals = hmod.Rental.objects.all().order_by('id')
	
	params['rentals'] = rentals

	return templater.render_to_response(request, 'rental.html', params)

@view_function
@permission_required('homepage.add_rental', login_url='/homepage/login.notAuthorized/')
def create(request):
	rental = hmod.Rental()
	rental.rental_time = "2000-01-01"
	rental.discount_percent = '0.0'
	rental.Organization_id = hmod.Organization.objects.first().id
	rental.Person_id = hmod.Person.objects.first().id
	rental.Agent_id = hmod.Agent.objects.first().id
	rental.save()

	return HttpResponseRedirect('/homepage/rental.edit/{}/'.format(rental.id))


@view_function
@permission_required('homepage.delete_rental', login_url='/homepage/login.notAuthorized/')
def delete(request):
	'''delete an rental'''

	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except hmod.Rental.DoesNotExist:
		return HttpResponseRedirect('/homepage/rental/')

	rental.delete()

	return HttpResponseRedirect('/homepage/rental/'.format(rental.id))

@view_function
@permission_required('homepage.change_rental', login_url='/homepage/login.notAuthorized/') 
def edit(request):
	params = {}

	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except hmod.Rental.DoesNotExist:
		return HttpResponseRedirect('/homepage/rental/')

	class OrgMyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, obj):
			return str(obj.id) + " - " + obj.organization_type
	class PerMyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, obj):
			return str(obj.id) + " - " + obj.given_name + " " + obj.family_name
	
	class RentalEditForm(forms.Form):
		id = forms.CharField(required=True, max_length=100)
		rental_time = forms.DateTimeField(required=True) 
		discount_percent = forms.DecimalField(required=True)
		Organization_id = OrgMyModelChoiceField(
			queryset= hmod.Organization.objects.all(), empty_label=None,
		)
		Person_id = PerMyModelChoiceField(
			queryset= hmod.Person.objects.all(), empty_label=None,
		)
		Agent_id = PerMyModelChoiceField(
			queryset= hmod.Agent.objects.all(), empty_label=None,
		)
		
	form = RentalEditForm(initial={
	'id': rental.id,
	'rental_time': rental.rental_time,
	'discount_percent': rental.discount_percent,
	'Organization_id': rental.Organization_id,
	'Person_id': rental.Person_id,
	'Agent_id': rental.Agent_id,

	})
	if request.method == 'POST':
		form = RentalEditForm(request.POST)
		if form.is_valid():
			rental.id = form.cleaned_data['id']
			rental.rental_time = form.cleaned_data['rental_time']
			rental.discount_percent = form.cleaned_data['discount_percent']
			rental.Organization_id = form.cleaned_data['Organization_id']
			rental.Person_id = form.cleaned_data['Person_id']
			rental.Agent_id = form.cleaned_data['Agent_id']
			rental.save()
			return HttpResponseRedirect('/homepage/rental/')

	params['form'] = form
	return templater.render_to_response(request, 'rental.edit.html', params)

