import utils


def menu():
    print(f"""
        #####################################################
        # BIENVENIDO A LOS JUEGOS INFANTILES DE MATEMATICAS #
        #####################################################
        
        ¿Cual es el nombre del participante?
        """)
    participante = str(input(''))
    nuevo_jugador = utils.Juegos_infantiles(participante)
    if len(participante) > 0:
        funciones = {
            1: nuevo_jugador.juego,
            2: nuevo_jugador.mostrar_ranking,
            3: nuevo_jugador.vaciar_ranking,
            4: nuevo_jugador.agregar_preguntas
        }
        while True:
            print(f"""
                  ####################
                  # MENU DE OPCIONES #
                  ####################
                  
            1) Jugar una ronda
            2) Ver ranking de jugadores
            3) Vaciar ranking (accion irreversible)
            4) Agregar preguntas al banco de preguntas
            5) Salir
            """)
            opcion = int(input())
            if opcion == 4:
                pregunta = str(input('Cual es la pregunta que desea agregar: '))
                a = str(input('¿Cual es la opcion A?'))
                b = str(input('¿Cual es la opcion B?'))
                c = str(input('¿Cual es la opcion C?'))
                respuesta = str(input('¿Cual letra es la opcion correcta?'))
                funciones[4](pregunta, a, b, c, respuesta)
                break
            elif opcion == 5:
                break
            elif opcion <= 3:
                funciones[opcion]()
                break
            else:
                print("La opcion no se encuentra dentro del menu, escoja una opcion correcta")
    else:
        print("El nombre del jugador estar vacio")
    print("¿Desea seguir jugando?  (Si/No)")
    r = str(input("")).lower()
    if r == "si":
        menu()
    else:
        print("Gracias por haber jugado nuestro juego")
    return None


if __name__ == '__main__':
    menu()
