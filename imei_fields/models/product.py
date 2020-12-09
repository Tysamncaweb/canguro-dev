# -*- coding: utf-8 -*-

from odoo import fields, api, models, _




class Product(models.Model):
    _name = 'product'

    imei = fields.Char(string='IMEI')





