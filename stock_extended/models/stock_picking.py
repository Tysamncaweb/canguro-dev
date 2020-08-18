# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _ 

_logger = logging.getLogger('__name__')



class StockPicking(models.Model):
    _inherit = 'stock.picking'


    weight = fields.Float(string='weight')
    security_bag = fields.Boolean(string='Security Bag')
    insurance = fields.Boolean(string='Insurance')
    parcel_service = fields.Char(string='Parcel service')

    # @api.depends('origin')
    # def _unit_price(self):
    #     unit_price = self.env['sale.order'].search()