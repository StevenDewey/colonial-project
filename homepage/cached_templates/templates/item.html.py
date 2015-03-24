# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374177.227939
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/item.html'
_template_uri = 'item.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-right">\r\n\t<a href="/homepage/item.create/" class="btn btn-warning" style="margin-bottom: 10px">Create New Item</a>\r\n\t</div>\r\n\t<div class="tableContain">\r\n\t<h1>Items</h1>\r\n\t\t<table class="table table-hover table-bordered table-responsive">\r\n\t\t<th>ID</th>\r\n\t\t<th>Name</th>\r\n\t\t<th>Description</th>\r\n\t\t<th>Value</th>\r\n\t\t<th>Standard Rental Price</th>\r\n\t\t<th>Legal Entity ID</th>\r\n\t\t<th>Edit | Delete</th>\r\n\t\t\r\n')
        for item in items:
            __M_writer('\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.value ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( item.legal_entity_id ))
            __M_writer('</td>\r\n\t\t\t\t<td><a href="/homepage/item.edit/')
            __M_writer(str( item.id ))
            __M_writer('">Edit</a> | <a href="/homepage/item.delete/')
            __M_writer(str( item.id ))
            __M_writer('/">Delete</a></td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "item.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/item.html", "line_map": {"64": 33, "65": 33, "66": 34, "67": 34, "68": 35, "69": 35, "70": 35, "71": 35, "72": 38, "78": 72, "27": 0, "35": 1, "40": 40, "46": 11, "53": 11, "54": 26, "55": 27, "56": 29, "57": 29, "58": 30, "59": 30, "60": 31, "61": 31, "62": 32, "63": 32}}
__M_END_METADATA
"""
