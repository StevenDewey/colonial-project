# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427173549.832606
_enable_loop = True
_template_filename = 'C:\\Users\\Steven\\test_dmp\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['centerContent']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def centerContent():
            return render_centerContent(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n        \r\n        <link rel="stylesheet" type="text/css" href="/static/homepage/styles/style.css">\r\n\r\n    <title>homepage</title>\r\n    \r\n    \r\n')
        __M_writer('\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n    <link rel="icon" type="image/jpeg" href="/static/homepage/media/KordLordab.jpg" />\r\n  <meta charset="utf-8">\r\n  \r\n  \r\n  \r\n  \r\n  <link rel="stylesheet" type="text/css" href="/static/homepage/datetimepicker-master/jquery.datetimepicker.css"/ >\r\n  <script src="/static/homepage/datetimepicker-master/jquery.js"></script>\r\n  <script src="/static/homepage/datetimepicker-master/jquery.datetimepicker.js"></script>\r\n\r\n  <link rel="stylesheet" href="http://code.jquery.com/ui/1.11.3/themes/smoothness/jquery-ui.css">\r\n  <script src="http://code.jquery.com/jquery-1.10.2.js"></script>\r\n  <script src="http://code.jquery.com/ui/1.11.3/jquery-ui.js"></script>\r\n  <script type="text/javascript" src="//code.jquery.com/jquery-1.11.2.min.js"></script>\r\n  <!--<script type="text/javascript" src="/static/homepage/js/script.js"></script>-->\r\n  <!-- Latest compiled and minified JavaScript -->\r\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n  </head>\r\n  <body>\r\n  <!--\r\n    <header>\r\n     <a href="/homepage/index"><h3>Home</h3></a>\r\n     <a href="/homepage/user"><h3>Users</h3></a>\r\n     <a href="/homepage/item"><h3>Items</h3></a>\r\n   <!-  <a href="/homepage/rental"><h3>Rentals</h3></a>\r\n     <a href="/homepage/order"><h3>Orders</h3></a>->\r\n     <a href="/homepage/event"><h3>Events</h3></a>\r\n     <a href="/homepage/product"><h3>Products</h3></a>\r\n     <a href id="show_login_dialog" data-toggle="modal" data-target="#login_dialog"><h3>Sign In</h3></a>\r\n     <a href="/homepage/login.logout"><h3>Logout</h3></a>\r\n    <div class="btn-group" style="margin-right: 10px; margin-top: 20px">\r\n      <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" aria-expanded="false">\r\n')
        if request.user.is_authenticated():
            __M_writer('            ')
            __M_writer(str( request.user.first_name +' '+ request.user.last_name ))
            __M_writer('\r\n')
        else:
            __M_writer('            ')
            __M_writer(str( "Not Signed In" ))
            __M_writer('\r\n')
        __M_writer('      <span class="caret"></span>\r\n  </button>\r\n    <ul class="dropdown-menu" role="menu">\r\n')
        if request.user.is_authenticated():
            __M_writer('            <li><a href="/homepage/EditAccount/')
            __M_writer(str( request.user.id ))
            __M_writer('/')
            __M_writer(str( request.user.address_id ))
            __M_writer('">Edit Account</a></li>\r\n            <li><a href="/homepage/login.logout/">Sign Out</a></li>\r\n')
        else:
            __M_writer('            <li><a href id="show_login_dialog" data-toggle="modal" data-target="#login_dialog">Sign In</a></li>\r\n')
        __M_writer('    </ul>\r\n    <a href="/homepage/overdue_rental/" ><p>Daily Batch Process</p></a>\r\n  </div>\r\n    </header>\r\n    -->\r\n    <header class="top">\r\n    <nav class="navbar navbar-default">\r\n        <div class="container-fluid">\r\n            <!-- Brand and toggle get grouped for better mobile display -->\r\n            <div class="navbar-header">\r\n                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"\r\n                        data-target="#bs-example-navbar-collapse-1">\r\n                    <span class="sr-only">Toggle navigation</span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                </button>\r\n                <a class="navbar-brand" href="/homepage/">Colonial Heritage Foundation</a>\r\n            </div>\r\n\r\n            <!-- Collect the nav links, forms, and other content for toggling -->\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                <ul class="nav navbar-nav">\r\n                    <li class="dropdown" id="test1">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">\r\n                            Rental System<span class="caret"></span></a>\r\n                        <ul class="dropdown-menu" role="menu">\r\n                            <li><a href="/homepage/rental/">Rentals</a></li>\r\n                            <li class="divider"></li>\r\n                            <li><a href="/homepage/item/">Items</a></li>\r\n                            <li class="divider"></li>\r\n                            <li><a href="/homepage/overdue_rental/">Overdue Items</a></li>\r\n                        </ul>\r\n                    </li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">\r\n                            Order System<span class="caret"></span></a>\r\n                        <ul class="dropdown-menu" role="menu">\r\n                            <li><a href="/homepage/order/">Orders</a></li>\r\n                            <li class="divider"></li>\r\n                            <li><a href="/homepage/product/">Products</a></li>\r\n                        </ul>\r\n                    </li>\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">\r\n                            Event System<span class="caret"></span></a>\r\n                        <ul class="dropdown-menu" role="menu">\r\n                            <li><a href="/homepage/event/">Events</a></li>\r\n                            <li class="divider"></li>\r\n                            <li><a href="/homepage/area/">Areas</a></li>\r\n                            <li class="divider"></li>\r\n                            <li><a href="/homepage/venue/">Venues</a></li>\r\n                        </ul>\r\n                    </li>\r\n                    <li><a href="/homepage/user/">Users</a></li>\r\n                </ul>\r\n                <ul class="nav navbar-nav navbar-right">\r\n                    <li class="dropdown">\r\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">\r\n')
        if request.user.is_authenticated():
            __M_writer('                                ')
            __M_writer(str( request.user.first_name +' '+ request.user.last_name ))
            __M_writer('\r\n                                <span class="caret"></span></a>\r\n                                    <ul class = "dropdown-menu" role="menu">\r\n                                        <li><a href="/homepage/login.logout">Sign Out</a></li>\r\n                                    </ul>\r\n')
        else:
            __M_writer('                                ')
            __M_writer(str( "Not Signed In" ))
            __M_writer('\r\n                                <span class="caret"></span></a>\r\n                                    <ul class="dropdown-menu" role="menu">\r\n                                        <li><a href id="show_login_dialog" data-toggle="modal" data-target="#login_dialog">Sign In</a></li>\r\n                                    </ul>\r\n')
        __M_writer('                    </li>\r\n                </ul>\r\n            </div>\r\n            <!-- /.navbar-collapse -->\r\n        </div>\r\n        <!-- /.container-fluid -->\r\n    </nav>\r\n</header>\r\n    <div id="header">\r\n      <h1>Colonial Heritage Foundation</h1>\r\n    </div>\r\n      <br>\r\n    <p class="bg-info loggedin">\r\n    Current User: \r\n')
        if request.user.is_authenticated():
            __M_writer('        ')
            __M_writer(str( request.user.first_name +' '+ request.user.last_name ))
            __M_writer('\r\n')
        __M_writer('    </p>\r\n\r\n    <div class="">\r\n      \r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'centerContent'):
            context['self'].centerContent(**pageargs)
        

        __M_writer(' \r\n    </div>\r\n\r\n  <br>\r\n  <div class="row" id="footer">\r\n    <div class="col-md-6">\r\n    \r\n    <p>Colonial Heritage Foundation:</p>\r\n      <ul>\r\n        <li><a href="/homepage/index">Home</a></li>\r\n        <li><a href="/homepage/user">Users</a></li>\r\n        <li><a href="/homepage/item">Items</a></li>\r\n        <li><a href="/homepage/rental">Rentals</a></li>\r\n        <li><a href="/homepage/order">Orders</a></li>\r\n        <li><a href="/homepage/event">Events</a></li>\r\n        <li><a href="/homepage/product">Products</a></li>\r\n        <li></li>\r\n        <li><a href="/homepage/login.logout">Logout</a></li>\r\n     </ul>\r\n    </div>\r\n    <div class="col-md-6">\r\n    <p>Contact information:</p>\r\n      <p>Mailing address:</p>\r\n      <p>Colonial Heritage Foundation</p>\r\n      <p>1617 N Freedom Blvd Suite 9, Provo, UT 84602</p>\r\n\r\n      <p>Telephone:</p>\r\n      <p>801-422-4636 or</p>\r\n      <p>801-422-1211</p>\r\n\r\n\r\n    </div>\r\n  </div>\r\n\r\n  <!-- Modal -->\r\n  <div class="modal fade" id="shoppingCart" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n    <div class="modal-dialog">\r\n      <div class="modal-content">\r\n        <div class="modal-header">\r\n          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n          <h4 class="modal-title" id="myModalLabel">Shopping Cart</h4>\r\n        </div>\r\n        <div class="modal-body">\r\n         \r\n        </div>\r\n        <div class="modal-footer">\r\n          <button type="button" class="btn btn-default" data-dismiss="modal">Continue Shopping</button>\r\n          <button id="checkout_btn" type="button" class="btn btn-primary">Checkout</button>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_centerContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def centerContent():
            return render_centerContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Site content goes here in sub-templates.\r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "base.htm", "filename": "C:\\Users\\Steven\\test_dmp\\homepage\\templates/base.htm", "line_map": {"16": 5, "18": 0, "28": 2, "29": 4, "30": 5, "31": 7, "35": 7, "36": 20, "37": 26, "38": 26, "39": 26, "40": 46, "41": 46, "42": 47, "43": 47, "44": 63, "45": 64, "46": 64, "47": 64, "48": 65, "49": 66, "50": 66, "51": 66, "52": 68, "53": 71, "54": 72, "55": 72, "56": 72, "57": 72, "58": 72, "59": 74, "60": 75, "61": 77, "62": 136, "63": 137, "64": 137, "65": 137, "66": 142, "67": 143, "68": 143, "69": 143, "70": 149, "71": 163, "72": 164, "73": 164, "74": 164, "75": 166, "80": 172, "81": 227, "82": 227, "83": 227, "89": 170, "95": 170, "101": 95}}
__M_END_METADATA
"""
