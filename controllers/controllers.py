# -*- coding: utf-8 -*-
# from odoo import http


# class GestorFutbol(http.Controller):
#     @http.route('/gestor_futbol/gestor_futbol', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_futbol/gestor_futbol/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_futbol.listing', {
#             'root': '/gestor_futbol/gestor_futbol',
#             'objects': http.request.env['gestor_futbol.gestor_futbol'].search([]),
#         })

#     @http.route('/gestor_futbol/gestor_futbol/objects/<model("gestor_futbol.gestor_futbol"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_futbol.object', {
#             'object': obj
#         })

