# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'product.template.wizard'
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('mobile.manufacturer', 'Manufacturer')
    model_id = fields.Many2one('mobile.model', 'Model')

    @api.one
    @api.depends('manufacturer_id', 'model_id')
    def _createname(self):
        manufacturer = str(self.manufacturer_id.name)
        model = str(self.model_id.name)
        self.name = manufacturer + ' ' + model

    name = fields.Char(string='Name', compute='_createname', readonly=True)

    state = fields.Selection(
        selection=[
            ('step1', 'Step 1'),
            ('step2', 'Step 2'),
        ],
        string="Current step",
        default="step1",
        readonly=True
    )

    @api.multi
    def action_step1(self):
        self.state = 'step1'
        return {"type": "set_scrollTop"}

    @api.multi
    def action_step2(self):
        self.state = 'step2'
        return {"type": "set_scrollTop"}
