# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422770885.501316
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/legalentity.html'
_template_uri = 'legalentity.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['centerContent']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        legalentitys = context.get('legalentitys', UNDEFINED)
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<html>\r\n<head>\r\n<!-- Latest compiled and minified CSS -->\r\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n\t<title></title>\r\n</head>\r\n<body>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        legalentitys = context.get('legalentitys', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<table class="table table-hover table-bordered table-responsive">\r\n\t<th>First Name</th>\r\n\t<th>Last Name</th>\r\n\t<th>Address 1</th>\r\n\t<th>Address 2</th>\r\n\t<th>City</th>\r\n\t<th>State</th>\r\n\t<th>Zip Code</th>\r\n\t<th>Email</th>\r\n\t<th>Birthday</th>\r\n\t<th>Biographical Sketch</th>\r\n\t<th>Emergency Contact Relationship</th>\r\n\t<th>PhotoID</th>\r\n\t<th>Appointment Date</th>\r\n\t<th>Edit/Delete</th>\r\n')
        for legalentity in legalentitys:
            __M_writer('\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.given_name ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.person.family_name ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.address1 ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.address2 ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.city ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.state ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.zip_code ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.email ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.creation_date ))
            __M_writer('</td>\r\n\t\t\t<td>')
            __M_writer(str( legalentity.Person.Participant.biographical_sketch ))
            __M_writer('</td>\r\n\r\n\t\t\t<td><a href="/homepage/">Edit</a> | Delete</td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "legalentity.html", "source_encoding": "ascii", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/legalentity.html", "line_map": {"64": 34, "65": 34, "66": 35, "67": 35, "68": 36, "69": 36, "70": 37, "71": 37, "72": 38, "73": 38, "74": 39, "75": 39, "76": 44, "82": 76, "27": 0, "35": 1, "40": 45, "46": 11, "53": 11, "54": 27, "55": 28, "56": 30, "57": 30, "58": 31, "59": 31, "60": 32, "61": 32, "62": 33, "63": 33}}
__M_END_METADATA
"""
