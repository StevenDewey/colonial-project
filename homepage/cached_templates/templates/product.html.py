# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425784601.032523
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/product.html'
_template_uri = 'product.html'
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def centerContent():
            return render_centerContent(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="text-right">\r\n\t\t<input id="search"/> <button class="filter btn btn-info" >Search</button> <div id="results"></div>\r\n')
        __M_writer('</div>\r\n\t<div class="tableContain">\r\n\t<h1>Products</h1>\r\n\t\r\n\t\t<div id="DisplayProducts">\r\n\t\t\t<div class="displaystuff">\r\n')
        for product in products:
            __M_writer('\t\t\t\t<div class="productstuff">\r\n\t\t\t\t\t<div class="productDiv">\r\n\t\t\t\t\t\t<a href="/product_detail/')
            __M_writer(str( product.id ))
            __M_writer('"><img src="')
            __M_writer(str( product.photo ))
            __M_writer('"/></a>\r\n\t\t\t\t\t\t<div class="buyButton"><a href="/product_detail/')
            __M_writer(str( product.id ))
            __M_writer('">')
            __M_writer(str( product.name ))
            __M_writer('</a></div>\r\n\t\t\t\t\t\t<p>Description: </p>')
            __M_writer(str( product.description ))
            __M_writer('<br>\r\n\t\t\t\t\t\t<p>Price: </p>')
            __M_writer(str( product.price ))
            __M_writer(' <br>\r\n\t\t\t\t\t\t<div class="buyButton">\r\n\t\t\t\t\t\t\t<button data-pid="')
            __M_writer(str( product.id ))
            __M_writer('" class="add_button btn btn-warning">Buy Now</button>\r\n\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\r\n')
        __M_writer('\t\t\t</div>\r\n\t\t</div>\r\n\t\t\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "product.html", "line_map": {"64": 17, "65": 18, "66": 18, "67": 19, "68": 19, "69": 21, "70": 21, "71": 29, "77": 71, "27": 0, "35": 1, "40": 33, "46": 3, "53": 3, "54": 7, "55": 13, "56": 14, "57": 16, "58": 16, "59": 16, "60": 16, "61": 17, "62": 17, "63": 17}, "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/product.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
