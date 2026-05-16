# =============================================================================
# Script de análisis de ventas - 2024
# Análisis de Ventas de una Pequeña Empresa
# Materia: Organización Empresarial – UTN TUP
# =============================================================================

import csv
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

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


ventas_por_mes = {}

for fecha, monto in registros:
    mes = fecha[:7]   # tomar solo "YYYY-MM" de "YYYY-MM-DD"
    if mes not in ventas_por_mes:
        ventas_por_mes[mes] = 0
    ventas_por_mes[mes] += monto

# Ordenar por mes cronológicamente
meses   = sorted(ventas_por_mes.keys())
totales = [ventas_por_mes[m] for m in meses]

mes_mayor = meses[totales.index(max(totales))]
mes_menor = meses[totales.index(min(totales))]

print("\n" + "=" * 55)
print("VENTAS POR MES")
print("=" * 55)
print(f"  {'Mes':<12} {'Total ($)'}")
print(f"  {'-'*11} {'-'*12}")
for mes, total in zip(meses, totales):
    print(f"  {mes:<12} $ {total:,.0f}")
print(f"\n  Mes con más ventas:   {mes_mayor}  ($ {max(totales):,.0f})")
print(f"  Mes con menos ventas: {mes_menor}  ($ {min(totales):,.0f})")

# Exportar resumen mensual a CSV
ruta_mensual = os.path.join(RUTA_RESULT, 'resumen_ventas_mensuales.csv')
with open(ruta_mensual, 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Mes', 'Total'])
    for mes, total in zip(meses, totales):
        escritor.writerow([mes, total])
print(f"  → Exportado: {ruta_mensual}")


fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(range(len(montos)), montos, color='steelblue', linewidth=0.8)
ax.axhline(venta_promedio, color='tomato', linestyle='--', linewidth=1.2,
           label=f'Promedio diario: ${venta_promedio:,.0f}')

# Marcar en el eje X el primer día de cada mes
indices_meses   = []
etiquetas_meses = []
mes_actual = None
for i, fecha in enumerate(fechas):
    mes = fecha[:7]
    if mes != mes_actual:
        indices_meses.append(i)
        etiquetas_meses.append(mes)
        mes_actual = mes

ax.set_xticks(indices_meses)
ax.set_xticklabels(etiquetas_meses, rotation=30, fontsize=8)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_title('Evolución Diaria de Ventas – 2024', fontsize=13, fontweight='bold')
ax.set_xlabel('Mes', fontsize=10)
ax.set_ylabel('Monto ($)', fontsize=10)
ax.legend(fontsize=9)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()

ruta_graf1 = os.path.join(RUTA_RESULT, 'grafico_ventas_diarias.png')
plt.savefig(ruta_graf1, dpi=150)
plt.close()
print(f"\n  → Gráfico exportado: {ruta_graf1}")

