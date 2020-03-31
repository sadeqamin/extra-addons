# -*- coding: utf-8 -*-
# Copyright 2020 WR Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Report Id',
    'description': """
        Copy report id to account move line""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'WR Ltd',
    'website': 'https://wrltd.ca',
    'depends': [
        'account'
    ],
    'data': [
        'views/account_financial_report.xml',
    ],
    'demo': [
    ],
}
