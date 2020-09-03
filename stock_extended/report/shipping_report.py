# -*- coding:utf-8 -+-

import logging

from odoo import api, models

_logger = logging.getLogger('__name__')



class StockShippingReport(models.AbstractModel):
    _name = 'report.stock_extended.template_shipping_report'
    

    def _shipping_report(self, docids, date_from, date_to):
        lis = []
        _logger.info("\n\n LLEGO AL REPORTE \n\n")
        ids = self.env['stock.picking'].search([('date', '>=', date_from),('date', '<=', date_to)]).ids
        _logger.info("\n\n ids %s\n\n", ids)
        records =  self.env['stock.picking'].browse(ids)
        _logger.info("\n\n\n\n records %s \n\n", records)
        for item in records:    
            for record in item: 
                _logger.info("\n\n record %s\n\n", record)
                _logger.info("\n\n record.date %s\n\n", record.date)
                lis.append({
                    'date': record.scheduled_date,
                    'adviser': record.user_id.name,
                    'customer': record.partner_id.name,
                    'weight': record.weight,
                    'security_bag': record.security_bag,
                    'insurance': record.insurance,
                    'destinity': record.partner_id.state_id.name,
                    'parcel_service': record.carrier_id.name,
                })
        _logger.info("\n\n lis %s \n\n", lis)
        return lis


    @api.model
    def _get_report_values(self, docids, data):
        _logger.info("\n\n\n\n data %s\n\n\n\n", data)
        
        docids = self.env['stock.picking'].search([])[0].ids
        _logger.info("\n\n docids %s\n\n", docids)

        report_name = 'stock_extended.template_shipping_report'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        docs = self.env[report.model].browse(docids)
        _logger.info("\n\n\n docs %s\n\n\n", docs)
        # _logger.info("\n\n\n report %s\n\n\n", report)
        # _logger.info("\n\n\n report.model %s\n\n\n", report.model)
        # _logger.info("\n\n\n doc_ids %s\n\n\n", docids)

        

        docargs = {
            'doc_ids': docids,
            'data': data,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
            'shipping_report': self._shipping_report,
        }
        return docargs






