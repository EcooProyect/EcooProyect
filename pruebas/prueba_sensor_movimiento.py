import unittest
from pruebas.prueba_sensor_movimiento import SensorMovimiento

class TestSensorMovimiento(unittest.TestCase):
    
    def setUp(self):
        self.sensor = SensorMovimiento()
    
    def test_detectar_movimiento(self):
        # Simula la detección de movimiento
        self.sensor.simular_deteccion_movimiento(True)  # Asegúrate de tener un método para simular detección
        self.assertTrue(self.sensor.detectar_movimiento())
    
    def test_no_hay_movimiento(self):
        # Simula la ausencia de movimiento
        self.sensor.simular_deteccion_movimiento(False)
        self.assertFalse(self.sensor.detectar_movimiento())

if __name__ == '__main__':
    unittest.main()

