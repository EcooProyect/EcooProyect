from utils.logger import setup_logger
from sensors.temperature_sensor import TemperatureSensor
from sensors.motion_sensor import MotionSensor
from controllers.power_controller import PowerController
from controllers.safety_controller import SafetyController

# Configura el logger
logger = setup_logger('EnergySaver', 'energy_saver.log')

def run_main():
    """Función principal para ejecutar la aplicación."""
    logger.info("Iniciando el proyecto Energy Saver...")

    # Inicializa los sensores
    temperature_sensor = TemperatureSensor()
    motion_sensor = MotionSensor()

    # Inicializa los controladores   
    
    power_controller = PowerController()
    safety_controller = SafetyController()

    # Lógica de funcionamiento (Ejemplo)
    while True:
        # Leer la temperatura
        temperature = temperature_sensor.read_temperature()
        logger.info(f"Temperatura actual: {temperature}°C")

        # Detectar movimiento
        if motion_sensor.detect_motion():
            logger.info("Movimiento detectado.")
            # Implementa la lógica para manejar el movimiento detectado
            safety_controller.activate_safety_protocols()
        
        # Control de energía (Ejemplo)
        power_controller.manage_power_usage()

        # Puedes agregar un tiempo de espera o condición para salir del bucle

if __name__ == "__main__":
    run_main()
