class Usuario:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        self._mensajes_recibidos = []

    def enviar_mensaje(self, destinatario, contenido):
        from mensaje import Mensaje
        mensaje = Mensaje(self, destinatario, contenido)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self._mensajes_recibidos.append(mensaje)

    def mostrar_mensajes(self):
        print(f"Mensajes para {self._nombre}:")
        for msg in self._mensajes_recibidos:
            print(msg)
