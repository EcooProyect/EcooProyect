import logging
from fuentes.sensores.sensor_movimiento import sensorMovimiento  # Asegúrate de que el nombre de la clase y la ruta sean correctos

class ControladorSeguridad:
    def __init__(self, temperature_threshold=75.0):
        self.temperature_threshold = temperature_threshold
        self.sensor = sensorMovimiento()  # Asegúrate de que esta clase está definida en el módulo correcto

    def check_temperature(self):
        current_temp = self.sensor.read_temperature()  # Asegúrate de que este método esté implementado en la clase SensorMovimiento
        logging.info(f"Temperatura actual: {current_temp:.2f}°C")

        if current_temp > self.temperature_threshold:
            self.trigger_alarm()
            return False
        return True

    def trigger_alarm(self):
        logging.warning("¡La temperatura excede el umbral! Activando alarma.")
        # Aquí puedes añadir código para realizar acciones de seguridad

class ControladorSeguridadProtocolos:
    def activate_safety_protocols(self):
        # Lógica para activar protocolos de seguridad
        self.safety_activated = True  # Asigna a un atributo si es necesario
        logging.info("Protocolos de seguridad activados.")

# Ejemplo de uso
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Configura el logging para mostrar mensajes
    safety_controller = ControladorSeguridad()
    
    if not safety_controller.check_temperature():
        safety_controller.trigger_alarm()  # Llama a la alarma si la temperatura es alta
        print("¡Protocolo de seguridad activado!")
