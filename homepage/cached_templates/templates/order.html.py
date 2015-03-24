# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374194.104419
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/order.html'
_template_uri = 'order.html'
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
        orders = context.get('orders', UNDEFINED)
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
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
        orders = context.get('orders', UNDEFINED)
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="text-right">\r\n\t\t<a href="/homepage/order.create/" class="btn btn-warning" style="margin-bottom: 10px">Create New Order</a>\r\n</div>\r\n\t<div class="tableContain">\r\n\t<h1>Orders</h1>\r\n\t\t<table class="table table-hover table-bordered table-responsive">\r\n\t\t<th>ID</th>\r\n\t\t<th>Order Date</th>\r\n\t\t<th>Phone</th>\r\n\t\t<th>Date Packed</th>\r\n\t\t<th>Date Paid</th>\r\n\t\t<th>Date Shipped</th>\r\n\t\t<th>Tracking Number</th>\r\n\t\t<th>Shipping Address 1</th>\r\n\t\t<th>Shipping Address 2</th>\r\n\t\t<th>Shipping City</th>\r\n\t\t<th>Shipping State</th>\r\n\t\t<th>Shipping Country</th>\r\n\t\t<th>AgentID</th>\r\n\t\t<th>BulkDetail ID</th>\r\n\t\t<th>Personal Detail ID</th>\r\n\t\t<th>Edit | Delete</th>\r\n\t\t\r\n')
        for order in orders:
            __M_writer('\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str( order.id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.order_date ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.phone ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.date_packed ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.date_paid ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.date_shipped ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.tracking_number ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.ship_address1 ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.ship_address2 ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.ship_city ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.ship_state ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.ship_country ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.Agent_id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.BulkDetail_id ))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str( order.PersonalDetail_id ))
            __M_writer('</td>\r\n\r\n\t\t\t\t<td><a href="/homepage/order.edit/')
            __M_writer(str( order.id ))
            __M_writer('">Edit</a> | <a href="/homepage/order.delete/')
            __M_writer(str( order.id ))
            __M_writer('/">Delete</a></td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "order.html", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/order.html", "line_map": {"64": 42, "65": 42, "66": 43, "67": 43, "68": 44, "69": 44, "70": 45, "71": 45, "72": 46, "73": 46, "74": 47, "75": 47, "76": 48, "77": 48, "78": 49, "79": 49, "80": 50, "81": 50, "82": 51, "83": 51, "84": 52, "85": 52, "86": 54, "87": 54, "88": 54, "89": 54, "90": 57, "27": 0, "96": 90, "35": 1, "40": 59, "46": 11, "53": 11, "54": 35, "55": 36, "56": 38, "57": 38, "58": 39, "59": 39, "60": 40, "61": 40, "62": 41, "63": 41}}
__M_END_METADATA
"""
