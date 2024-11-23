# EnergySaverProject

## Descripción
EnergySaverProject es un software diseñado para monitorear la actividad de un equipo y, después de un tiempo de inactividad, apagarlo de manera segura. Su objetivo principal es ahorrar energía y proteger los dispositivos de posibles daños por sobrecalentamiento o uso prolongado.

# Conóceme

## 1. Requerimientos Funcionales y No Funcionales

### Requerimientos Funcionales
- **Gestión de Dispositivos:** El sistema debe permitir a los usuarios gestionar dispositivos (encender/apagar).
- **Detección de Movimiento:** Los sensores deben poder detectar movimiento y notificar al sistema.
- **Registro de Resultados:** El sistema debe almacenar los resultados de las pruebas realizadas por los sensores.

### Requerimientos No Funcionales
- **Usabilidad:** La interfaz debe ser intuitiva y fácil de usar.
- **Rendimiento:** El sistema debe responder a las acciones del usuario en menos de 2 segundos.
- **Seguridad:** Los datos del usuario deben estar protegidos con métodos de encriptación.

## 2. Tablas Usadas en el Diagrama de Entidad-Relación

- **Usuarios** (`usuarios`)
  - ID de usuario
  - Nombre
  - Correo electrónico
  - Contraseña

- **Dispositivos** (`dispositivos`)
  - ID de dispositivo
  - Nombre del dispositivo
  - Estado
  - Tipo

- **Resultados** (`resultados`)
  - ID de resultado
  - ID de dispositivo (foránea)
  - Timestamp
  - Resultado

## 3. Pruebas Realizadas en la Etapa de Prototipado

- **Prueba de Detección de Movimiento:** Se verifica que el sensor detectara correctamente el movimiento simulado.
- **Prueba de Gestión de Energía:** Se evalua que el controlador pudiera encender y apagar el dispositivo correctamente.
- **Prueba de Detección de temperatura:** Se verifica que sensor dertecte en porcentaje mayormente acertivo entorno al ambiente y sector de prueba
**Prueba de Gestion de Seguridad:** Se tiene en cuenta el resultado de los sensores para proceder a relaizar atajos seguros para proceder al apagado

## 4. Sistema de Gestión de Bases de Datos (SGBD)

Se decidió utilizar **MySQL** como SGBD para el proyecto debido a su robustez, facilidad de uso y capacidad para manejar grandes volúmenes de datos. MySQL es ampliamente utilizado en la industria, lo que facilita el soporte y la integración con otras herramientas.

## 5. Modelo de Entidad-Relación

A continuación se muestra el modelo de entidad-relación del sistema, que describe las entidades y sus relaciones:

[Usuarios] ---< (1,n) >--- [Dispositivos] | | (1,n) (1,n) | | [Resultados] ---< (1,n) >--- [Dispositivos]

### Carpetas y Archivos Relacionados
- **`fuentes/controladores`**
  - `controladorEnergia.py`: Controlador para gestionar el estado de los dispositivos.
  - `controladorSeguridad.py`: Controlador para gestionar los protocolos de seguridad.
- **`fuentes/sensores`**
  - `sensor_movimiento.py`: Sensor que detecta movimiento.
  - `sensor_temperatura.py`: Sensor que mide la temperatura.
- **`pruebas`**
  - `prueba_controlador_gastoenergia.py`: Verifica el funcionamiento del controlador de energía.
  - `prueba_controlador_seguridad.py`: Verifica el funcionamiento del sensor de movimiento.

## 6. Por qué usar Python

Se eligió **Python** como el lenguaje de programación principal para el proyecto debido a varias razones:

- **Simplicidad y Legibilidad:** Python es conocido por su sintaxis clara y legible, lo que facilita la escritura y el mantenimiento del código. Esto es especialmente útil en proyectos colaborativos, donde varios desarrolladores pueden trabajar en el mismo código base.

- **Gran Ecosistema de Bibliotecas:** Python cuenta con una amplia variedad de bibliotecas y frameworks que permiten realizar tareas específicas de manera eficiente. Por ejemplo, bibliotecas como `unittest` para pruebas, `Flask` o `Django` para el desarrollo web, y `SQLAlchemy` para la interacción con bases de datos, hacen que el desarrollo sea más ágil y robusto.

- **Comunidad Activa:** La comunidad de Python es grande y activa, lo que significa que hay una abundante cantidad de recursos, documentación y soporte disponibles. Esto ayuda a resolver problemas rápidamente y a aprender mejores prácticas de programación.

- **Interoperabilidad:** Python puede integrarse fácilmente con otros lenguajes y tecnologías, lo que lo convierte en una opción versátil para proyectos que requieren colaborar con diferentes sistemas.

- **Aplicaciones en Diferentes Áreas:** Python es adecuado para una variedad de aplicaciones, desde el desarrollo web hasta el análisis de datos y la inteligencia artificial. Esta flexibilidad permite que el mismo lenguaje se utilice para diferentes aspectos del proyecto, facilitando la colaboración y la coherencia en el desarrollo.

Por estas razones, Python se presenta como una opción ideal para el desarrollo del proyecto, permitiendo un enfoque eficiente y efectivo en la creación de la aplicación de monitoreo y gestión de energía.
