# -*- coding:utf-8 -+-

import logging

from odoo import api, models

_logger = logging.getLogger('__name__')



class StockShippingReport(models.AbstractModel):
    _name = 'report.stock_extended.template_shipping_report'
    
    def _shipping_report(self, docids, date_from, date_to):
        lis = []
        ids = self.env['stock.picking'].search([('date', '>=', date_from),('date', '<=', date_to)]).ids
        records =  self.env['stock.picking'].browse(ids)
        for item in records:    
            for record in item: 
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
        return lis


    @api.model
    def _get_report_values(self, docids, data):
        
        docids = self.env['stock.picking'].search([])[0].ids

        report_name = 'stock_extended.template_shipping_report'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        #docs = self.env[report.model].browse(docids)

        docargs = {
            'doc_ids': docids,
            'data': data,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
            'shipping_report': self._shipping_report,
        }
        return docargs






