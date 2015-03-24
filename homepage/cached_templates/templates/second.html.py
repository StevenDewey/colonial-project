# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421215173.055821
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/second.html'
_template_uri = 'second.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['leftContent', 'centerContent']


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
        def leftContent():
            return render_leftContent(context._locals(__M_locals))
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'leftContent'):
            context['self'].leftContent(**pageargs)
        

        __M_writer('\r\n    \r\n  \r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_leftContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def leftContent():
            return render_leftContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <h1 style="text-align: center; "><span class="glyphicon glyphicon-star" aria-hidden="true"></span>Welcome to the homepage app!</h1>\r\n  <ul class="nav nav-pills" role="tablist">\r\n  <li style="width: 100%" role="presentation" class="active"><a href="#">Pending Transactions <span class="badge">42</span></a></li>\r\n  <li style="width: 100%" role="presentation"><a href="#">Unfinshined Tickets<span class="badge">21</span></a></li>\r\n  <li style="width: 100%" role="presentation"><a href="#">Missed Calls <span class="badge">3</span></a></li>\r\n</ul>\r\n  \r\n        \r\n      ')
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
        __M_writer('\r\n    <div class="content">\r\n      <h3><span class="label label-default">Wahoo!! -- youve successfully created a new django-mako-plus app!</span></h3>\r\n      <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\r\n    </div>\r\n\t<div class="alert alert-danger" role="alert">\r\n\t\tYou are a fantastic person</div>\r\n    ')

        import random
        r = random.randint(10, 100)
            
        
        __M_writer('\r\n    \r\n\t<h1>')
        __M_writer(str( r ))
        __M_writer('</h1>\r\n\r\n\t<button class="btn btn-success">This is cool</button>\r\n  <button type="button" class="btn btn-primary">This is primarily cooler</button>\r\n\r\n')
        for i in range(50):
            if i % 2 ==0:
                __M_writer('    \t<p>')
                __M_writer(str( i ))
                __M_writer(': welcome to my site</p>\r\n')
        __M_writer('\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 16, "91": 85, "37": 1, "71": 16, "72": 23, "42": 12, "77": 26, "78": 28, "79": 28, "80": 33, "81": 34, "82": 35, "83": 35, "52": 3, "85": 38, "84": 35, "58": 3, "27": 0}, "source_encoding": "ascii", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/second.html", "uri": "second.html"}
__M_END_METADATA
"""
