#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para generar el Mapa Conceptual - Opción 2 con Matplotlib
Dataset: Terremotos Chile 2000-2024
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

print("=" * 70)
print("GENERANDO MAPA CONCEPTUAL - CLASIFICACION DE VARIABLES")
print("=" * 70)

# Paso 1: Crear directorio
print("\n[1/3] Preparando estructura de directorios...")
if not os.path.exists('graficos'):
    os.makedirs('graficos')
    print("    ✓ Directorio 'graficos/' creado")
else:
    print("    ✓ Directorio 'graficos/' ya existe")

# Paso 2: Crear figura
print("\n[2/3] Generando diagrama del mapa conceptual...")

fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Colores
color_raiz = '#FFD700'
color_cat = '#87CEEB'
color_nom = '#B0E0E6'
color_ord = '#B0E0E6'
color_num = '#90EE90'
color_cont = '#98FB98'
color_var = '#E0FFFF'
color_numvar = '#F0FFF0'

def draw_box(ax, x, y, width, height, text, color, fontsize=10, fontweight='normal'):
    """Dibuja una caja redondeada con texto"""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.1", 
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
            fontweight=fontweight, wrap=True)

def draw_arrow(ax, x1, y1, x2, y2):
    """Dibuja una flecha entre dos puntos"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, 
                           linewidth=2, color='black')
    ax.add_patch(arrow)

# Nodo raíz
draw_box(ax, 5, 12.5, 3, 1, 'DATASET TERREMOTOS\nCHILE 2000-2024\n(134,062 registros)', 
         color_raiz, fontsize=11, fontweight='bold')

# Variables Categóricas y Numéricas
draw_box(ax, 2.5, 10.5, 2.5, 1, 'VARIABLES\nCATEGORICAS\n(6 variables)', 
         color_cat, fontsize=10, fontweight='bold')
draw_box(ax, 7.5, 10.5, 2.5, 1, 'VARIABLES\nNUMERICAS\n(2 variables)', 
         color_num, fontsize=10, fontweight='bold')

# Flechas principales
draw_arrow(ax, 4.5, 12, 3.2, 11)
draw_arrow(ax, 5.5, 12, 6.8, 11)

# Nominales y Ordinales
draw_box(ax, 1, 8.5, 2, 0.8, 'NOMINALES\n(Sin orden)', 
         color_nom, fontsize=9, fontweight='bold')
draw_box(ax, 4, 8.5, 2, 0.8, 'ORDINALES\n(Con orden)', 
         color_ord, fontsize=9, fontweight='bold')

# Continuas
draw_box(ax, 7.5, 8.5, 2.5, 0.8, 'CONTINUAS\n(Infinitos valores)', 
         color_cont, fontsize=9, fontweight='bold')

# Flechas categóricas
draw_arrow(ax, 2, 10, 1.5, 8.9)
draw_arrow(ax, 3, 10, 4, 8.9)

# Flecha numéricas
draw_arrow(ax, 7.5, 10, 7.5, 8.9)

# Variables Nominales específicas
draw_box(ax, 0.3, 7, 1.8, 0.7, 'Location\n(28,965 valores)', color_var, fontsize=8)
draw_box(ax, 1.7, 7, 1.8, 0.7, 'UTC Date\n(133,946 valores)', color_var, fontsize=8)

# Flechas a nominales
draw_arrow(ax, 0.8, 8.1, 0.3, 7.35)
draw_arrow(ax, 1.2, 8.1, 1.7, 7.35)

# Variables Ordinales específicas
draw_box(ax, 2.8, 7, 1.6, 0.7, 'Magnitude\n(244 valores)', color_var, fontsize=8)
draw_box(ax, 4.4, 7, 1.6, 0.7, 'Profoundity\n(391 valores)', color_var, fontsize=8)
draw_box(ax, 6, 7, 1.4, 0.7, 'Date\n(8,771 valores)', color_var, fontsize=8)
draw_box(ax, 7.5, 7, 1.4, 0.7, 'Hour\n(68,078 valores)', color_var, fontsize=8)

# Flechas a ordinales
draw_arrow(ax, 3.2, 8.1, 2.8, 7.35)
draw_arrow(ax, 3.8, 8.1, 4.4, 7.35)
draw_arrow(ax, 4.2, 8.1, 6, 7.35)
draw_arrow(ax, 4.2, 8.1, 7.5, 7.35)

# Variables Numéricas específicas
draw_box(ax, 6.5, 7, 2, 0.7, 'Latitude\n(Rango: -65.4 a 58.7)', color_numvar, fontsize=8)
draw_box(ax, 8.5, 7, 2, 0.7, 'Longitude\n(Rango: -179.9 a 179.6)', color_numvar, fontsize=8)

# Flechas a numéricas
draw_arrow(ax, 7, 8.1, 6.5, 7.35)
draw_arrow(ax, 8, 8.1, 8.5, 7.35)

# Agregar leyenda/resumen
summary_text = """
RESUMEN DEL MAPA CONCEPTUAL

VARIABLES CATEGORICAS (6):
  ├─ Nominales (2): Location, UTC Date
  └─ Ordinales (4): Magnitude, Profoundity, Date, Hour

VARIABLES NUMERICAS (2):
  └─ Continuas (2): Latitude, Longitude

ESTADISTICAS:
  • Total de variables: 8
  • Total de registros: 134,062
  • Valores nulos: 472 (0.35%)
  • Período: 2000-2024
"""

ax.text(5, 4.5, summary_text, ha='center', va='top', fontsize=9,
        family='monospace', bbox=dict(boxstyle='round', facecolor='#FFFACD', alpha=0.8))

# Título
ax.text(5, 13.5, 'Opción 2: Clasificación de Variables del Dataset', 
        ha='center', va='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', linewidth=2))

plt.tight_layout()

# Paso 3: Guardar figura
print("\n[3/3] Guardando imagen...")
try:
    output_path = 'graficos/mapa_conceptual_option2.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"    ✓ Imagen guardada correctamente")
    print(f"    ✓ Ruta: {output_path}")
    plt.close()
except Exception as e:
    print(f"    ✗ Error al guardar imagen: {e}")

print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)
print("\n✓ Mapa conceptual generado exitosamente")
print("\nUbicación del archivo:")
print(f"  → graficos/mapa_conceptual_option2.png")
print("\nCaracterísticas del mapa:")
print("  → Formato: PNG de alta calidad (300 DPI)")
print("  → Variables Categóricas: 6 (Nominales + Ordinales)")
print("  → Variables Numéricas: 2 (Continuas)")
print("  → Total de variables: 8")
print("  → Total de registros: 134,062")
print("\n" + "=" * 70)
