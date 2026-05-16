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

print("=" * 55)
print("ANÁLISIS DE VENTAS 2024")
print("=" * 55)
print(f"Registros cargados: {len(montos)}")
print(f"Período: {fechas[0]}  →  {fechas[-1]}")

venta_total    = sum(montos)
venta_promedio = venta_total / len(montos)
venta_max      = max(montos)
venta_min      = min(montos)

# Buscar las fechas correspondientes al máximo y mínimo
dia_max = fechas[montos.index(venta_max)]
dia_min = fechas[montos.index(venta_min)]

print("\n" + "=" * 55)
print("INDICADORES GENERALES")
print("=" * 55)
print(f"  Venta total del año:    $ {venta_total:,.0f}")
print(f"  Venta promedio diaria:  $ {venta_promedio:,.2f}")
print(f"  Día con mayor venta:    {dia_max}  ($ {venta_max:,.0f})")
print(f"  Día con menor venta:    {dia_min}  ($ {venta_min:,.0f})")

