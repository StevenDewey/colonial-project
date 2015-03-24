# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425161234.450914
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\t<div><br>\r\n\t\t<h1 class="clear">Welcome to the Colonial Heritage Foundation Web Application</h1>\r\n\t\t<br>\r\n\t\t<div class="panel panel-primary">\r\n        <div class="panel-heading">\r\n         <h3 class="panel-title">What is the Colonial Heritage Foundation?</h3>\r\n        </div>\r\n        <div class="panel-body">\r\n        The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America\r\n        </div>\r\n        </div>\r\n        <form action="Post">\r\n            <input type="text" id="id_username"/>\r\n            <span id="id_username_message"></span>\r\n        </form>\r\n    </div>\r\n\t\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
