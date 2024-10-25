import unittest
from sensors.motion_sensor import MotionSensor

class TestMotionSensor(unittest.TestCase):
    
    def setUp(self):
        self.sensor = MotionSensor()
    
    def test_detect_motion(self):
        # Simula la detección de movimiento
        self.sensor.simulate_motion_detection(True)  # Asegúrate de tener un método para simular detección
        self.assertTrue(self.sensor.detect_motion())
    
    def test_no_motion(self):
        # Simula la ausencia de movimiento
        self.sensor.simulate_motion_detection(False)
        self.assertFalse(self.sensor.detect_motion())

if __name__ == '__main__':
    unittest.main()
