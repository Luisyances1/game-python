import random
import json


class Juegos_infantiles():
    def __init__(self, jugador: str):
        self.jugador = jugador

    def leer_textos_json(self, archivo: str) -> dict:
        try:
            with open(f'{archivo}.json', 'r', encoding='utf-8') as archivo_json:
                datos = json.load(archivo_json)
        except FileNotFoundError as error:
            print(f'Error: {error}')
            return {}
        except json.decoder.JSONDecodeError as error:
            print(f'Error: {error}')
            return {}
        return datos

    def guardar_ranking(self, diccionario, nombre_archivo):
        with open(f'{nombre_archivo}.json', 'w') as archivo:
            json.dump(diccionario, archivo)
        return None

    def juego(self, cantidad_preguntas=3):
        preguntas = self.leer_textos_json('banco_preguntas')
        limite = len(preguntas.keys())
        respuesta = ''
        puntos = 0
        conteo = 1
        while True:
            if conteo <= cantidad_preguntas:
                numero_aleatorio = random.randint(1, limite)
                print(f"""
                    {preguntas[str(numero_aleatorio)]['pregunta']}
                    A) {preguntas[str(numero_aleatorio)]['opciones']['a']}
                    B) {preguntas[str(numero_aleatorio)]['opciones']['b']}
                    C) {preguntas[str(numero_aleatorio)]['opciones']['c']}
                    """)
                respuesta = input('¿Cual es su respuesta?: ').lower()
                if len(respuesta) == 0:
                    print(f"Omitir una pregunta no genera puntos, puntos actuales {puntos}")
                    puntos += 0
                elif respuesta == preguntas[str(numero_aleatorio)]['respuesta_correcta']:
                    print(f"Muy bien, su respuesta fue correcta, ¡ANIMO! se le suman 5 puntos a su acumulado")
                    puntos += 5
                else:
                    print("(U_U) Respuesta incorrecta, Pero animo")
                    puntos += 2
                conteo += 1
            else:
                break
        print(f"""
        Juego terminado:
        Jugador: {self.jugador}
        Puntos: {puntos}
        """)
        ranking = self.leer_textos_json('ranking')
        ranking[f'Juego-{len(ranking.keys())+1}'] = {'nombre': self.jugador,
                                                     'puntos': puntos}
        self.guardar_ranking(ranking, 'ranking')
        return None

    def mostrar_ranking(self):
        ranking = self.leer_textos_json('ranking')
        ranking = dict(sorted(ranking.items(), key=lambda x: x[1]['puntos'], reverse=True))
        if len(ranking.keys()) <= 10:
            for puesto, jugador in enumerate(ranking.values()):
                print(f"""
                {puesto+1}) - {jugador['nombre']} - {jugador['puntos']}
                """)
        else:
            for puesto, jugador in enumerate(ranking.values()):
                if puesto < 10:
                    print(f"""
                    {puesto+1}) - {jugador['nombre']} - {jugador['puntos']}
                    """)
        return None

    def vaciar_ranking(self):
        ranking = self.leer_textos_json('ranking')
        ranking.clear()
        self.guardar_ranking(ranking, 'ranking')
        return None

    def agregar_preguntas(self, pregunta: str, opcion_a: str,
                          opcion_b: str, opcion_c: str, respuesta: str):
        preguntas = self.leer_textos_json('banco_preguntas')
        id_pregunta = len(preguntas.keys())
        if '¿' not in pregunta:
            pregunta = f'¿{pregunta}'
        if '?' not in pregunta:
            pregunta = f'{pregunta}?'
        else:
            pass
        while True:
            print(f"""
            ¿Esta es la pregunta que desea ingresar?
            {pregunta}
            A) {opcion_a}
            B) {opcion_b}
            C) {opcion_c}
            (Si/No)
            """)
            confirmacion = str(input('')).lower()
            if confirmacion == 'si':
                try:
                    preguntas[f'{id_pregunta+1}'] = {'pregunta': pregunta,
                                                  'opciones':{'a': opcion_a,
                                                              'b': opcion_b,
                                                              'c': opcion_c},
                                                  'respuesta': respuesta.lower()}
                    print("¡¡¡Se agrego correctamente la pregunta!!!")
                    break
                except Exception as e:
                    print(f"Ocurrio un error {e}")
                    break
            elif confirmacion == 'no':
                print('Corrija su pregunta y escoja nuevamente la opcion de agregar pregunta, gracias')
                break
            else:
                print('Digite solo si o no')
        self.guardar_ranking(preguntas, 'banco_preguntas')
        return None