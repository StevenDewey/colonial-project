from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.forms import ModelChoiceField
import homepage.models as hmod
from django import forms

templater = get_renderer('homepage')


@view_function
def process_request(request):
	params = {}

	orders = hmod.Order.objects.all().order_by('id')
	
	params['orders'] = orders

	return templater.render_to_response(request, 'order.html', params)

@view_function
@permission_required('homepage.delete_order', login_url='/homepage/login.notAuthorized/')
def delete(request):
	'''delete an rental'''

	try:
		order = hmod.Order.objects.get(id=request.urlparams[0])
	except hmod.Order.DoesNotExist:
		return HttpResponseRedirect('/homepage/order/')

	order.delete()

	return HttpResponseRedirect('/homepage/order/'.format(order.id))

@view_function
@permission_required('homepage.add_order', login_url='/homepage/login.notAuthorized/')
def create(request):
	order = hmod.Order()
	order.order_date = "2000-01-01"
	order.phone = '000-000-0000'
	order.date_packed = '2000-01-01'
	order.date_paid = '2000-01-01'
	order.date_shipped = '2000-01-01'
	order.tracking_number = '0'
	order.ship_address1 = ''
	order.ship_address2 = ' '
	order.ship_city = ' '
	order.ship_state = ' '
	order.ship_zip = ''
	order.ship_country = ' '
	order.Agent_id = hmod.Agent.objects.first().id
	order.BulkDetail_id = hmod.BulkDetail.objects.first().id
	order.PersonalDetail_id = hmod.PersonalDetail.objects.first().id

	order.save()

	return HttpResponseRedirect('/homepage/order.edit/{}/'.format(order.id))

@view_function
@permission_required('homepage.change_order', login_url='/homepage/login.notAuthorized/') 
def edit(request):
	params = {}

	try:
		order = hmod.Order.objects.get(id=request.urlparams[0])
	except hmod.Order.DoesNotExist:
		return HttpResponseRedirect('/homepage/order/')

	class AgentModelChoiceField(ModelChoiceField):
		def label_from_instance(self, obj):
			return str(obj.id) + " - " + obj.given_name + " " + obj.family_name

	class MyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, obj):
			return str(obj.id)
	

	class OrderEditForm(forms.Form):
		id = forms.CharField(required=True, max_length=100)
		order_date = forms.DateTimeField(required=True) 
		phone = forms.CharField(required=True, max_length=100)
		date_packed = forms.DateTimeField(required=True)
		date_paid = forms.DateTimeField(required=True)
		date_shipped = forms.DateTimeField(required=True)
		tracking_number = forms.CharField(required=True, max_length=100)
		ship_address1 = forms.CharField(required=True, max_length=100)
		ship_address2 = forms.CharField(required=False, max_length=100)
		ship_city = forms.CharField(required=True, max_length=100)
		ship_state = forms.CharField(required=True, max_length=100)
		ship_zip = forms.CharField(required=True, max_length=100)
		ship_country = forms.CharField(required=True, max_length=100)
		Agent_id = AgentModelChoiceField(
			queryset= hmod.Agent.objects.all(), empty_label=None,
		)
		BulkDetail_id = MyModelChoiceField(
			queryset= hmod.BulkDetail.objects.all(), empty_label=None,
		)
		PersonalDetail_id = MyModelChoiceField(
			queryset= hmod.PersonalDetail.objects.all(), empty_label=None,
		)


	form = OrderEditForm(initial={
	'id': order.id,
	'order_date': order.order_date,
	'phone': order.phone,
	'date_packed': order.date_packed,
	'date_paid': order.date_paid,
	'date_shipped': order.date_shipped,
	'tracking_number': order.tracking_number,
	'ship_address1': order.ship_address1,
	'ship_address2': order.ship_address2,
	'ship_city': order.ship_city,
	'ship_state': order.ship_state,
	'ship_zip': order.ship_zip,
	'ship_country': order.ship_country,
	'Agent_id': order.Agent_id,
	'BulkDetail_id': order.BulkDetail_id,
	'PersonalDetail_id': order.PersonalDetail_id,

	})
	if request.method == 'POST':
		form = OrderEditForm(request.POST)
		if form.is_valid():
			order.id = form.cleaned_data['id']
			order.order_date = form.cleaned_data['order_date']
			order.phone = form.cleaned_data['phone']
			order.date_packed = form.cleaned_data['date_packed']
			order.date_paid = form.cleaned_data['date_paid']
			order.date_shipped = form.cleaned_data['date_shipped']
			order.tracking_number = form.cleaned_data['tracking_number']
			order.ship_address1 = form.cleaned_data['ship_address1']
			order.ship_address2 = form.cleaned_data['ship_address2']
			order.ship_city = form.cleaned_data['ship_city']
			order.ship_state = form.cleaned_data['ship_state']
			order.ship_zip = form.cleaned_data['ship_zip']
			order.ship_country = form.cleaned_data['ship_country']
			order.Agent_id = form.cleaned_data['Agent_id']
			order.BulkDetail_id = form.cleaned_data['BulkDetail_id']
			order.PersonalDetail_id = form.cleaned_data['PersonalDetail_id']
			order.save()
			return HttpResponseRedirect('/homepage/order/')

	params['form'] = form
	return templater.render_to_response(request, 'order.edit.html', params)

