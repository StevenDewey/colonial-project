# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425773791.421042
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/user.edit.html'
_template_uri = 'user.edit.html'
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
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def centerContent():
            return render_centerContent(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="clear">\r\n\t\t<form method="POST">\r\n\t\t\t<table>\r\n\t\t\t<span id="id_username_message_valid"></span><span id="id_username_message_invalid"></span>\r\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t\t\t\r\n\t\t\t</table>\r\n\t\t\t<button id="create_submit_button" type="submit">Submit</button>\r\n\t\t</form>\r\n\t</div>\r\n\r\n\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "53": 8, "54": 8, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/user.edit.html", "uri": "user.edit.html"}
__M_END_METADATA
"""
