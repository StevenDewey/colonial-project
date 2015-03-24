# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374188.896392
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/rental.html'
_template_uri = 'rental.html'
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
        rentals = context.get('rentals', UNDEFINED)
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<html>\r\n<head>\r\n<!-- Latest compiled and minified CSS -->\r\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n\t<title></title>\r\n</head>\r\n<body>\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentals = context.get('rentals', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-right">\r\n\t\t<a href="/homepage/rental.create/" class="btn btn-warning" style="margin-bottom: 10px">Create New Rental</a>\r\n\t</div>\r\n\t<div class="tableContain">\r\n\t<h1>Rentals</h1>\r\n\t\t<table class="table table-hover table-bordered table-responsive">\r\n\t\t<th>ID</th>\r\n\t\t<th>Rental Time</th>\r\n\t\t<th>Discount Percent</th>\r\n\t\t<th>Organization ID</th>\r\n\t\t<th>Person ID</th>\r\n\t\t<th>Agent ID</th>\r\n\t\t<th>Edit | Delete</th>\r\n\t\t\r\n')
        for rental in rentals:
            __M_writer('\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.rental_time ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.discount_percent ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.Organization_id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.Person_id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( rental.Agent_id ))
            __M_writer('</td>\r\n\t\t\t\t<td><a href="/homepage/rental.edit/')
            __M_writer(str( rental.id ))
            __M_writer('">Edit</a> | <a href="/homepage/rental.delete/')
            __M_writer(str( rental.id ))
            __M_writer('/">Delete</a></td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rental.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/rental.html", "line_map": {"64": 35, "65": 35, "66": 36, "67": 36, "68": 37, "69": 37, "70": 37, "71": 37, "72": 40, "78": 72, "27": 0, "35": 1, "40": 42, "46": 13, "53": 13, "54": 28, "55": 29, "56": 31, "57": 31, "58": 32, "59": 32, "60": 33, "61": 33, "62": 34, "63": 34}}
__M_END_METADATA
"""
