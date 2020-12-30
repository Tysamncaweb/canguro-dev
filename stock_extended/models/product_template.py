# -*- coding:utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError




class ProductTemplate(models.Model):
    _inherit='product.template'

    #@api.constrains('default_code')
    def unique_code(self):
        if not self.default_code:
            raise ValidationError(_("The default code cannot be blank"))

    _sql_constraints = [
            ('default_code_uniq', 'unique (default_code)', 'Remember the code it\'s unique by each product')
            ]
