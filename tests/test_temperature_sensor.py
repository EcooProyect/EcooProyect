import unittest
from src.sensors.temperature_sensor import TemperatureSensor

class TestTemperatureSensor(unittest.TestCase):
    
    def setUp(self):
        self.sensor = TemperatureSensor()
        
    def test_temperature_within_range(self):
        self.sensor.set_temperature(25)
        self.assertEqual(self.sensor.read_temperature(), 25)

    
    def test_temperature_below_range(self):
        self.sensor.set_temperature(15)
        self.assertEqual(self.sensor.read_temperature(), 15)

if __name__ == '__main__':
    unittest.main()
