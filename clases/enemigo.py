import random


class Enemigo:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano

    def atacar(self):
        return random.randint(5, 15)

    def recibir_dano(self, dano):
        if self.salud <= dano:
            self.salud = 0
            print(f"Has derrotado a {self.nombre}")
            return True
        return False
