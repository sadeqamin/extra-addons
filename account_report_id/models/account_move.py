# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountMove(models.Model):
  _inherit = "account.move.line"
  
  @api.one
  @api.depends('user_type_id')
  def _get_account_report_id(self):
      for line in self:
          reports = self.env['account.financial.report'].search([('parent_id', '=', False)])
          for report in reports:
              child_reports = report._get_children_by_order()
              if child_reports:
                  for child_report in child_reports:
                      is_acount_type = child_report.search([('id', '=', child_report.id), ('type', '=$
                      if is_acount_type:
                          if line.user_type_id in child_report.account_type_ids:
                              line.account_report_id = child_report
                                                                                          
  
  account_report_id = fields.Many2one('account.financial.report', compute='_get_account_report_id', string="Account Report", store=True, readonly=False)  

                                                                                           
