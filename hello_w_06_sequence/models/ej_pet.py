from odoo import models, fields, api

class EjPet(models.Model):
    _name = 'ej.pet'
    _description = 'ej.pet'

    name = fields.Char('name', required=True)
    age = fields.Char('age', required=True)
    color = fields.Char('color', required=True)
    is_new = fields.Boolean('is_new', default=True)
    code = fields.Char('code', default='New', readonly=1)

    pretty_name = fields.Boolean('Pretty Name')

    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    ], string='type', default='dog', required=True)

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code('ej.pet') or "New"
        pet = super(EjPet, self).create(vals)
        return pet
    