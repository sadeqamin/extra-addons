# -*- coding: utf-8 -*-
# Copyright 2020 WR Ltd - adhoc cloud services (https://cloud.wrltd.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.addons.cmis_field import fields


class CrmClaimFolder(models.Model):
    _inherit = "crm.claim"

    cmis_folder = fields.CmisFolder()



