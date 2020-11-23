# -*- coding:utf-8 -*-


from odoo import api, fields, models, _




class ProductTemplate(models.Model):
    _inherit='product.template'

    #default_code = fields

    _sql_constraints = [
            ('default_code_uniq', 'unique (default_code)', 'Remember the code it\'s unique by each product')
            ]
