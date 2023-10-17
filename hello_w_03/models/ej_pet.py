from odoo import models, fields, api

class EjPet(models.Model):
    _inherit = 'ej.pet'

    fur = fields.Char('fur', size=20, default='Blue')
    to_walk = fields.Boolean('To walk')
    date_b = fields.Date('Fecha', default=fields.Date.today)

    is_pretty_name = fields.Boolean('Is Pretty Name', compute='_compute_is_pretty_name')

    @api.depends('fur')
    def _compute_is_pretty_name(self):
        for record in self:
            record.is_pretty_name = record.fur == 'Blue'

    
    