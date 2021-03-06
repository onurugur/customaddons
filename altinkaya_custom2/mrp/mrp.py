# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013-Present Acespritech Solutions Pvt. Ltd. (<http://acespritech.com>).
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
from openerp.osv import osv, fields
from openerp.tools.translate import _


class mrp_production(osv.osv):

    #_name = 'mrp.production'
    _inherit = 'mrp.production'

    _columns = {
      'date_planned': fields.datetime('Scheduled Date'),
      'date_start2': fields.datetime('Start Date',),
      'date_finished2': fields.datetime('End Date',),
      'priority': fields.selection([('0','Not urgent'),('1','Normal'),('2','Urgent'),('3','Very Urgent')], 'Priority',
            select=True),
      }

mrp_production()