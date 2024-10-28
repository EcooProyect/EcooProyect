import unittest
from fuentes.controladores.controladorSeguridad import controladorEnergia

class TestControladorSeguridad(unittest.TestCase):
    
    def setUp(self):
        self.controlador = controladorEnergia()
    
    def test_activar_protocolos_seguridad(self):
        # Simula la activación de protocolos de seguridad
        self.controlador.activar_protocolos_seguridad()
        self.assertTrue(self.controlador.protocolos_activados)

if __name__ == '__main__':
    unittest.main()

