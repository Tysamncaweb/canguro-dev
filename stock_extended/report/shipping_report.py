# -*- coding:utf-8 -+-

import logging

from odoo import api, models

_logger = logging.getLogger('__name__')



class StockShippingReport(models.AbstractModel):
    _name = 'report.stock_extended.template_shipping_report'
    

    def _shipping_report(self, docids):
        records = self.env['stock.picking'].browse(docids)
        _logger.info("\n\n\n\n records %s \n\n", records)
        return [{
            'name': records, 
            # 'name': "Alejandro", 
            'LastName': "Sanchez",
        }]



    @api.model
    def _get_report_values(self, docids, data=None):
        _logger.info("\n\n\n\n YES IS HERE!!!!!!! =)\n\n\n\n")
        var = data.get('form')
        _logger.info("\n\n\n var %s \n\n\n", var)
        report_name = 'stock_extended.template_shipping_report'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        docs = self.env[report.model].browse(docids),
        _logger.info("\n\n\n report %s\n\n\n", report)
        _logger.info("\n\n\n report.model %s\n\n\n", report.model)
        _logger.info("\n\n\n doc_ids %s\n\n\n", docids)

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
            'shipping_report': self._shipping_report,
        }
        return docargs






