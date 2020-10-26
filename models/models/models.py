# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mobile_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    # manufacturer_id = fields.Many2one('mobile.manufacturer', 'Manufacturer')
    model_id = fields.Many2one('mobile.model', 'Model')


class Mobile_model(models.Model):
    _name = 'mobile.model'

    manufacturer_id = fields.Many2one('mobile.manufacturer', 'Manufacturer', required=True)
    name = fields.Char('Model Name')
