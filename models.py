#-*- coding: utf-8 -*-
from openerp import models, fields, api

class Account(models.Model):
    _inherit = 'account.invoice'

    date_day = fields.Date('Fecha de cita')
    ccss_ref = fields.Char('Número de referencia')