#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C)2010-  OpenERP SA (<http://openerp.com>). All Rights Reserved
#    oszckar@gmail.com
#
#    Developed by Oscar Alcala <oszckar@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Reporte Sobre Desperdicios con Salidas de Almacen",
    "version" : "0.1",
    "depends" : ["base"],
    "author" : "Juan Alejandro VR",
    "description" : """
        Este modulo crea incidencias sobre desperdicios y tmb crea salidas a otro sistema
                    """,
    "website" : "http://casasalce.com",
    "category" : "Tools",
    "init_xml" : [
    ],
    "demo_xml" : [
    ],
    "update_xml" : [
        "garbage_view.xml",
    ],
    "active": False,
    "installable": True,
}
