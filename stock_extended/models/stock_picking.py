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
        self.write({'printed': True})
        return self.env.ref('stock.action_report_delivery').report_action(self)







