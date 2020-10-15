menu = """
Bienvenido al conversor de monedas 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion """

opcion = int(input(menu))

def convertir(moneda, valor_dolar):
    pesos = input('Cuantos Pesos ' + moneda + ' tienes?: ')
    pesos = float(pesos)
    dolares  = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')

if opcion == 1:
    convertir('Colombianos', 3875)
elif opcion == 2:
    convertir('Argentinos', 65)
elif opcion == 3:
    convertir('Mexicanos', 24)
else:
    print('Ingresa una opcion correcta por favor')