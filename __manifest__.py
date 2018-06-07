# -*- encoding: utf-8 -*-
###############################################################################
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Egas - www.egas.com.mx
#    All Rights Reserved.
###############Credits######################################################
#    Coded by: Edgar Gustavo gustavo.hernandez@smartqs.com
#    Planified by: Edgar Gustavo
#    Finance by: Egas.
#    Audited by: Edgar Gustavo
############################################################################
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
{
    'name': "Point of Sale 0.2",

    'summary': """Se agregan los servicios gasolineros""",

    'description': """
        Esto es solo un modulo de pruebas (DESCRIPCION)
    """,

    'author': "Edgar Gustavo",
    'website': "http://www.egasPrueba.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # Poner los XML a cargar
    'data': [
        #'templates.xml',
        #'views/personas.xml',
        #'views/ciudades.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'active':False,
    'installable': True,
}