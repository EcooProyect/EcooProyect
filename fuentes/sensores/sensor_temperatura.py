import random
import logging

class TemperatureSensor:
   
    def __init__(self):
        self.current_temperature = 20  # Temperatura inicial

    def read_temperature(self):
        return self.current_temperature

    def set_temperature(self, temperature):
        self.current_temperature = temperature  # Establece la temperatura
