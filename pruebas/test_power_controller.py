import unittest
from src.controllers.power_controller import PowerController

class TestPowerController(unittest.TestCase):
    
    def setUp(self):
        self.controller = PowerController()
    
    def test_manage_power_usage(self):
        # Simula una gestión de energía
        self.controller.set_power_state(True)
        self.assertTrue(self.controller.get_power_state())
        self.controller.set_power_state(False)
        self.assertFalse(self.controller.get_power_state())

if __name__ == '__main__':
    unittest.main()
