from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime

import homepage.models as hmod

templater = get_renderer('homepage')

############################################################
#### Display Checkout Form with Items in Shopping Cart

@view_function
# @login_required(login_url='/homepage/checkout.login/')
def process_request(request):
  params = {}

  return templater.render_to_response(request, 'checkout.html', params)

