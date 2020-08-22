# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError 

_logger = logging.getLogger('__name__')



class StockPicking(models.Model):
    _inherit = 'stock.picking'


    weight = fields.Float(string='weight')
    security_bag = fields.Boolean(string='Security Bag')
    insurance = fields.Boolean(string='Insurance')
    parcel_service = fields.Char(string='Parcel service')
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")


    @api.constrains('note')
    def _note_limited(self):
        if self.note:
            if len(self.note) > 89:
                raise ValidationError(_("Field note cannot be contain more than 89 characters.!"))
        else:
            pass



class StockShippingReport(models.Model):
    _name = "stock.shipping.report"


    name = fields.Char(string="Name")
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    report = fields.Binary(string="Shipping Report")




