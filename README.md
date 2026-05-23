# TP2 – Análisis de Ventas | Organización Empresarial

**Trabajo Práctico N.º 2**  
Tecnicatura Universitaria en Programación – UTN (Modalidad a Distancia)  
Materia: Organización Empresarial | Comisión: 9

---

## Integrantes

| Nombre | Rol |
|---|---|
| Juan Manuel Bravo | P1 – Líder y Organizador |
| Nicolás Rodríguez | P2 – Desarrollador Técnico |

---

## Descripción del proyecto

Este proyecto corresponde al Escenario B – **Análisis de Ventas de una Pequeña Empresa**.

Se desarrolló un script en Python que procesa un dataset de ventas diarias del año 2024 y genera indicadores clave para apoyar la evaluación del desempeño comercial de una empresa. El trabajo integra el uso de **Git y GitHub** para el control de versiones, **Jira** para la planificación y trazabilidad de tareas, y **Google Colab** como entorno de desarrollo.

---

## Dataset utilizado

**Fuente:** [Sales Sample Dataset – gist.github.com](https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6)

El dataset contiene 366 registros de ventas diarias correspondientes al año 2024, con las siguientes columnas:

| Columna | Descripción |
|---|---|
| `id` | Identificador único del registro |
| `sales_date` | Fecha de la venta (formato YYYY-MM-DD) |
| `sales_amount` | Monto de la venta en unidades monetarias |

El archivo se encuentra en la carpeta `/datos` del repositorio.

---

## Resultados generados

El script produce los siguientes archivos en la carpeta `/resultados`:

| Archivo | Descripción |
|---|---|
| `resumen_ventas_mensuales.csv` | Total de ventas agrupado por mes |
| `top10_dias_mayor_venta.csv` | Los 10 días con mayor monto de venta |
| `grafico_ventas_diarias.png` | Gráfico de línea con la evolución diaria de ventas |
| `grafico_ventas_mensuales.png` | Gráfico de barras con ventas totales por mes |

---

## Estructura del repositorio

```
TP2_OE_Bravo_Rodriguez/
│
├── datos/
│   └── sales_sample_2024.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── resumen_ventas_mensuales.csv
│   ├── top10_dias_mayor_venta.csv
│   ├── grafico_ventas_diarias.png
│   └── grafico_ventas_mensuales.png
│
├── README.md
└── .gitignore
```

---

## Instrucciones de ejecución

> El script utiliza rutas relativas, por lo que debe ejecutarse **desde la raíz del repositorio** en todos los casos.

### Google Colab (recomendado)

```python
# 1. Clonar el repositorio
!git clone https://github.com/usuario/TP2_OE_Bravo_Rodriguez.git
%cd TP2_OE_Bravo_Rodriguez

# 2. Instalar matplotlib si no está disponible
!pip install matplotlib

# 3. Ejecutar el script
!python scripts/analisis_ventas.py
```

### Linux / macOS

```bash
# 1. Activar el entorno virtual
source .venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el script
python scripts/analisis_ventas.py
```

### Windows (PowerShell)

```powershell
# 1. Activar el entorno virtual
.venv\Scripts\Activate.ps1
# Nota: si PowerShell bloquea la ejecución, correr primero:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el script
python scripts\analisis_ventas.py
```

---

## Dependencias

| Librería | Uso |
|---|---|
| `csv` | Lectura del dataset (módulo estándar de Python) |
| `os` | Manejo de rutas y carpetas (módulo estándar de Python) |
| `matplotlib` | Generación de gráficos |

---

## Trazabilidad

Las tareas de este proyecto fueron gestionadas en Jira. Cada commit del repositorio incluye el ID del issue correspondiente siguiendo el formato:

```
OE-8: Agregar cálculo de indicadores generales
```

:link: [Tablero de Jira](https://utn-programa.atlassian.net/jira/software/projects/OE/boards/1) 
:link: [Repositorio GitHub](https://github.com/JuanManuelBravo/TP2_OE_Bravo_Rodriguez)
