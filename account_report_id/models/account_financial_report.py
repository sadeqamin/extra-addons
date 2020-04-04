# -*- coding: utf-8 -*-
# Copyright 2020 WR Ltd
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class AccountFinancialReport(models.Model):

    _inherit = 'account.move.line'

    @api.depends('user_type_id')
    def _get_account_report_id(self):
        for line in self:
            reports = self.env['account.financial.report'].search([('parent_id', '=', False)])
            for report in reports:
                child_reports = report._get_children_by_order()
                if child_reports:
                    for child_report in child_reports:
                        is_acount_type = child_report.search([('id', '=', child_report.id), ('type', '=', 'account_type')])
                        if is_acount_type:
                            if line.user_type_id in child_report.account_type_ids:
                                line.account_report_id = child_report

    @api.depends('balance', 'account_report_id.sign')
    def _store_balance_invert(self):
        for line in self:
            report_sign = line.account_report_id.sign
            line.balance_invert = line.balance * -report_sign


    account_report_id = fields.Many2one('account.financial.report', compute='_get_account_report_id', string='Level-2', store=True, readonly=False, help="Main sections in financial reports")
    balance_invert = fields.Monetary(compute='_store_balance_invert', string='Balance(G)', store=True, currency_field='company_currency_id', help="field used to store an inverted value of balance to give some meaningful analysis in Graph views")
    account_report_parent = fields.Many2one('account.financial.report', related='account_report_id.parent_id', store=True, string="Level-1", help="Financial Statement Report")

