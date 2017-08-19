# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import UserError, ValidationError


class PatientTreatment(models.Model):
    _name = 'patient.treatment'
    _description = 'Patient Treatment'

    name 	= fields.Char(string="Treatment No.", default=lambda s: s._default_name())
    time_taken 	= fields.Float(string="Time Taken", help="Approximate time taken for this service in Hours")
    service_ids = fields.Many2many('product.product', string="Services List", domain="[('type','=','service')]")
    doctor_id 	= fields.Many2one('res.partner', string="Therapist",domain=[('is_doctor','=',True)])
    patient_id 	= fields.Many2one('res.partner', string="Patient",domain=[('is_patient','=',True)])
    date 	= fields.Date(string="Date")
    user_id 	= fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user)
    services = fields.Many2many('physio.service', string="Services")

    weight 	= fields.Char(string='Weight(Kg.)')
    bmi 	= fields.Char(string='BMI')
    bp 		= fields.Char(string='Pressure')
    pulse 	= fields.Char(string='Pulse(BMP)')
    temp 	= fields.Char(string='Temp. (F*)')
    notes	= fields.Text(string="Notes")


    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code('patient.treatment')


class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'

    treatment_ids = fields.One2many(comodel_name='patient.treatment', inverse_name='patient_id',string='Treatments')


