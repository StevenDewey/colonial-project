# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425784592.930906
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/product_detail.html'
_template_uri = 'product_detail.html'
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
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<html>\r\n<head>\r\n\r\n\t<title></title>\r\n</head>\r\n<body>\r\n\r\n')
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
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<a href="/product"><button class="right btn btn-primary">Back To Products</button></a>\r\n\t<h1> ')
        __M_writer(str( product.name ))
        __M_writer(' <br> </h1>\r\n\t\t<div class="productDiv">\r\n\t\t\t<img src="')
        __M_writer(str( product.photo ))
        __M_writer('"/>\r\n\t\t\t<div>\r\n\t\t\t\t<p>Description: </p>')
        __M_writer(str( product.description ))
        __M_writer('<br>\r\n\t\t\t\t<p>Price: </p>')
        __M_writer(str( product.price ))
        __M_writer('\r\n\t\t\t</div>\r\n\t\t\t<div class="center">\r\n\t\t\t\t<form >\r\n\t\t\t\t\t<label for="quantity">Qty: </label>\r\n\t\t\t\t\t<input min="1" type="number" id="quantity" name="quantity" value="1" />\r\n\t\t\t\t</form>\r\n\t\t\t\t<button data-pid="')
        __M_writer(str( product.id ))
        __M_writer('" class="add_button btn btn-warning">Buy Now</button>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t\r\n\t\t\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "product_detail.html", "line_map": {"35": 1, "69": 63, "40": 29, "46": 10, "59": 16, "53": 10, "54": 12, "55": 12, "56": 14, "57": 14, "58": 16, "27": 0, "60": 17, "61": 17, "62": 24, "63": 24}, "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/product_detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
