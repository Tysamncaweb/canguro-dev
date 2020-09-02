# -*- coding:utf-8 -*-

import logging

from odoo import api, models, fields


_logger = logging.getLogger('__name__')




class StockShippingReportWizard(models.TransientModel):
    _name = "stock.shipping.report.wizard"


    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    

    def shipping_report(self):
        _logger.info("\n\n Aqui estoy\n\n\n")
        _logger.info("\n\n self %s \n\n", self)
        return self.env.ref('stock_extended.action_shipping_report').report_action(self)