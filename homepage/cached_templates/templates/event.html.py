# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425167445.543032
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/event.html'
_template_uri = 'event.html'
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
        events = context.get('events', UNDEFINED)
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
        def centerContent():
            return render_centerContent(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="text-right">\r\n\t\t<a href="/homepage/event.create/" class="btn btn-warning" style="margin-bottom: 10px">Create New Event</a>\r\n</div>\r\n\t<div class="tableContain">\r\n\t<h1>Events</h1>\r\n\t\t<table class="table table-hover table-bordered table-responsive">\r\n\t\t<th>ID</th>\r\n\t\t<th>Start Date</th>\r\n\t\t<th>End Date</th>\r\n\t\t<th>Map File Name</th>\r\n\t\t<th>Edit | Delete</th>\r\n\t\t\r\n')
        for event in events:
            __M_writer('\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str( event.id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.start_date ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.end_date ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.map_file_name ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( event.address ))
            __M_writer('</td>\r\n\t\t\t\t\r\n\t\t\t\t<td><a href="/homepage/event.edit/')
            __M_writer(str( event.id ))
            __M_writer('">Edit</a> | <a href="/homepage/event.delete/')
            __M_writer(str( event.id ))
            __M_writer('/">Delete</a></td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/event.html", "uri": "event.html", "line_map": {"64": 31, "65": 31, "66": 32, "67": 32, "68": 33, "69": 33, "70": 35, "71": 35, "72": 35, "73": 35, "74": 38, "80": 74, "27": 0, "35": 1, "40": 40, "46": 11, "53": 11, "54": 24, "55": 25, "56": 27, "57": 27, "58": 28, "59": 28, "60": 29, "61": 29, "62": 30, "63": 30}, "source_encoding": "ascii"}
__M_END_METADATA
"""
