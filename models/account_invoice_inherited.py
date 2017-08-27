#-*- coding: utf-8 -*-
from openerp import models, fields, api

class Account(models.Model):
    _inherit = 'account.invoice'
    date_day = date_effective = fields.Date('Fecha de cita')
    ccss_ref = name  = fields.Char('Número de referencia',20)