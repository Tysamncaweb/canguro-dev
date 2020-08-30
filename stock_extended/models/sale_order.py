# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError 

_logger = logging.getLogger('__name__')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one('payment.acquirer',string="Payment method")
