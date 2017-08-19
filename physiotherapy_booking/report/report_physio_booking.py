# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields
from openerp import tools


class report_physio_booking(models.Model):
    """Booking physio Analysis"""
    _name = "report.physio.booking"
    _order = 'booking_date desc'
    _auto = False

    create_date = fields.Datetime('Creation Date', readonly=True)
    booking_date = fields.Datetime('Date', readonly=True)
    doctor_id = fields.Many2one('res.partner', string="Doctor")
    draft_state = fields.Integer(' # No. of Draft Appointment')
    cancel_state = fields.Integer(' # No. of Cancelled Appointment')
    confirm_state = fields.Integer(' # No. of Confirmed Appointment')
    nbbooking = fields.Integer('Number of Booking')
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default="draft")


    def init(self, cr):
        """Initialize the sql view for the booking """
        tools.drop_view_if_exists(cr, 'report_physio_booking')
        # TOFIX this request won't select events that have no registration
        cr.execute(""" CREATE VIEW report_physio_booking AS (
            SELECT
                b.id::varchar || '/' || coalesce(b.id::varchar,'') AS id,
                b.doctor_id AS doctor_id,
                b.date AS create_date,
                b.start_time AS booking_date,
                count(b.id) AS nbbooking,
                CASE WHEN b.state = 'draft' THEN count(b.doctor_id) ELSE 0 END AS draft_state,
                CASE WHEN b.state = 'approved' THEN count(b.doctor_id) ELSE 0 END AS confirm_state,
                CASE WHEN b.state = 'rejected' THEN count(b.doctor_id) ELSE 0 END AS cancel_state,
                b.state AS state 
            FROM
                physio_booking b
            GROUP BY
                b.doctor_id,
                b.id,
                b.state,
                b.date,
                b.start_time 
        )
        """)


class report_today_physio_booking(models.Model):
    """Today Booking Analysis"""
    _name = "report.today.physio.booking"
    _order = 'booking_date desc'
    _auto = False

    create_date = fields.Datetime('Creation Date', readonly=True)
    booking_date = fields.Datetime('Date', readonly=True)
    doctor_id = fields.Many2one('res.partner', string="Doctor")
    confirm_state = fields.Integer(' # No. of Appointment')
    nbbooking = fields.Integer('Number of Appointment')
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default="draft")

    def init(self, cr):
        """Initialize the sql view for the booking """
        tools.drop_view_if_exists(cr, 'report_today_physio_booking')
        # TOFIX this request won't select events that have no registration
        cr.execute(""" CREATE VIEW report_today_physio_booking AS (
            SELECT
                b.id::varchar || '/' || coalesce(b.id::varchar,'') AS id,
                b.doctor_id AS doctor_id,
                b.date AS create_date,
                b.start_time AS booking_date,
                count(b.id) AS nbbooking,
                CASE WHEN b.state = 'approved' THEN count(b.doctor_id) ELSE 0 END AS confirm_state,
                b.state AS state 
            FROM
                physio_booking b 
	    WHERE b.date = now()::date and b.state = 'approved' 
            GROUP BY
                b.doctor_id,
                b.id,
                b.state,
                b.date,
                b.start_time 
        )
        """)

