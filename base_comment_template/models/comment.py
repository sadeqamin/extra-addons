# -*- coding: utf-8 -*-
# Copyright 2014 Guewen Baconnier (Camptocamp SA)
# Copyright 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api
from odoo.exceptions import UserError


class BaseCommentTemplate(models.Model):
    _name = "base.comment.template"
    _description = "Base comment template"

    name = fields.Char('Comment summary', required=True)
    position = fields.Selection([('before_lines', 'Before lines'),
                                 ('after_lines', 'After lines')],
                                'Position',
                                required=True,
                                default='before_lines',
                                help="Position on document")
    text = fields.Html('Comment', translate=True, required=True)
    # add jija expression
    model_id = fields.Many2one('ir.model', 'Applies to', help="The type of document this template can be used with")
    model = fields.Char('Related Document Model', related='model_id.model', index=True, store=True, readonly=True)
    model_object_field = fields.Many2one('ir.model.fields', string="Field",
                                         help="Select target field from the related document model.\n"
                                              "If it is a relationship field you will be able to select "
                                              "a target field at the destination of the relationship.")
    sub_object = fields.Many2one('ir.model', 'Sub-model', readonly=True,
                                 help="When a relationship field is selected as first field, "
                                      "this field shows the document model the relationship goes to.")
    sub_model_object_field = fields.Many2one('ir.model.fields', 'Sub-field',
                                             help="When a relationship field is selected as first field, "
                                                  "this field lets you select the target field within the "
                                                  "destination document model (sub-model).")
    null_value = fields.Char('Default Value', help="Optional value to use if the target field is empty")
    copyvalue = fields.Char('Placeholder Expression', help="Final placeholder expression, to be copy-pasted in the desired template field.")
    
    @api.onchange('model_id')
    def onchange_model_id(self):
        # TDE CLEANME: should'nt it be a stored related ?
        if self.model_id:
            self.model = self.model_id.model
        else:
            self.model = False

    def build_expression(self, field_name, sub_field_name, null_value):
        """Returns a placeholder expression for use in a template field,
        based on the values provided in the placeholder assistant.

        :param field_name: main field name
        :param sub_field_name: sub field name (M2O)
        :param null_value: default value if the target value is empty
        :return: final placeholder expression """
        expression = ''
        if field_name:
            expression = "${object." + field_name
            if sub_field_name:
                expression += "." + sub_field_name
            if null_value:
                expression += " or '''%s'''" % null_value
            expression += "}"
        return expression

    @api.onchange('model_object_field', 'sub_model_object_field', 'null_value')
    def onchange_sub_model_object_value_field(self):
        if self.model_object_field:
            if self.model_object_field.ttype in ['many2one', 'one2many', 'many2many']:
                models = self.env['ir.model'].search([('model', '=', self.model_object_field.relation)])
                if models:
                    self.sub_object = models.id
                    self.copyvalue = self.build_expression(self.model_object_field.name, self.sub_model_object_field and self.sub_model_object_field.name or False, self.null_value or False)
            else:
                self.sub_object = False
                self.sub_model_object_field = False
                self.copyvalue = self.build_expression(self.model_object_field.name, False, self.null_value or False)
        else:
            self.sub_object = False
            self.copyvalue = False
            self.sub_model_object_field = False
            self.null_value = False

    @api.multi
    def get_value(self, partner_id=False):
        self.ensure_one()
        lang = None
        if partner_id:
            lang = self.env['res.partner'].browse(partner_id).lang
        return self.with_context({'lang': lang}).text

    @api.multi
    @api.depends('model', 'text')
    def render_html(self):
        if self.text:
            rendered_note = self.env['mail.template'].render_template(self.text, self.model, [self.id])
            for key, value in rendered_note.items():
                return(str(value))
           
class BaseCommentTemplate(models.Model):
    _inherit = ["multi.company.abstract", "base.comment.template"]
    _name = "base.comment.template"
    _description = "Base Comments Template (Multi-Company)"
