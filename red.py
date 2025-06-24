class RedSocial:
    def __init__(self, nombre):
        self._nombre = nombre
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)

    def listar_usuarios(self):
        print(f"Usuarios en {self._nombre}:")
        for u in self._usuarios:
            print(f"- {u._nombre}")
