# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Physio Therapy Booking System',
    'version' : '1.1',
    'category' : 'Website',
    'website' : 'http://www.openerp.com',
    'description': """
Module for resource management.
===============================

A resource represent something that can be scheduled the employee based one time slots. This module manages a resource calendar
associated to every resource. It also manages the leaves of every emoloyee.
    """,
    'depends': ['base','hr','product','board'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/partner_view.xml',
	'views/menu_view.xml',
	'views/clinic_patient_view.xml',
	'views/physio_view.xml',
	'views/consultant_view.xml',
	'views/clinic_services.xml',
	'views/clinic_treatment.xml',
	'report/report_physio_booking_view.xml',
	'views/dashboard_view.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
