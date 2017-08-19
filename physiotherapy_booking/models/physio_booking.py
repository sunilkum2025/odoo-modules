# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2015-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Avinash Nk(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from datetime import date


class ResPartner(models.Model):
    _inherit = 'res.partner'
    ref = fields.Char('NRIC/WP/FIN No.', size=10,help='Identity Number')

class PhysioBooking(models.Model):
    _name = 'physio.booking'

    name = fields.Char(string="Name")
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default="draft")
    start_time = fields.Datetime(string="Start time", default=date.today(), required=True)
    end_time = fields.Datetime(string="End time")
    date = fields.Date(string="Date", required=True, default=date.today())

    phone = fields.Char(string="Phone")
    email = fields.Char(string="E-Mail")
    dob = fields.Date(string='Date of Birth')
    ref = fields.Char('NRIC/WP/FIN No.', size=10, readonly=True, states={'draft':[('readonly',False)]})
    is_existing = fields.Boolean('Existing Patient?',readonly=True, states={'draft':[('readonly',False)]})
    patient_id = fields.Many2one('res.partner', string="Patient",domain=[('is_patient','=',True)])
    services = fields.Many2many('physio.service', string="Services")
    doctor_id = fields.Many2one('res.partner', string="Therapist",domain=[('is_doctor','=',True)])
    company_id = fields.Many2one('res.company', 'Company',default=lambda self: self.env['res.company'].browse(1))
    lang = fields.Many2one('res.lang', 'Language', default=lambda self: self.env['res.lang'].browse(1))
    user_id = fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user)
    start_date_only = fields.Date(string="Date Only")
    gender = fields.Selection([('m','Male'),('f','Female')])

    @api.multi
    def booking_approve(self):
        patient_obj = self.env['res.partner']
        patient_data ={
            'name': self.name,
            'ref': self.ref,
            'dob': self.dob,
            'phone': self.phone,
            'email': self.email,
            'active': True,
            'is_patient': True,
            'gender': self.gender,
        }
	if not self.patient_id:
	        patient = patient_obj.create(patient_data)
        	print ":::::",patient
        	self.patient_id = patient
        #clinic_order_obj = self.env['clinic.order']
        #clinic_service_obj = self.env['clinic.order.lines']
        #order_data ={
        #    'customer_name': self.name,
        #    'doctor_id': self.doctor_id.id,
        #    'patient_id': self.patient_id.id,
        #    'start_time': self.date,
        #    'date': date.today(),
        #    'stage_id': 1,
        #    'booking_identifier': True,
        #}
        #order = clinic_order_obj.create(order_data)
        #for records in self.services:
        #    service_data = {
        #        'service_id': records.id,
        #        'time_taken': records.time_taken,
        #        'price': records.price,
        #        'price_subtotal': records.price,
        #        'clinic_order': order.id,
        #    }
        #    clinic_service_obj.create(service_data)
        #template = self.env.ref('clinic_management.clinic_email_template_approved')
        #self.env['mail.template'].browse(template.id).send_mail(self.id)
        self.state = "approved"

    @api.multi
    def booking_reject(self):
        #template = self.env.ref('clinic_management.clinic_email_template_rejected')
        #self.env['mail.template'].browse(template.id).send_mail(self.id)
        self.state = "rejected"


    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id:
            self.name = self.patient_id.name
            self.ref = self.patient_id.ref
            self.dob = self.patient_id.dob
            self.phone = self.patient_id.phone
            self.email = self.patient_id.email
            self.gender = self.patient_id.gender



