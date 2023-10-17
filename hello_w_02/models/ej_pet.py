from odoo import models, fields, api

class EjPet(models.Model):
    _inherit = 'ej.pet'

    fur = fields.Char('fur', size=20, default='Blue')
    to_walk = fields.Boolean('To walk')
    