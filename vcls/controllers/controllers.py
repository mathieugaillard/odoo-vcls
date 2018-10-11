# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/vcls/benefit/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/vcls/benefit/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('benefit.listing', {
            'root': '/vcls/benefit',
            'objects': http.request.env['vcls.benefit'].search([]),
        })

    @http.route('/vcls/benefit/objects/<model("vcls.benefit"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('benefit.object', {
            'object': obj
        })