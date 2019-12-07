# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Recurring Transactions',
    'category': 'Extra Tools',
    'description': """
Create recurring transactions - multi-company aware.
===========================

This module allows to create new documents and add subscriptions on that document.

e.g. To have an invoice generated automatically periodically:
-------------------------------------------------------------
    * Define a document type based on Invoice object
    * Define a subscription whose source document is the document defined as
      above. Specify the interval information and partner to be invoiced.
    """,
    'author': "WR",
    'depends': ['base', 'account', 'hr_expense', 'base_multi_company'],
    'data': [
        'security/subscription_security.xml',
        'security/ir.model.access.csv',
        'views/subscription_view.xml',
        'data/data.xml'
    ],
    'demo': ['data/subscription_demo.xml'],
}
