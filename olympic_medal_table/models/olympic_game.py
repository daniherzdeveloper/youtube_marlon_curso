from odoo import models, fields, api

class OmtOlympicGame(models.Model):
    _name = 'omt.olympic.game'
    _description = 'omt.olympic.game'

    name = fields.Char('name')
    