# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425776889.706298
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/overdue_rental.html'
_template_uri = 'overdue_rental.html'
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
        overdue_rentals = context.get('overdue_rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<html>\r\n<head>\r\n\r\n</head>\r\n<body>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def centerContent():
            return render_centerContent(context)
        overdue_rentals = context.get('overdue_rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        <div class="page-header">\r\n            <h1> Overdue Rental Items <small></small></h1>\r\n        </div>\r\n')
        __M_writer('        <table id="overdue_rental_table" class="table table-bordered table-hover">\r\n            <tr>\r\n                <th> Rented Item </th>\r\n                <th> Customer </th>\r\n                <th> Customer\'s Phone Number </th>\r\n                <th> Date Due </th>\r\n                <th> Replacement Price </th>\r\n            </tr>\r\n\r\n')
        for overdue_rental in overdue_rentals:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( overdue_rental.rental_product.product_specification.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( overdue_rental.order.customer.first_name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( overdue_rental.order.customer.phone ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( overdue_rental.date_due ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( overdue_rental.rental_product.replacement_price ))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "overdue_rental.html", "line_map": {"64": 27, "65": 28, "66": 28, "35": 1, "40": 32, "73": 67, "46": 8, "59": 25, "67": 31, "53": 8, "54": 13, "55": 22, "56": 23, "57": 24, "58": 24, "27": 0, "60": 25, "61": 26, "62": 26, "63": 27}, "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/overdue_rental.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
