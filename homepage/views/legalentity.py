from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	legalentitys = hmod.LegalEntity.objects.all()
	
	params['legalentitys'] = legalentitys

	return templater.render_to_response(request, 'legalentity.html', params)

