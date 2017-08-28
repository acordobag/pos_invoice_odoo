#-*- coding: utf-8 -*-

from openerp import models, fields, api

class invoice_extend(models.Model):
    _inherit = 'account.invoice'

    date_day = fields.Datetime('Fecha cita')
    ccss_ref = fields.Char('Número receta')
