#-*- coding: utf-8 -*-

from openerp import models, fields, api
from num2words import num2words

class invoice_extend(models.Model):
    _inherit = 'account.invoice'

    date_day = fields.Datetime('Fecha cita')
    ccss_ref = fields.Char('Número receta')
    total_amount_text=fields.Char('Total en letras', compute="_amount_total_to_text")

    @api.depends('amount_total')
    def _amount_total_to_text(self):
        self.total_amount_text= num2words(int(self.amount_total), lang='es')

