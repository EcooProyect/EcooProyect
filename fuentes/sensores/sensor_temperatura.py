import random
import logging

class sensorTemperatura:
   
    def __init__(self):
        self.current_temperature = 20  # Temperatura inicial

    def read_temperature(self):
        return self.current_temperature

    def set_temperature(self, temperatura):
        self.current_temperature = temperatura  # Establece la temperatura
