from modelo.persona import Persona

class Turno:
    def __init__(self, persona: Persona, numero: int):
        self._persona: Persona = persona
        self._numero: int = numero

    @property
    def persona(self):
        return self._persona

    @property
    def numero(self):
        return self._numero

    def __str__(self):
        return f"Turno #{self._numero:02d} : {self._persona}"

