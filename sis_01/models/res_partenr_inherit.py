from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    rut = fields.Char('rut', size=10)
    age = fields.Integer('age')
    profession = fields.Char('profession', size=50)
    