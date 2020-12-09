# -*- coding: utf-8 -*-

from odoo import fields, api, models, _




class Product(models.Model):
    _inherit = 'product.template'

    tracking = fields.Selection(selection_add=[('imei', 'IMEI')])

