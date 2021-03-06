# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    odoo_edi_token = fields.Char(string='Token', help='Define the token that is used for login to FlexEDI')
    gln = fields.Char(string='GLN number', help='GLN identification number of the company. This can also be called the EAN identifier/number')
    edi_mode = fields.Selection(string="EDI Operation mode", help="Choose how we handle EDI connections. Option 'Production' for running against a production environment and sending real documents to real customers. Option 'Test' is to send documents to the testing environment where data is processed but not actually sent. Option 'Development/Debug' is used when we do not want to contact a server, which results in the file just being dumped locally on the server",
                                selection=[('production', 'Production'), ('test', 'Test'), ('development', 'Development/Debugging')])
    
