import os
import pandas as pd
import matplotlib.pyplot as plt

#Carga el dataset
oferta_gastronomica_df = pd.read_csv("oferta_gastronomica_limpio.csv", sep=";", encoding="latin-1")

#Revision inicial datos
print("\nDIMENSION DEL DATASET")
print(f"Filas: {oferta_gastronomica_df.shape[0]}")
print(f"Columnas: {oferta_gastronomica_df.shape[1]}")
print("\nCOLUMNAS DEL DATASET")
print(oferta_gastronomica_df.columns.tolist())

#FILTRADO
rubros_saludables = [
    "NATURISTA",
    "VEGETARIANA"
]

saludables_df = oferta_gastronomica_df[
    oferta_gastronomica_df["cocina"].isin(rubros_saludables)
].copy()

## Mostrar la cantidad de establecimientos saludables
cantidad_total = len(oferta_gastronomica_df)
cantidad_saludables = len(saludables_df)

porcentaje_saludables = (
    cantidad_saludables / cantidad_total * 100
)

print("\nCantidad de establecimientos saludables:")
print(cantidad_saludables)

print("\nPorcentaje sobre el total:")
print(round(porcentaje_saludables, 2), "%")

## Analizar la distribución por rubro
print("\nDISTRIBUCIÓN POR RUBRO")
print(saludables_df["cocina"].value_counts())

## Analizar la distribución por categoría
print("\nDISTRIBUCIÓN POR CATEGORÍA")
print(saludables_df["categoria"].value_counts())

## Analizar la concentración por barrio
print("\nCONCENTRACIÓN POR BARRIO")
print(saludables_df["barrio"].value_counts())

## Detectar barrios sin oferta saludable
todos_los_barrios = set(oferta_gastronomica_df["barrio"].unique())

barrios_saludables = set(saludables_df["barrio"].unique())

barrios_sin_oferta = sorted(
    todos_los_barrios - barrios_saludables
)

print("\nBARRIOS SIN OFERTA SALUDABLE")
for barrio in barrios_sin_oferta:
    print("-", barrio)

## Mostrar los locales saludables encontrados
print("\nLOCALES SALUDABLES ENCONTRADOS")

print(
    saludables_df[
        ["nombre", "categoria", "cocina", "barrio", "comuna"]
    ].to_string(index=False)
)

print("\nCONCLUSIONES")

print(
    f"La oferta saludable representa aproximadamente "
    f"el {porcentaje_saludables:.2f}% del total."
)

print(
    "Los rubros naturista y vegetariano tienen una presencia "
    "reducida dentro del mercado analizado."
)

print(
    "Los barrios sin establecimientos saludables registrados "
    "podrían representar oportunidades para abrir nuevos locales."
)

print(
    "También existe una oportunidad para ofrecer formatos distintos "
    "a los que actualmente predominan, como cafeterías saludables, "
    "delivery, comida rápida saludable o sandwicherías."
)