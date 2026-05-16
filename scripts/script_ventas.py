# =============================================================================
# Script de análisis de ventas - 2024
# Análisis de Ventas de una Pequeña Empresa
# Materia: Organización Empresarial – UTN TUP
# =============================================================================

import csv
import os

RUTA_DATOS  = os.path.join(os.getcwd(), 'datos', 'sales_data.csv')
RUTA_RESULT = os.path.join(os.getcwd(), 'resultados')

os.makedirs(RUTA_RESULT, exist_ok=True)

fechas = []
montos = []

with open(RUTA_DATOS, newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fechas.append(fila['sales_date'])       # cadena de texto "YYYY-MM-DD"
        montos.append(float(fila['sales_amount']))
