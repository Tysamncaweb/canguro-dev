# -*- coding: utf-8 -*-

import logging

from odoo import fields, api, models, _

_logger = logging.getLogger('__name__')


class Product(models.Model):
    _inherit = 'product.template'


    tracking = fields.Selection([
        ('serial', 'By Unique Serial Number/ IMEI Number'),
        ('lot', 'By Lots'),
        ('none', 'No Tracking')], 
        string="Tracking", 
        help="Ensure the traceability of a storable product in your warehouse.", 
        default='none', required=True)


    @api.onchange('tracking')
    def onchange_tracking(self):
        return self.mapped('product_variant_ids').onchange_tracking()


    def action_open_product_imei(self):
        self.ensure_one()
        action = self.env.ref('imei_fields.action_product_imei_view').read()[0]
        action['domain'] = [('product_id', '=', self.id)]
        action['context'] = {'default_product_id': self.id}
        return action




class ProductProduct(models.Model):
    _inherit = 'product.product'


    @api.onchange('tracking')
    def onchange_tracking(self):
        products = self.filtered(lambda self: self.tracking and self.tracking != 'none')
        if products:
            unassigned_quants = self.env['stock.quant'].search_count([('product_id', 'in', products.ids), ('lot_id', '=', False), ('location_id.usage','=', 'internal')])
            if unassigned_quants:
                return {
                    'warning': {
                        'title': _('Warning!'),
                        'message': _("You have products in stock that have no lot number.  You can assign serial numbers or IMEI code by doing an inventory. ")}}






#class ImeiNumber(models.Model):
#    _name = 'imei.number'
#    _description = 'IMEI'
#
#
#    name = fields.Char(string='IMEI', help='IMEI code')
#    active = fields.Boolean(string='Active', default=True)
#    sold = fields.Boolean(string='Sold', readonly=True, store=True)
#    product_id = fields.Many2one('product.product' ,string='Products')
#    ref = fields.Char(string='Code')
#    company_id = fields.Many2one(string='Company')