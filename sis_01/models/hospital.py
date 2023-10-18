from odoo import models, fields, api

class Hospital(models.Model):
    _name = 'sis.hospital'
    _description = 'Hospital'

    name = fields.Char(string='Hospital Name', required=True, size=50)
    country_id = fields.Many2one('res.country', string='Country')

    