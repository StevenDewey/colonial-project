# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425798165.066361
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/searchProducts.html'
_template_uri = 'searchProducts.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        for product in products:
            __M_writer('\t<div class="productstuff">\r\n\t\t<div class="productDiv">\r\n\t\t\t<a href="/product_detail/')
            __M_writer(str( product.id ))
            __M_writer('"><img src="')
            __M_writer(str( product.photo ))
            __M_writer('"/></a>\r\n\t\t\t<div class="buyButton"><a href="/product_detail/')
            __M_writer(str( product.id ))
            __M_writer('">')
            __M_writer(str( product.name ))
            __M_writer('</a></div>\r\n\t\t\t<p>Description: </p>')
            __M_writer(str( product.description ))
            __M_writer('<br>\r\n\t\t\t<p>Price: </p>')
            __M_writer(str( product.price ))
            __M_writer(' <br>\r\n\t\t\t<div class="buyButton">\r\n\t\t\t\t<button data-pid="')
            __M_writer(str( product.id ))
            __M_writer('" class="add_button btn btn-warning">Buy Now</button>\r\n\r\n\t\t\t</div>\r\n\t\t</div>\r\n\r\n\t</div>\r\n\t\t\t\t\t\t\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 6, "33": 6, "34": 7, "35": 7, "36": 9, "37": 9, "43": 37, "16": 0, "22": 1, "23": 2, "24": 4, "25": 4, "26": 4, "27": 4, "28": 5, "29": 5, "30": 5, "31": 5}, "source_encoding": "ascii", "uri": "searchProducts.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/searchProducts.html"}
__M_END_METADATA
"""
