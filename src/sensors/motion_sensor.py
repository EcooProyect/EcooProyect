import random
import logging

class MotionSensor:
    def __init__(self):
        self.motion_detected = False

    def detect_motion(self):
        return self.motion_detected

    def simulate_motion_detection(self, detected):
        self.motion_detected = detected  # Simula detección de movimiento
