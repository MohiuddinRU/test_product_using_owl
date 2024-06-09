# -*- coding: utf-8 -*-
# from odoo import http


# class TestProductUsingOwl(http.Controller):
#     @http.route('/test_product_using_owl/test_product_using_owl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_product_using_owl/test_product_using_owl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_product_using_owl.listing', {
#             'root': '/test_product_using_owl/test_product_using_owl',
#             'objects': http.request.env['test_product_using_owl.test_product_using_owl'].search([]),
#         })

#     @http.route('/test_product_using_owl/test_product_using_owl/objects/<model("test_product_using_owl.test_product_using_owl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_product_using_owl.object', {
#             'object': obj
#         })

