# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(size=25)
    relative_id = fields.Many2one(
        string='Contact',
        comodel_name='res.partner',
    )
    alias = fields.Char(
        string='Alias',
        size=256,
        help='Common name the partner is referred to as',
    )
    activation_date = fields.Date(
        string='Activation Date',
        help='Date the partner was activated',
    )
    ref = fields.Char(
        size=256,
        string='ID/SSN',
        help='Patient Social Security Number or equivalent',
    )
    is_doctor = fields.Boolean(
        string='Health Doctor',
        help='Check if the partner is a health professional',
    )
    is_patient = fields.Boolean(
        string='Patient',
        help='Check if the partner is a patient',
    )
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection(
        [
            ('m', 'Male'),
            ('f', 'Female'),
        ],
    )
    marital_status = fields.Selection(
        [
            ('s', 'Single'),
            ('m', 'Married'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('x', 'Separated'),
            ('z', 'law marriage'),
        ],
        string='Marital Status',
    )
    blood_group = fields.Selection(
        [
            ('ap', 'A+'),
            ('bp', 'B+'),
            ('op', 'O+'),
            ('abp','AB+'),
            ('an', 'A-'),
            ('bn', 'B-'),
            ('on', 'O-'),
            ('abn','AB-'),
        ],
        string='Blood Group',
    )


