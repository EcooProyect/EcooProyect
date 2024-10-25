# EnergySaverProject

## Descripción
EnergySaverProject es un software diseñado para monitorear la actividad de un equipo y, después de un tiempo de inactividad, apagarlo de manera segura. Su objetivo principal es ahorrar energía y proteger los dispositivos de posibles daños por sobrecalentamiento o uso prolongado.

## Características
- **Monitoreo continuo de la actividad del equipo:** El software detecta la inactividad para tomar acciones según configuraciones definidas.
- **Apagado seguro tras un periodo de inactividad:** Después de un tiempo configurable sin actividad, se ejecuta un procedimiento de apagado seguro del equipo.
- **Integración con sensores para detectar presencia (opcional):** Puede configurarse para trabajar con sensores de movimiento y temperatura, manteniendo el dispositivo encendido si detecta la presencia o actividad cercana.
- **Configuración personalizable:** El usuario puede establecer tiempos de inactividad, umbrales de temperatura, y otras configuraciones para ajustar el comportamiento del software.
- **Notificaciones y alertas:** El sistema puede enviar alertas antes de proceder con el apagado para advertir al usuario.
- **Control de dispositivos periféricos:** Incluye la capacidad de controlar ventiladores o alarmas si se detecta que la temperatura ha superado los límites definidos.

## Estructura del Proyecto

### `src/`
- **`main.py`**: Punto de entrada de la aplicación, encargado de iniciar los módulos de monitoreo y control.
- **`controllers/`**
  - **`power_controller.py`**: Gestiona el encendido y apagado del equipo.
  - **`safety_controller.py`**: Activa medidas de seguridad en caso de sobrecalentamiento.
- **`sensors/`**
  - **`motion_sensor.py`**: Detecta movimiento para determinar si hay presencia en las cercanías.
  - **`temperature_sensor.py`**: Monitorea la temperatura para activar el ventilador o la alarma si es necesario.
- **`utils/`**
  - **`logger.py`**: Gestiona la generación de logs para el sistema.
  - **`config.py`**: Almacena configuraciones globales y parámetros del sistema.
  
### `tests/`
- Contiene pruebas unitarias para validar la funcionalidad de los módulos principales del proyecto.

### `scripts/`
- **`deploy.sh`**: Script para desplegar el software en otros equipos.
- **`setup.sh`**: Script para instalar dependencias necesarias.

### `README.md`
- Contiene la descripción general del proyecto, instrucciones de instalación y uso.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/EnergySaverProject.git
   cd EnergySaverProject
