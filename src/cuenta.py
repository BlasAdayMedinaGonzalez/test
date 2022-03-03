class Cuenta:
    saldo = None

    def __init__(self):
        self.saldo = 0

    def getSaldo(self):
        """Función que retorna saldo 
        >>> self.getSaldo()
        0
        """
        return self.saldo

    def ingreso(self, cantidad):
        """Función que guarda en la variable saldo la cantidad del ingreso
        >>> self.ingreso(12)
        12
        """
        esValida = self.validarCantidadIngresada(cantidad)
        if esValida:
            self.saldo += cantidad

    def validarCantidadIngresada(self, cantidad):
        """Función que valida la cantidad ingresada.
        >>> validarCantidadIngresada(-23)
        False
        >>> validarCantidadIngresada(23)
        True
        >>> validarCantidadIngresada(7000)
        False
        """
        if round(cantidad, 2) != cantidad:
            return False

        if cantidad < 0:
            return False

        if cantidad > 6000.0:
            return False
        
        return True

    def retirada(self, cantidad):
        """Función que quita una cantidad de retirada al saldo"""
        esValida = self.validarCantidadRetirada(cantidad)
        if esValida:
            self.saldo -= cantidad

    def validarCantidadRetirada(self, cantidad):
        """Función que valida cantidad retirada"""
        if round(cantidad, 2) != cantidad:
            return False

        if cantidad < 0:
            return False

        if cantidad > self.saldo:
            return False

        if cantidad > 6000.0:
            return False

        return True

    def transferencia(self, cuenta_destino, cantidad):
        esValida = self.validarCantidadTransferencia(cantidad)
        if esValida:
            self.retirada(cantidad)
            cuenta_destino.ingreso(cantidad)

    def validarCantidadTransferencia(self, cantidad):
        if cantidad < 0:
            return False

        if cantidad > self.saldo:
            return False

        if cantidad > 3000:
            return False

        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()