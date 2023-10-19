from odoo import models, fields, api

class EjPet(models.Model):
    _inherit = 'ej.pet'

    fur = fields.Char('fur', size=20, default='Blue')
    to_walk = fields.Boolean('To walk')
    date_b = fields.Date('Fecha', default=fields.Date.today)

    is_pretty_name = fields.Boolean('Is Pretty Name', compute='_compute_is_pretty_name')
    is_not_pretty_name = fields.Boolean('is_not_pretty_name', compute='_compute_not_pretty_name', store=True)

    mydb = fields.Char(default=lambda self: self.env.cr.dbname, string='db')

    @api.depends('pretty_name', 'fur')
    def _compute_is_pretty_name(self):
        for record in self:
            record.is_pretty_name = record.pretty_name or record.fur.lower() == 'blue'

    @api.depends('pretty_name')
    def _compute_not_pretty_name(self):
        for record in self:
            record.is_not_pretty_name = not record.pretty_name

    
    