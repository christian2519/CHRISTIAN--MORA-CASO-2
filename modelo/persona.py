class Persona:
    def __init__(self, nombre: str, documento: str):
        self._nombre: str = nombre
        self._documento: str = documento

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    def __str__(self):
        return f"{self._nombre} (Doc: {self._documento})"

