import logging

class PowerController:
    def __init__(self):
        self.power_state = False  # Estado inicial

    def set_power_state(self, state):
        self.power_state = state

    def get_power_state(self):
        return self.power_state  # Retorna el 
