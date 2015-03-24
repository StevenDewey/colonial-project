# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425962282.033684
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/EditAccount.html'
_template_uri = 'EditAccount.html'
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
        form = context.get('form', UNDEFINED)
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <a href="/homepage/index" class="cancel">Cancel</a>\r\n    <div class="content">\r\n        <form method="POST">\r\n            <table style="margin-top:37px;">\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n                <img src="/static/homepage/media/productPictures/barrell.jpg" class="profile_pic" align="right"/>\r\n            </table>\r\n            <button type="submit">Submit</button>\r\n            <a href="/homepage/EditAccount.changePassword/')
        __M_writer(str( user.id ))
        __M_writer('/" >Change Username/Password</a>\r\n        </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "EditAccount.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/EditAccount.html", "line_map": {"64": 58, "36": 1, "54": 3, "55": 9, "56": 9, "57": 13, "58": 13, "27": 0, "46": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
