# -*- encoding: utf-8 -*-
{
    'name': 'Product Documents',
    'version': '0.1',
    'category': 'Sale',
    'author': 'WR Ltd'
    'description': """
Add documents to product, for example datasheet, catalogue or catalogue, you will be able to send product documents with quotation or sales order. 
""",
    'depends': [
        'document',
    ],
    'installable': True,
    'data': [
        'views/website_sale_digital_view.xml',
    ],
    'demo': [
        'data/product_demo.xml',
    ],
}
