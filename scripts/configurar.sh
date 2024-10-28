#!/bin/bash
# Script para configurar el entorno

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Configurando variables de entorno..."
export ENV=production

echo "Configuración completa."
