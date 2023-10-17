from odoo import models, fields, api

class EjPet(models.Model):
    _name = 'ej.pet'
    _description = 'ej.pet'

    name = fields.Char('name', required=True)
    age = fields.Char('age', required=True)
    color = fields.Char('color', required=True)
    is_new = fields.Boolean('is_new', default=True)

    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    ], string='type', default='dog', required=True)
    