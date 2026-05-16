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


registros = list(zip(fechas, montos))
top10 = sorted(registros, key=lambda x: x[1], reverse=True)[:10]

print("\n" + "=" * 55)
print("TOP 10 DÍAS CON MAYORES VENTAS")
print("=" * 55)
print(f"  {'#':<5} {'Fecha':<15} {'Monto ($)'}")
print(f"  {'-'*4} {'-'*14} {'-'*10}")
for i, (fecha, monto) in enumerate(top10, start=1):
    print(f"  {i:<5} {fecha:<15} $ {monto:,.0f}")

# Exportar top 10 a CSV
ruta_top10 = os.path.join(RUTA_RESULT, 'top10_dias_mayor_venta.csv')
with open(ruta_top10, 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Posicion', 'Fecha', 'Monto'])
    for i, (fecha, monto) in enumerate(top10, start=1):
        escritor.writerow([i, fecha, monto])
print(f"\n  → Exportado: {ruta_top10}")
