# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421164778.173546
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/about.html'
_template_uri = 'about.html'
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
        range = context.get('range', UNDEFINED)
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
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Wahoo!! -- youve successfully created a new django-mako-plus app!</h3>\r\n      <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\r\n    </div>\r\n\t<div class="alert alert-danger" role="alert">\r\n\t\tYou are a fantastic person</div>\r\n')

        import random
        r = random.randint(10, 100)
        
        
        __M_writer('\r\n\t<h1>')
        __M_writer(str( r ))
        __M_writer('</h1>\r\n\r\n\t<button class="btn btn-success">This is cool</button>\r\n\r\n\r\n')
        for i in range(50):
            if i % 2 ==0:
                __M_writer('    \t<p>')
                __M_writer(str( i ))
                __M_writer(': welcome to my site</p>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 21, "65": 21, "66": 24, "35": 1, "72": 66, "45": 3, "27": 0, "52": 3, "53": 10, "58": 13, "59": 14, "60": 14, "61": 19, "62": 20, "63": 21}, "uri": "about.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/about.html"}
__M_END_METADATA
"""
