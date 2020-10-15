def run():
    LIMITE = 1
    contador = 0
    while contador < LIMITE:
        respuesta = input('Este era un gato con los pies de trapo y los ojos al revéz. Quieres que te lo cuente otra vez?: ')
        if respuesta == 'break':
            break


if __name__ == '__main__':
    run()