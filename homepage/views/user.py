from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.forms import ModelChoiceField
import homepage.models as hmod
from django import forms
from django.contrib.auth import authenticate, login

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	users = hmod.User.objects.all().order_by('id')
	
	params['users'] = users

	return templater.render_to_response(request, 'user.html', params)

@view_function
def create(request):
	user = hmod.User()
	user.username = ""
	user.password = "" 
	user.first_name = ""
	user.last_name = ""
	user.email = ""
	# user.phone = ""
	# #user.address = ""
	# user.security_question = ""
	# user.security_answer = ""
	# user.requires_reset = ""
	user.save()

	return HttpResponseRedirect('/homepage/user.edit/{}/'.format(user.id))


@view_function
@permission_required('homepage.delete_user', login_url='/homepage/login.notAuthorized/')
def delete(request):
	'''delete an user'''

	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/user/')

	user.delete()

	return HttpResponseRedirect('/homepage/user/'.format(user.id))

@view_function 
def edit(request):
	params = {}

	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/user/')

	class AddressMyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, adr):
			return str(adr.id) + " - " + adr.street1 + " " + adr.city + " " + adr.state + " " + adr.zip_code + " " + adr.country

	class PhotoMyModelChoiceField(ModelChoiceField):
		def label_from_instance(self, pho):
			return str(pho.id) + " - " + pho.description

	class UserEditForm(forms.Form):
		# id = forms.CharField(required=True, max_length=100)
		username = forms.CharField(required=True, max_length=100) 
		password = forms.CharField(required=True, widget=forms.PasswordInput)
		first_name = forms.CharField(required=True, max_length=100)
		last_name = forms.CharField(required=True, max_length=100)
		email = forms.CharField(required=True)
		# phone = forms.CharField(required=True)
		# address = AddressMyModelChoiceField(
		# 	queryset= hmod.Address.objects.all(), empty_label=None,
		# )
		# photo = PhotoMyModelChoiceField(
		# 	queryset= hmod.Photograph.objects.all(), empty_label=None,
		# )
		# organization_name = forms.CharField(required=True)
		# organization_type = forms.CharField(required=True)
		# date_appointed_agent = forms.DateField(widget=forms.TextInput(attrs={'id': 'datepicker'}))
		# relationship = forms.CharField(required=True)
		# emergency_contact = forms.CharField(required=True)
		# emergency_phone = forms.CharField(required=True)
		# emergency_relationship = forms.CharField(required=True)
		# security_question = forms.CharField(required=True)
		# security_answer = forms.CharField(required=True)
		
	form = UserEditForm(initial={
	# 'id': user.id,
	'username': user.username,
	'password': user.password,
	'first_name': user.first_name,
	'last_name': user.last_name,
	'email': user.email,
	# 'phone': user.phone,
	# 'address': user.address,
	# 'photo': user.photo,
	# 'organization_name': user.organization_name,
	# 'organization_type': user.organization_type,
	# 'date_appointed_agent': user.date_appointed_agent,
	# 'relationship': user.relationship,
	# 'emergency_contact': user.emergency_contact,
	# 'emergency_phone': user.emergency_phone,
	# 'emergency_relationship': user.emergency_relationship,
	# 'security_question' : user.security_question,
	# 'security_answer': user.security_answer,
	

	})
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		if form.is_valid():
			#user.id = form.cleaned_data['id']
			user.username = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			# user.phone = form.cleaned_data['phone']
			# user.address = form.cleaned_data['address']
			# user.photo = form.cleaned_data['photo']
			# user.organization_name = form.cleaned_data['organization_name']
			# user.organization_type = form.cleaned_data['organization_type']
			# user.date_appointed_agent = form.cleaned_data['date_appointed_agent']
			# user.relationship = form.cleaned_data['relationship']
			# user.emergency_contact = form.cleaned_data['emergency_contact']
			# user.emergency_phone = form.cleaned_data['emergency_phone']
			# user.emergency_relationship = form.cleaned_data['emergency_relationship']
			# user.security_question = form.cleaned_data['security_question']
			# user.security_answer = form.cleaned_data['security_question']
			user.save()
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			return HttpResponseRedirect('/homepage/user/')

	params['form'] = form
	return templater.render_to_response(request, 'user.edit.html', params)

@view_function
def check_username(request):
    username = request.REQUEST.get('u')

    #check to see if in database
    #make sure you take care of the case where I set my own username to the same username
    try:
        user = hmod.User.objects.get(username=username)# if exists:
        return HttpResponse('Exists')
    except hmod.User.DoesNotExist: # if does not exist
        return HttpResponse('DoesNotExist')
