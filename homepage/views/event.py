from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
import homepage.models as hmod
from django.forms import ModelChoiceField
from django import forms

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	events = hmod.Event.objects.all().order_by('id')
	
	params['events'] = events

	return templater.render_to_response(request, 'event.html', params)

@view_function
@permission_required('homepage.add_event', login_url='/homepage/login.notAuthorized/')
def create(request):
	event = hmod.Event()
	event.name = "New Event"
	event.description = "New Event"
	event.start_date = "2000-01-01"
	event.end_date = '2000-01-01'
	event.map_file_name = ''
	event.venue_name = "New Event Venue"
	#event.address = ""
	event.save()

	return HttpResponseRedirect('/homepage/event.edit/{}/'.format(event.id))

@view_function
@permission_required('homepage.delete_event', login_url='/homepage/login.notAuthorized/')
def delete(request):
	'''delete an rental'''

	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		return HttpResponseRedirect('/homepage/event/')

	event.delete()

	return HttpResponseRedirect('/homepage/event/'.format(event.id))

@view_function
@permission_required('homepage.change_event', login_url='/homepage/login.notAuthorized/') 
def edit(request):
	params = {}

	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		return HttpResponseRedirect('/homepage/event/')

	class AddressMyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, adr):
			return str(adr.id) + " - " + adr.street1 + " " + adr.city + " " + adr.state + " " + adr.zip_code + " " + adr.country

	class EventEditForm(forms.Form):
		id = forms.CharField(required=True, max_length=100)
		name = forms.CharField(required=True,  max_length=200)
		description = forms.CharField(required=True,  max_length=1000)  
		start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'})) 
		end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
		map_file_name = forms.CharField(required=True, max_length=100)
		address = address = AddressMyModelChoiceField(
			queryset= hmod.Address.objects.all(), empty_label=None,
		)

	form = EventEditForm(initial={
	'id': event.id,
	'name': event.name,
	'description': event.description,
	'start_date': event.start_date,
	'end_date': event.end_date,
	'map_file_name': event.map_file_name,
	'address': event.address,
	})
	if request.method == 'POST':
		form = EventEditForm(request.POST)
		if form.is_valid():
			event.id = form.cleaned_data['id']
			event.description = form.cleaned_data['description']
			event.start_date = form.cleaned_data['start_date']
			event.end_date = form.cleaned_data['end_date']
			event.map_file_name = form.cleaned_data['map_file_name']
			event.address = form.cleaned_data['address']
			event.save()
			return HttpResponseRedirect('/homepage/event/')

	params['form'] = form
	return templater.render_to_response(request, 'event.edit.html', params)
