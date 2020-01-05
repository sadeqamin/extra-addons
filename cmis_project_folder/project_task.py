# -*- coding: utf-8 -*-
# Copyright 2020 WR Ltd - adhoc cloud services (https://cloud.wrltd.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import httplib2
import functools

from odoo import _, api, fields, models
from odoo.addons.cmis_field import fields


class Project(models.Model):
	_inherit = "project.project"

	cmis_folder = fields.CmisFolder()

    httplib2.Http = functools.partial(
        httplib2.Http,
        ca_certs=""
    )


class ProjectTaskFolder(models.Model):
    _inherit = "project.task"

    cmis_folder = fields.CmisFolder(related='project_id.cmis_folder')

    httplib2.Http = functools.partial(
        httplib2.Http,
        ca_certs=""
    )


