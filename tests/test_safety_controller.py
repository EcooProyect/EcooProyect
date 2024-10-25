import unittest
from src.controllers.safety_controller import SafetyController

class TestSafetyController(unittest.TestCase):
    
    def setUp(self):
        self.controller = SafetyController()
    
    def test_activate_safety_protocols(self):
        # Simula la activación de protocolos de seguridad
        self.controller.activate_safety_protocols()
        self.assertTrue(self.controller.safety_activated)

if __name__ == '__main__':
    unittest.main()
