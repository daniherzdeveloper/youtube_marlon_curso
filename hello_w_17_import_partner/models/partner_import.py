from odoo import api, fields, models,_
import os
import tempfile
import csv
from odoo.exceptions import UserError
import base64
import xlrd

class PartnerImport(models.Model):
    _name = 'partner.import'
    _description = 'Partner Import'

    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('csv', 'Csv'), ('xls', 'Excel')], string='Type', required=True)
    file = fields.Binary(string='File', required=True)
    file_name = fields.Char(string='File Name', required=True)
    imported = fields.Boolean(string='Imported', default=False, copy=False)

    def action_import(self):
        if self.type == 'csv':
            self.import_csv()
        else:
            self.import_xls()
        self.imported = True
        return True

    @api.model
    def validate_extension_file(self, filename, allowed_extensions):
        name, ext = os.path.splitext(filename)
        return ext in allowed_extensions

    def import_csv(self):
        if not self.validate_extension_file(self.file_name, ['.csv']):
            raise UserError(_("File should be CSV extension"))
        
        file_path = tempfile.gettempdir() + '/file.csv'
        data = self.file
        f = open(file_path, 'wb')
        f.write(base64.b64decode(data))
        f.close()

        archive = csv.DictReader(open(file_path))
        PartnerObj = self.env['res.partner']

        for line in archive:
            partner_name = line.get('Name')
            partner_phone = line.get('Phone')
            partner_email = line.get('Email')
            PartnerObj.create({
                'name': partner_name,
                'phone': partner_phone,
                'email': partner_email,
            })

    def import_xls(self):
        if not self.validate_extension_file(self.file_name, ['.xls', '.xlsx']):
            raise UserError(_("File should be Excel extension"))

        PartnerObj = self.env['res.partner']
        data = base64.b64decode(self.file)
        work_book = xlrd.open_workbook(file_contents=data)
        sheet = work_book.sheet_by_index(0)
        first_row = []

        for col in range(sheet.ncols):
            first_row.append(sheet.cell_value(0, col))

        cont = 0
        for count, row in enumerate(range(1, sheet.nrows), 2):
            try:
                val = {}
                cont += 1
                for col in range(sheet.ncols):
                    val[first_row[col]] = sheet.cell_value(row, col)
                name = val.get('Name', '')
                phone = val.get('Phone', '')
                email = val.get('Email', '')
                PartnerObj.create({
                    'name': name,
                    'phone': phone,
                    'email': email,
                })
            except Exception as e:
                raise UserError(_("There is an error in line %s: %s" % (cont, str(e))))

 