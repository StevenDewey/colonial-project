# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425354762.374921
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/user.html'
_template_uri = 'user.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n\t<div class="text-right">\r\n\t<a href="/homepage/user.create/" class="btn btn-warning" style="margin-bottom: 10px">Create New User</a>\r\n\t</div>\r\n\r\n\t<div class="tableContain">\r\n\t<h1>Current Users</h1>\r\n\t\t<table class="table table-hover table-bordered table-responsive">\r\n\t\t<th>ID</th>\r\n\t\t<th>Username</th>\r\n\t\t<th>First Name</th>\r\n\t\t<th>Last Name</th>\r\n\t\t<th>Email</th>\r\n\t\t<th>Phone</th>\r\n\t\t<th>Address</th>\r\n\t\t<th>Photo</th>\r\n\t\t<th>Organization Name</th>\r\n\t\t<th>Emergency Contact</th>\r\n\t\t<th>Relationship</th>\r\n\t\t<th>Phone</th>\r\n\t\t<th>Edit | Delete</th>\r\n\t\t\r\n')
        for user in users:
            __M_writer('\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str( user.id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.username ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.phone ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.address ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.photo ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.organization_name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.emergency_contact ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.emergency_relationship ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( user.emergency_phone ))
            __M_writer('</td>\r\n\t\t\t\t<td><a href="/homepage/user.edit/')
            __M_writer(str( user.id ))
            __M_writer('">Edit</a> | <a href="/homepage/user.delete/')
            __M_writer(str( user.id ))
            __M_writer('/">Delete</a></td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/user.html", "source_encoding": "ascii", "line_map": {"64": 41, "65": 41, "66": 42, "67": 42, "68": 43, "69": 43, "70": 44, "71": 44, "72": 45, "73": 45, "74": 46, "75": 46, "76": 47, "77": 47, "78": 48, "79": 48, "80": 49, "81": 49, "82": 49, "83": 49, "84": 52, "90": 84, "27": 0, "35": 1, "40": 54, "46": 11, "53": 11, "54": 34, "55": 35, "56": 37, "57": 37, "58": 38, "59": 38, "60": 39, "61": 39, "62": 40, "63": 40}, "uri": "user.html"}
__M_END_METADATA
"""
