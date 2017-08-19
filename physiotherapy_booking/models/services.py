# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import UserError, ValidationError


class PhysioServices(models.Model):
    _name = 'physio.service'
    _description = 'Physio Service'

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")
    time_taken = fields.Float(string="Time Taken", help="Approximate time taken for this service in Hours")
    product_id = fields.Many2one('product.product', string="Service Product", domain="[('type','=','service')]")
    service_ids = fields.Many2many('product.product', string="Services List", domain="[('type','=','service')]")


