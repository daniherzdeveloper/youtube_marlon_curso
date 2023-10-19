from odoo import models, fields, api

class Athletes(models.Model):
    _name = 'omt.athletes'
    _description = 'athletes'

    name = fields.Char('name', required=True)
    country_id = fields.Many2one('res.country', string='Country')
    gold = fields.Integer('gold')
    silver = fields.Integer('silver')
    bronze = fields.Integer('bronze')
    active = fields.Boolean('active', default=True)

    olympic_game_id = fields.Many2one('omt.olympic.game', string='Olympic Game')
    
    