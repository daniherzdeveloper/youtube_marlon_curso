from odoo import models, fields, api

class Consultations(models.Model):
    _name = 'sis.consultations'
    _description = 'Consultations'

    name = fields.Char(string='Consultations Name', required=True, size=50)
    partner_id = fields.Many2one('res.partner', string='Patient', ondelete='restrict')
    specialties_id = fields.Many2one('sis.specialties', string='Specialties', ondelete='restrict')

    