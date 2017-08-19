# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 ICTSTUDIO (<http://www.ictstudio.eu>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, tools, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class PatientTreatImages(models.Model):
    _name = "patient.treatment.image"

    image = fields.Binary(string="Image")
    sequence = fields.Char(string="Seq")
    name = fields.Char(string="Name")
    default = fields.Boolean(string="Main Product Image")
    treatment_id = fields.Many2one(comodel_name='patient.treatment',string='Treatment')


class PatientTreatment(models.Model):
    _inherit = 'patient.treatment'
    _description = 'Patient Treatment'

    image_ids = fields.One2many(comodel_name='patient.treatment.image', inverse_name='treatment_id',string='Images')




