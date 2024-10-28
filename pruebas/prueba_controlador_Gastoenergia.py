import unittest
from fuentes.controladores.power_controller import PowerController  # Actualiza la ruta aquí

class TestControladorDeEnergia(unittest.TestCase):
    
    def setUp(self):
        self.controlador = PowerController()  # Inicializa el controlador de energía
    
    def test_gestionar_uso_de_energia(self):
        # Simula una gestión de energía
        self.controlador.set_power_state(True)  # Activa el estado de energía
        self.assertTrue(self.controlador.get_power_state())  # Verifica que el estado sea verdadero
        self.controlador.set_power_state(False)  # Desactiva el estado de energía
        self.assertFalse(self.controlador.get_power_state())  # Verifica que el estado sea falso

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas

