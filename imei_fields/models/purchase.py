# -*- coding: utf-8 -*-

from odoo import fields, api, models, _




class Purchase(models.Model):
    _name = 'purchase.order'

    imei = fields.Char(string='IMEI')