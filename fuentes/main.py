from utilidades.logger import setup_logger
from sensores.sensor_temperatura import sensorTemperatura
from sensores.sensor_movimiento import sensorMovimiento
from controladores.controladorEnergia import controladorEnergia
from controladores.controladorSeguridad import ControladorSeguridad

# Configura el logger
logger = setup_logger('EnergySaver', 'energy_saver.log')

def run_main():
    """Función principal para ejecutar la aplicación."""
    logger.info("Iniciando el proyecto Energy Saver...")

    # Inicializa los sensores
    temperature_sensor = sensorTemperatura()
    motion_sensor = sensorMovimiento()

    # Inicializa los controladores   
    
    power_controller = controladorEnergia()
    safety_controller = ControladorSeguridad()

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
