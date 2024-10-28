# Guía de Uso

## Descripción General
`EcooProyect` está diseñado para gestionar y monitorear el consumo de energía de dispositivos, asegurando su eficiencia y seguridad. El sistema detecta automáticamente la inactividad y apaga los equipos de manera segura, protegiéndolos del sobrecalentamiento y del desperdicio de energía.

## Ejecución de la Aplicación
1. **Iniciar la Aplicación:**
   - Abre la terminal.
   - Navega al directorio raíz del proyecto.
   - Ejecuta el script principal:
     ```bash
     python src/main.py
     ```

2. **Configurar Sensores:**
   - La aplicación incluye módulos para sensores de movimiento y temperatura. Puedes ajustar la sensibilidad y los umbrales modificando los archivos de configuración en `src/utils/config.py`.

3. **Monitorear la Actividad:**
   - El sistema registrará todas las actividades en el directorio `logs`, que puedes monitorear en tiempo real.
   - Usa los controladores para anular la configuración manualmente si es necesario:
     ```bash
     python src/controllers/power_controller.py
     ```

4. **Control de Energía:**
   - La aplicación apagará automáticamente los equipos según la inactividad detectada o cuando se alcance un umbral de seguridad.

## Ejemplos
1. **Simulación de un Evento de Sensor de Movimiento:**
   ```bash
   python src/sensors/motion_sensor.py --simulate
