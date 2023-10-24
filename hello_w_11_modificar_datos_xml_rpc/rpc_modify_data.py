import xmlrpc.client
import csv

host = '127.0.0.1'
port = 8069
db = 'desoft'
user = 'admin'
password = 'admin'

url = 'http://%s:%d/xmlrpc/2/' % (host, port)

common_proxy = xmlrpc.client.ServerProxy(url + 'common')
object_proxy = xmlrpc.client.ServerProxy(url + 'object')
uid = common_proxy.login(db, user, password)
if uid:
    print('Conectado al servidor maestro')

def _create(state):
    print("=1=")
    print(state)
    if state is True:
        archive = csv.DictReader(open('D:\\Intall\\install\\desoft\\odoo-16.0\\custom\\addons\\youtube_marlon_curso\\hello_w_11_modificar_datos_xml_rpc\\data.csv'))
        cont = 0
        for field in archive:
            cont += 1
            _name = field['name'].strip()
            _list_price = field['list_price'].strip()
            # _phone = field['phone'].strip()

            vals = {}
            vals['name'] = _name
            vals['list_price'] = _list_price
            # vals['phone'] = _phone
            # vals['active'] = True
            print(vals)

            # Validate the register does not exist
            _id = object_proxy.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', _name]]])
            if _id:
                new_product = object_proxy.execute(db, uid, password, 'product.template', 'write', _id, vals)
                if new_product:
                    print("Se ha modificado el registro: ")
                else:
                    print("No se ha modificado el registro: ")
            
        cont += 1
        print("Se han modificado: ", cont)


def main():
    print("Ha comenzado el proceso")
    _create(True)
    print('Ha finalizado la carga tabla')
main()