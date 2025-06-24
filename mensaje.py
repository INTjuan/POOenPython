class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self._remitente = remitente
        self._destinatario = destinatario
        self._contenido = contenido

    def __str__(self):
        return f"De: {self._remitente._nombre}, Mensaje: {self._contenido}"
