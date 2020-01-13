#! /usr/bin/python
# Copyright 2020 WR Ltd - adhoc cloud services (https://cloud.wrltd.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import httplib2
import functools

from odoo import _, api, fields, models
from odoo.addons.cmis_field import fields

class CrmClaim(models.Model):
    _inherit = "crm.claim"

    cmis_folder = fields.CmisFolder()

    # Set system CA Certificates based SSL Certificate Validation by python code
    # httplib2.Http = functools.partial(httplib2.Http, ca_certs="//usr/lib/python2.7/dist-packages/odoo/.local/fullchain.pem")
    # httplib2.Http = functools.partial(httplib2.Http, disable_ssl_certificate_validation=True)

    @api.multi
    def _check_cmis_access_operation(self, operation, field_name=None):
        my_true_condition = False
        my_false_condition = False
        if my_true_condition:
            return 'allow'
        if my_false_condition:
             return 'deny'
        return 'default'

    @api.model
    def create(self, vals):
        res = super(CrmClaim, self).create(vals)
        vals['cmis_folder'] = self.name
        self._fields['cmis_folder'].create_value(res)
        return res
