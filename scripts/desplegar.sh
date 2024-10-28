#!/bin/bash
# Script para desplegar la aplicación

echo "Desplegando la aplicación..."

# Copiar archivos al servidor
scp -r ./src user@server:/path/to/deployment

# Reiniciar el servicio
ssh user@server "systemctl restart my_application.service"

echo "Despliegue completado."
