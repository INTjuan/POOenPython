from red import RedSocial
from usuario import Usuario
from admin import Admin

def main():
    red = RedSocial("RedEjemplo")

    u1 = Usuario("Juan", "juan@mail.com")
    u2 = Usuario("Nestor", "nestor@mail.com")
    admin = Admin("Admin", "admin@red.com")

    red.agregar_usuario(u1)
    red.agregar_usuario(u2)
    red.agregar_usuario(admin)

    red.listar_usuarios()

    u1.enviar_mensaje(u2, "Hola Nestor!")
    u2.enviar_mensaje(u1, "¡Hola Juan! ¿Cómo estás?")
    u1.mostrar_mensajes()
    u2.mostrar_mensajes()

    admin.eliminar_usuario(red, u2)
    red.listar_usuarios()
