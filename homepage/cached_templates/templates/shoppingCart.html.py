# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425960108.579108
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/shoppingCart.html'
_template_uri = 'shoppingCart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        float = context.get('float', UNDEFINED)
        int = context.get('int', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<html>\r\n\t<head>\r\n\t</head>\r\n\t<body>\r\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \r\n\t</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        float = context.get('float', UNDEFINED)
        int = context.get('int', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t<table class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Photo</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Price</th>\r\n\t\t\t\t<th>Quantity</th>\r\n\t\t\t\t<th>Remove from Cart</th>\r\n\t\t\t\t<th>Total</th>\r\n\t\t\t</tr>\r\n')
        for k in products:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( k.name ))
            __M_writer(' \r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<img src="')
            __M_writer(str( k.photo ))
            __M_writer('"/>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( k.description ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( k.price ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td class="qtyContainer">\r\n\t\t\t\t\t\t<input  type="number" id="id_quantity" class="quantity" name="quantity" data-pid="')
            __M_writer(str( k.id ))
            __M_writer('" value="')
            __M_writer(str(products[k]))
            __M_writer('" />\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<button data-pid="')
            __M_writer(str( k.id ))
            __M_writer('" class="remove_btn btn btn-danger">Remove</button>\r\n\t\t\t\t\t</td>\t\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str(round(float(k.price) * int(products[k]), 2)))
            __M_writer('\r\n\t\t\t\t\t</td>\t\r\n\t\t\t\t</tr>\t\r\n')
        __M_writer('\t\t\t\t\r\n\t\t</table>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "shoppingCart.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/shoppingCart.html", "line_map": {"64": 25, "65": 25, "66": 28, "67": 28, "68": 31, "69": 32, "70": 32, "71": 35, "72": 35, "73": 35, "74": 35, "75": 38, "76": 38, "77": 41, "78": 41, "79": 45, "85": 79, "27": 0, "38": 1, "43": 47, "49": 7, "59": 7, "60": 19, "61": 20, "62": 22, "63": 22}, "source_encoding": "ascii"}
__M_END_METADATA
"""
