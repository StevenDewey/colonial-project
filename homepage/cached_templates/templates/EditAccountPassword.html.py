# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425769940.737785
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/EditAccountPassword.html'
_template_uri = 'EditAccountPassword.html'
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
        error = context.get('error', UNDEFINED)
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
        error = context.get('error', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="content">\r\n        <form method="POST">\r\n            <table style="margin-top:37px;">\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n            </table>\r\n            <h5 class="error">')
        __M_writer(str( error ))
        __M_writer('</h5>\r\n            <button type="submit">Submit</button>\r\n        </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "36": 1, "54": 3, "55": 8, "56": 8, "57": 10, "58": 10, "27": 0, "46": 3}, "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/EditAccountPassword.html", "uri": "EditAccountPassword.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
