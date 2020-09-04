# -*- coding:utf-8 -*-

import logging

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


_logger = logging.getLogger('__name__')




class StockShippingReportWizard(models.TransientModel):
    _name = "stock.shipping.report.wizard"


    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    

    def shipping_report(self):
        
        _logger.info("\n\n type %s \n\n", type(self.date_from))
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                raise ValidationError(_("The start date cannot be greater than the end date"))
        elif (self.date_from == False) or (self.date_to == False):
            raise ValidationError(_("Fields date cannot be empty."))

        data = {
            'model': 'stock.shipping.report.wizard',
            'form': self.read()[0]
        }
        return self.env.ref('stock_extended.action_shipping_report').report_action(self, data=data)