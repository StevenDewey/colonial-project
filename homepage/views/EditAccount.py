from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django import forms

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

    #################### How do you pass more than one set of params??
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/')

    if request.urlparams[1] != "None":
        try:
            address = hmod.Address.objects.get(id=request.urlparams[1])
        except hmod.Address.DoesNotExist:
            return HttpResponseRedirect('/homepage/')
    else:
        address = hmod.Address()
        address.street1 = ''
        address.street2 = ''
        address.city = ''
        address.state = ''
        address.zip_code = ''
        address.country = ''
        address.save()


    class userEditForm(forms.Form):
        first_name = forms.CharField(required=True, max_length=100)
        last_name = forms.CharField(required=True, max_length=100)
        email = forms.CharField(required=True, max_length=100)
        security_question = forms.CharField(required=True, max_length=100)
        security_answer = forms.CharField(required=True, max_length=100)
        phone = forms.CharField(required=True, max_length=100)
        street1 = forms.CharField(required=True, max_length=100)
        street2 = forms.CharField(required=False, max_length=100)
        city = forms.CharField(required=True, max_length=100)
        state = forms.CharField(required=True, max_length=100)
        zip_code = forms.CharField(required=True, max_length=100)
        country = forms.CharField(required=True, max_length=100)

        #def clean_start_date(self):
        #    if self.cleaned_data['start_date'] != "????-??-??":
        #        raise forms.ValidationError("Type in a date with this format: YYYY-MM-DD")

    form = userEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'security_question': user.security_question,
        'security_answer': user.security_answer,
        'phone': user.phone,
        'street1': address.street1,
        'street2': address.street2,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code,
        'country': address.country,

    })

    if request.method == 'POST':
        form = userEditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.phone = form.cleaned_data['phone']
            address.street1 = form.cleaned_data['street1']
            address.street2 = form.cleaned_data['street2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.zip_code = form.cleaned_data['zip_code']
            address.country = form.cleaned_data['country']

            address.save()

            user.address_id = address.id

            user.save()
            return HttpResponseRedirect('/homepage/')

    params['user'] = user
    params['form'] = form
    return templater.render_to_response(request, 'EditAccount.html', params)

@view_function
def changePassword(request):

    params = {}

    #################### How do you pass more than one set of params??
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/')


    class userEditForm(forms.Form):
        username = forms.CharField(required=True, max_length=100)
        new_password = forms.CharField(required=True, widget=forms.PasswordInput)
        confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)


    form = userEditForm(initial={
        'username': user.username,
        'new_password': user.password,
        'confirm_password': user.password,
    })

    hi=False

    if request.method == 'POST':
        form = userEditForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['new_password'] == form.cleaned_data['confirm_password']:
                user.username = form.cleaned_data['username']
                user.set_password(form.cleaned_data['new_password'])

                user.save()

                userauth = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['new_password'])
                login(request, userauth)

                return HttpResponseRedirect('/homepage/EditAccount/{}/'.format(user.id) + '{}/'.format(user.address_id))
            else:
                hi = True
                pass

    if hi:
        params['error'] = "Passwords don't match"
    else:
        params['error'] = ""
    params['user'] = user
    params['form'] = form
    return templater.render_to_response(request, 'EditAccountPassword.html', params)