# Clase UsusarioBanco con atributos nombre,saldo, cuenta_corriente(True,False)
class UsuarioBanco:
    """
    Clase que representa a un usuario de un banco.
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Constructor de la clase UsusarioBanco.
        Args:
            nombre (str): nombre del usuario.
            saldo (float): saldo actual del usuario.
            cuenta_corriente (bool): indica si tiene o no cuenta corriente.
        """
        # Creamos atributos y asignamos el valor de los parámetros del método constructor
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente


    # 2. Método retirar_dinero.
    def retirar_dinero(self, retiro):
        """
        Comprobar que el usuario tenga saldo suficiente para realizar el retiro.
        Args:
            retiro (float): monto a retirar
        """
        if self.saldo <= 0 or self.saldo<retiro:
            print("No tiene suficiente saldo para realizar el retiro")
        else:
            self.saldo -= retiro
            print("Retiro realizado con exito")

    # 3. Método transferir dinero desde otro usuario al usuario actual
    def transferencia(self, otro_usuario, monto):
        """
        Transferir dinero desde otro usuario al usuario actual.
        Args:
            otro_usuario (UsuarioBanco): usuario del cual se va a transferir el dinero.
            monto (float): monto a transferir.
        """
        if otro_usuario.saldo < monto:
            print("No tiene suficiente saldo para realizar la transferencia")
        else:
           self.saldo += monto
           otro_usuario.saldo -= monto
           print("Transferencia realizada con exito")
    # 4.  Método agregar dinero
    def agregar_dinero(self, deposito):
        """
        Deposito de dinero en la cuenta del usuario.
        Args:
            deposito (float): monto a depositar
        """
        self.saldo += deposito
        print("Deposito realizado con exito")

    # 5. Método  info_usuario para devolver información sobre la cuenta del usuario
    def info_usuario(self):
        """
        Devuelve información sobre la información del usuario.
        Returns:
            str: información del usuario.
        """
        info = f"Nombre: {self.nombre}\n"
        info += f"Saldo: {self.saldo}\n"
        info += f"Tipo de cuenta: {self.cuenta_corriente} \n"
        return info

# 1. Inicializar un usuario

usuario1=UsuarioBanco("Alicia",100,True)
usuario2=UsuarioBanco("Bob",50,True)
print(usuario1.info_usuario())
print(usuario2.info_usuario())

# Llamado de cada metodo de la clase segun el orden solicitado
usuario2.agregar_dinero(20)
print(usuario1.info_usuario())
print(usuario2.info_usuario())

usuario1.retirar_dinero(50)
print(usuario1.info_usuario())
print(usuario2.info_usuario())

usuario1.transferencia(usuario2,80)
print(usuario1.info_usuario())
print(usuario2.info_usuario())

usuario1.retirar_dinero(50)
print(usuario1.info_usuario())
print(usuario2.info_usuario())

print(usuario1.info_usuario())





