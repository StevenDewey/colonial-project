from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib import auth
from django import forms

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/homepage/index/')

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user == None:
            raise forms.ValidationError('Incorrect Username or Password')
        return self.cleaned_data

@view_function
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/homepage/index')

@view_function
def loginform(request):
    params = {}
    print(request)
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')

    params['form'] = form
    return templater.render_to_response(request, 'login.loginform.html', params)
    # return templater.render_to_response(request, 'login.html', params)