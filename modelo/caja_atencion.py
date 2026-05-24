from typing import List, Optional
from modelo.persona import Persona
from modelo.turno import Turno

class CajaAtencion:
    def __init__(self):
        self._cola_turnos: List[Turno] = []
        self._consecutivo: int = 0

    def agregar_persona(self, persona: Persona):
        self._consecutivo += 1
        nuevo_turno = Turno(persona, self._consecutivo)
        self._cola_turnos.append(nuevo_turno)
        return nuevo_turno

    def atender_siguiente(self):
        if self.esta_vacia():
            return None
        return self._cola_turnos.pop(0)

    def esta_vacia(self):
        return len(self._cola_turnos) == 0

    def proximo_turno(self):
        if self.esta_vacia():
            return None
        return self._cola_turnos[0]

