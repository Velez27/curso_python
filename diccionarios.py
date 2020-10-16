def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424,
    }

    # print(poblacion_paises['Argentina'])

    for pais in poblacion_paises.keys():
        print(pais)

    for poblacion in poblacion_paises.values():
        print(poblacion)

    for pais_nombre, pais_poblacion in poblacion_paises.items():
        print(pais_nombre + ' tiene ' + str(pais_poblacion) + ' habitantes')

if __name__ == '__main__':
    run()