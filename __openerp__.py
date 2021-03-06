# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
#   @author Guewen Baconnier, Bessi Nicolas, Vincent Renaville
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Invoice POS reports',
 'version': '1.1.4',
 'category': 'Reports/Webkit',
 'description': """
Modulo de reporte de factura para pos, mas un comprobante adicional.

 https://launchpad.net/webkit-utils
 """,
 'author': "Adrian Cordoba",
 'website': 'http://www.camptocamp.com',
 'license': 'AGPL-3',
 'depends': ['base', 'account'],
 'external_dependencies': {
        'python' : ['num2words'],
},
 'data': [
        'views/account_invoice_form_inherited.xml',
        'views/res_partner_form_inherited.xml',
        'report/report_invoice_pos.xml',
        'report/report_invoice_full_page.xml',
        'report/report_date_pos.xml'],
 'demo_xml': [],
 'test': []
 }
