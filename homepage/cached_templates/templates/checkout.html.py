# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426780225.061381
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        request = context.get('request', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n    <br>\r\n      <h3>Checkout Page</h3>\r\n      <h4>Credit Card Information</h4>\r\n\t\t<form>\r\n\t\tCredit Card Number:<br>\r\n\t\t<input type="text" name="card_number">\r\n\t\t<br>\r\n\t\tExpiration Date:<br>\r\n\t\t<input type="text" name="exp_date">\r\n\t\t<br>\r\n\t\tCVV:<br>\r\n\t\t<input type="text" name="cvv">\r\n\t\t<br>\r\n\t\t</form>\r\n\t\t<h4>Shipping Address</h4>\r\n\t\t<form>\r\n\t\tStreet1:<br>\r\n\t\t<input type="text" name="card_number">\r\n\t\t<br>\r\n\t\tStreet2:<br>\r\n\t\t<input type="text" name="exp_date">\r\n\t\t<br>\r\n\t\tCity:<br>\r\n\t\t<input type="text" name="cvv">\r\n\t\t<br>\r\n\t\tState:<br>\r\n\t\t<input type="text" name="cvv">\r\n\t\t<br>\r\n\t\tZip:<br>\r\n\t\t<input type="text" name="cvv">\r\n\t\t<br>\r\n\t\t</form>\r\n      <a href="/homepage/thankyou/"><button id="process_payment_btn" class="btn btn-warning">Process Payment</button></a>\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t\t\t<p></p>\r\n')
        else:
            __M_writer('\t\t\t\t<div class="modal fade" id="checkout_login" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t\t\t\t  <div class="modal-dialog">\r\n\t\t\t\t    <div class="modal-content">\r\n\t\t\t\t      <div class="modal-header">\r\n\t\t\t\t        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t\t        <h4 class="modal-title" id="myModalLabel">Must Login to Checkout</h4>\r\n\t\t\t\t      </div>\r\n\t\t\t\t      <div class="modal-body">\r\n\t\t\t\t        ...\r\n\t\t\t\t      </div>\r\n')
            __M_writer('\t\t\t\t    </div>\r\n\t\t\t\t  </div>\r\n\t\t\t\t</div>\r\n\t\t\t\t</div><!-- End Modal -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/checkout.html", "line_map": {"35": 1, "52": 3, "53": 39, "54": 40, "55": 41, "56": 42, "57": 56, "27": 0, "45": 3, "63": 57}, "source_encoding": "ascii", "uri": "checkout.html"}
__M_END_METADATA
"""
