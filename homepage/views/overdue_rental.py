from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
import datetime
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    overdue_rentals= hmod.RentalItem.objects.filter(date_due__lte = datetime.datetime.today())#.order_by('date_due')
    params['overdue_rentals'] = overdue_rentals

    return templater.render_to_response(request, 'overdue_rental.html', params)