# -*- coding: utf-8 -*-
from odoo import http

# class Models(http.Controller):
#     @http.route('/models/models/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/models/models/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('models.listing', {
#             'root': '/models/models',
#             'objects': http.request.env['models.models'].search([]),
#         })

#     @http.route('/models/models/objects/<model("models.models"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('models.object', {
#             'object': obj
#         })