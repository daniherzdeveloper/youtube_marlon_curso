from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    has_vat = fields.Boolean(string="Has VAT", compute='_compute_has_vat', store=True)

    def _compute_has_vat(self):
        for partner in self:
            partner.has_vat = bool(partner.vat)
