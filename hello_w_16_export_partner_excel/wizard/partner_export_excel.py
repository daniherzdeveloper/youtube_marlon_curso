from odoo import fields, models, api, _
import base64
from io import BytesIO
from odoo.tools.misc import xlwt
from odoo.exceptions import UserError
from werkzeug.urls import url_encode

class PartnerExportExcel(models.TransientModel):
    _name = "partner.export.excel"
    _description = "Export Partner Excel"

    country_id = fields.Many2one('res.country', string='Country')

    def export_partner_excel(self):
        domain = []
        if self.country_id:
            domain.append(('country_id', '=', self.country_id.id))
        partners = self.env['res.partner'].search(domain)

        if not partners:
            raise UserError(_("There are no partners who belong to this country."))

        return self._helper_export_partner_excel(partners)


    def _helper_export_partner_excel(self, partners):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet(_("Partners"))
        file_name = _("Partners")

        style_border_table_top = xlwt.easyxf(
            'borders: left thin, right thin, top thin, bottom thin; font: bold on;')
        style_border_table_details = xlwt.easyxf('borders: bottom thin;')
        style_border_table_details_red = xlwt.easyxf('borders: bottom thin; font: colour red, bold True;')

        worksheet.write(0, 0, _("Name"), style_border_table_top)
        worksheet.write(0, 1, _("Country"), style_border_table_top)
        worksheet.write(0, 2, _("Email"), style_border_table_top)

        row = 1
        for partner in partners:
            worksheet.write(row, 0, partner.name, style_border_table_details)
            worksheet.write(row, 1, partner.country_id.name if partner.country_id else '', style_border_table_details)
            worksheet.write(row, 2, partner.email or '', style_border_table_details)
            row += 1

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        data_b64 = base64.encodebytes(data)
        doc = self.env['ir.attachment'].create({
            'name': '%s.xls' % (file_name),
            'datas': data_b64,
        })

        query_params = {
            'model': 'ir.attachment',
            'id': doc.id,
            'filename_field': 'name',
            'field': 'datas',
            'download': True,
            'filename': doc.name,
        }

        url = '/web/content?' + url_encode(query_params)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }

