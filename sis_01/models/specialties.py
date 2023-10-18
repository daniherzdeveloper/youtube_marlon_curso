from odoo import models, fields, api

class Specialties(models.Model):
    _name = 'sis.specialties'
    _description = 'Specialties'

    name = fields.Char(string='Specialties Name', required=True, size=50)

    