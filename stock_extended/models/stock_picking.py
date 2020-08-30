# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError 

_logger = logging.getLogger('__name__')



class StockPicking(models.Model):
    _inherit = 'stock.picking'


    security_bag = fields.Boolean(string='Security Bag')
    insurance = fields.Boolean(string='Insurance')


    @api.constrains('note')
    def _note_limited(self):
        if self.note:
            if len(self.note) > 89:
                raise ValidationError(_("Field note cannot be contain more than 89 characters.!"))
        else:
            pass


    def do_print_picking(self):
        _logger.info("\n\n Aqui estoy\n\n\n")
        self.write({'printed': True})
        _logger.info("\n\n self %s \n\n", self)
        return self.env.ref('stock.action_report_delivery').report_action(self)


class StockShippingReport(models.Model):
    _name = "stock.shipping.report"


    name = fields.Char(string="Name")
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    report = fields.Binary(string="Shipping Report")
    ir_attachment = fields.Many2one('ir.attachment', string="Attached")
    binary_name = fields.Char(string="File name")

    @api.onchange('binary_name')
    def _put_name(self):
        if self.binary_name:
            self.name = self.binary_name
        else:
            self.name = "/"




