import logging
from src.sensors.temperature_sensor import TemperatureSensor

class SafetyController:
    def __init__(self, temperature_threshold=75.0):
        self.temperature_threshold = temperature_threshold
        self.sensor = TemperatureSensor()

    def check_temperature(self):
        current_temp = self.sensor.read_temperature()
        logging.info(f"Current temperature: {current_temp:.2f}°C")

        if current_temp > self.temperature_threshold:
            self.trigger_alarm()
            return False
        return True

    def trigger_alarm(self):
        logging.warning("Temperature exceeds threshold! Triggering alarm.")
        # Aquí puedes añadir código para realizar acciones de seguridad
class SafetyController:
    def activate_safety_protocols(self):
        # Lógica para activar protocolos de seguridad
        pass
    
    def activate_safety_protocols(self):
        self.safety_activated = True 
# Ejemplo de uso
if __name__ == "__main__":
    safety_controller = SafetyController()
    if not safety_controller.check_temperature():
        print("Safety protocol activated!")
