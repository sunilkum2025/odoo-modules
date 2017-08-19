# -*- coding: utf-8 -*-

import datetime
from lxml import etree
import math
import pytz
import threading
import urlparse

import openerp
from openerp import tools, api, SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.osv.expression import get_unaccent_wrapper
from openerp.tools.translate import _
from openerp.exceptions import UserError


class patient_history(osv.Model):
    _name = "patient.history"
    _description = "Patient History"
    _columns = {
        'name': fields.char('Summary', required=True, select=True),
        'description': fields.text('Description'),
        'history_date': fields.datetime('Date'),
        'partner_id': fields.many2one('res.partner', 'Related Partner'),
        'employee_id': fields.many2one('hr.employee', 'Therapist'),
    	'doctor_id': fields.many2one('res.partner', string="Therapist",domain=[('is_doctor','=',True)]),
        'user_id': fields.many2one('res.users', 'User'),
    }

class res_partner(osv.Model):
    _description = 'Partner'
    _inherit = "res.partner"
    _columns = {
        'history_ids': fields.one2many('patient.history', 'partner_id', 'History'),
    }

