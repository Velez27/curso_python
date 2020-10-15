def run():
    nombre = input('Escribe tu nombre: ')
    palabra_final = ''
    for letra in nombre :
        palabra_final += letra.upper()
        
    print(palabra_final)

    # frase = input('Escribe una frase: ')
    # for caracter in frase:
    #     print(caracter.upper())


if __name__ == '__main__':
    run()