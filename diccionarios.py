# nombre_diccionario {
#   llave: valor
#   key: value
#   propiedad: valor 
# }

# paises = {
#     "honduras": "tegucigalpa",
#     "nicaragua": "managua",
#     "costa rica": "san jose",
#     "el salvador": "san salvador",
#     "guatemala": "guatemala",
#     "estados unidos": "washington"
# }

# Ver llaves (keys)
# for pais in paises.keys():
    # print(pais)

# Ver capitales (values)
#for capital in paises.values():
#    print(capital)

# Ver paises y capitales
#for pais, capital in paises.items():
#    print("La capital de " + pais + " es " + capital)

# try:
#     ingresoPais = str(input("Escriba el nombre de un pais: ")).lower()
#     print("La capital de {} es {}".format(ingresoPais, paises[ingresoPais]))
#     #print("La capital de " + ingresoPais + " es " + paises[ingresoPais])
# except KeyError:
#     #print("No hay datos para {}".format(ingresoPais))
#     print("No hay datos para " + ingresoPais)

# Script en el que a partir de un diccionario tenga la poblacion de 10 municipios de honduras
# Pedir al usuario que busque la poblacion por municipio

municipios = {
    "Morazan": 50000,
    "Villanueva": 120989,
    "Santa Cruz de Yojoa": 5000,
    "San Pedro Sula": 1200000,
    "Potrerillos": 34500,
    "Pimienta": 156789,
    "San Manuel": 23800,
    "La Esperanza": 130567,
    "El Progreso": 130456,
    "San Francisco de Yojoa": 23500
}

try:
    municipios2 = input("Ingrese municipio: ")
    print("La poblacion de {} tiene {} habitantes.".format(municipios2, format(municipios[municipios2], ",d")))
except KeyError:
    print("El municipio no existe.")