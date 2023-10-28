import requests
import json

# primer forma de consumir la api
# # URL de la API en el servidor de Odoo
# url = "http://localhost:8069/api/partner/info/ESA64922266/12345"

# # Hacer una solicitud GET a la API
# response = requests.get(url)

# # Verificar si la solicitud fue exitosa (código de estado 200)
# if response.status_code == 200:
#     # Decodificar la respuesta JSON
#     data = response.json()
#     # Manipular los datos como desees
#     print(json.dumps(data, indent=4))
# else:
#     # Si la solicitud no fue exitosa, imprimir el código de estado
#     print("Error al hacer la solicitud. Código de estado:", response.status_code)


# segunda forma de consumir la api
def obtener_info_partner(nif, token):
    url = f"http://localhost:8069/api/partner/info/{nif}/{token}"
    
    try:
        # Hacer una solicitud GET a la API
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Decodificar la respuesta JSON y devolver los datos
            data = response.json()

            return json.dumps(data, indent=4)
        else:
            # Si la solicitud no fue exitosa, imprimir el código de estado
            print("Error al hacer la solicitud. Código de estado:", response.status_code)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None

# Ejemplo de uso de la función
nif = "ESA64922266"
token = "12345"
datos_partner = obtener_info_partner(nif, token)

if datos_partner:
    print(datos_partner)
else:
    print("No se pudieron obtener los datos del partner.")

