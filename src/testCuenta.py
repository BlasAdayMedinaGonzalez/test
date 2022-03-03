from cuenta import *
import unittest

class testCuenta(unittest.TestCase):
    def test_getSaldo(self):
        cuenta = Cuenta()
        self.assertEqual(0, cuenta.getSaldo())
    def test_ingreso(self):
        cuenta = Cuenta()
        cuenta.ingreso(12)
        self.assertEqual(12, cuenta.getSaldo())
    def test_validarCantidadIngresadaPositivos(self):
        cuenta = Cuenta()
        self.assertFalse(cuenta.validarCantidadIngresada(-12))
    def test_validarCantidadIngresadaNegativos(self):
        cuenta = Cuenta()
        self.assertTrue(cuenta.validarCantidadIngresada(12))
    def test_validarCantidadRetiradaNegativos(self):
        cuenta = Cuenta()
        self.assertFalse(cuenta.validarCantidadRetirada(-2))
    


if __name__ == '__main__':
    unittest.main()