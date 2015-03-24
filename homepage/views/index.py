from django.conf import settings
from django.http import HttpResponse 
from django_mako_plus.controller import view_function 
from .. import dmp_render, dmp_render_to_response
import homepage.models as hmod

@view_function 
def process_request(request):
	template_vars = {}
	return dmp_render_to_response(request, 'index.html', template_vars)

@view_function 
def check_username(request):
	username = request.REQUEST.get('u')
	try:
		user = hmod.User.objects.get(username=username)
		return HttpResponse('0')
	except hmod.User.DoesNotExist:
		return HttpResponse('1')
	
	print('>>>>>>>>>>>>>>>', username)
	#check to see if in db

