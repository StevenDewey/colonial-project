# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423375004.043891
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/notAuthorized.html'
_template_uri = 'notAuthorized.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<head>\r\n\t<!-- Latest compiled and minified CSS -->\r\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n</head>\r\n\t<div class="jumbotron">\r\n\t  <h1>You are not authorized to perform this action!</h1>\r\n\t  <p>Please ask a manager or administrator to receive authorization. Until then please return back to the home screen by clicking below</p>\r\n\t  <p><a class="btn btn-primary btn-lg" href="/homepage/index/" role="button">Home</a></p>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "notAuthorized.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/notAuthorized.html", "line_map": {"16": 0, "27": 21, "21": 1}}
__M_END_METADATA
"""
