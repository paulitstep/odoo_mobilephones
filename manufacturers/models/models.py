# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mobile_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('mobile.manufacturer', 'Manufacturer')


class Mobile_manufacturer(models.Model):
    _name = 'mobile.manufacturer'

    name = fields.Char('Manufacturer Name')
