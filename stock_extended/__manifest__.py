# -*- coding:utf-8 -*-


{
        'name': 'Stock Picking Extended',
        'version': '0.1',
        'author': 'Tysamnca',
        'depends': [
            'stock',
            ],
        'data': [
            'security/ir.model.access.csv',
            'report/report_deliveryslip.xml',
            'report/internal_transfer_report_view.xml',
            'report/shipping_report.xml',
            'views/stock_picking_views.xml',
            'views/shipping_report_views.xml',
            ],
        'installable': True,
}
