import unittest
from pruebas.prueba_sensor_temperatura import SensorTemperatura

class TestSensorTemperatura(unittest.TestCase):
    
    def setUp(self):
        self.sensor = SensorTemperatura()
        
    def test_temperatura_en_rango(self):
        self.sensor.establecer_temperatura(25)
        self.assertEqual(self.sensor.leer_temperatura(), 25)

    def test_temperatura_bajo_rango(self):
        self.sensor.establecer_temperatura(15)
        self.assertEqual(self.sensor.leer_temperatura(), 15)

if __name__ == '__main__':
    unittest.main()
