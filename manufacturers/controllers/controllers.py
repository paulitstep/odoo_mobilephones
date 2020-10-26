# -*- coding: utf-8 -*-
from odoo import http

# class Manufacturers(http.Controller):
#     @http.route('/manufacturers/manufacturers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturers/manufacturers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturers.listing', {
#             'root': '/manufacturers/manufacturers',
#             'objects': http.request.env['manufacturers.manufacturers'].search([]),
#         })

#     @http.route('/manufacturers/manufacturers/objects/<model("manufacturers.manufacturers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturers.object', {
#             'object': obj
#         })