# -*- coding: utf-8 -*-
# WR Ltd https://wrltd.ca

{
    'name': 'Account Financial Report',
    'version': '10.0',
    'category': 'Accounting',
    'author': 'WR Ltd',
    'summary': 'Copy account report id to journal items',
    'depends': [
        'account', 'account_financial_report_qweb',
    ],
    'description': """
    Copy account report id to journal items
    """,
    'data': [
    'views/account_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
    
