# -*- coding: utf-8 -*-
from odoo import http


class TestProductUsingOwl(http.Controller):
    @http.route('/test', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("test_product_using_owl.somePythonTemplate")

    @http.route('/shop/products', type="json", auth="public")
    def shopProducts(self, **kw):
        products = http.request.env['product.template'].sudo().search_read([], ["name", "list_price"])
        return products
