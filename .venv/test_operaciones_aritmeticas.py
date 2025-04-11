import unittest
from operaciones_aritmeticas import operaciones_aritmeticas as Division

class Test_division(unittest.TestCase):

    def test_dividir_dosNumeros_retornaCociente(self):
        # Arrange
        dividendo = 20
        divisor = 4
        resultadoEsperado = 5

        objDivision = Division(dividendo, divisor)

        # Act
        resultadoActual = objDivision.calcularDivision()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Fallo la división")

    def test_dividir_porCero_lanzaExcepcion(self):
        objDivision = Division(10, 0)
        with self.assertRaises(ZeroDivisionError):
            objDivision.calcularDivision()

    def test_dividir_conOperandoNoNumerico_lanzaExcepcion(self):
        objDivision = Division(10, 'x')
        with self.assertRaises(ValueError):
            objDivision.calcularDivision()

if __name__ == '__main__':
    unittest.main()
