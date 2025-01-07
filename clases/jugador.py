import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel

    def recibir_dano(self, dano):
        self.salud -= dano
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto, Game Over !!")

    def ganar_experiencia(self, experiencia):
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia")
        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido de nivel  a {self.nivel}")
