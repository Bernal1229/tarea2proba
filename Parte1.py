import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------- Parte 1: Dados Ideales ----------------------------

# Definir los posibles resultados de un dado
dado_ideal = [1, 2, 3, 4, 5, 6]

# Crear una lista de las sumas al lanzar dos dados
sumas_ideales = [x + y for x in dado_ideal for y in dado_ideal]

# Crear una Serie de pandas a partir de las sumas
serie_sumas_ideales = pd.Series(sumas_ideales)

# Contar las ocurrencias de cada suma y normalizar (calcular la probabilidad)
pmf_ideales = serie_sumas_ideales.value_counts(normalize=True).sort_index()

# Crear un DataFrame para visualizar mejor
pmf_ideales_df = pd.DataFrame({'Suma': pmf_ideales.index, 'Probabilidad': pmf_ideales.values})

# ---------------------------- Parte 2: Dados de Truco ----------------------------

# Probabilidades del dado 1 (sesgado para obtener 3 con probabilidad 0.7)
prob_dado_truco_1 = {1: 0.06, 2: 0.06, 3: 0.7, 4: 0.06, 5: 0.06, 6: 0.06}

# Probabilidades del dado 2 (sesgado para obtener 4 con probabilidad 0.7)
prob_dado_truco_2 = {1: 0.06, 2: 0.06, 3: 0.06, 4: 0.7, 5: 0.06, 6: 0.06}

# Crear lista de las sumas posibles y sus probabilidades
sumas_truco = []
probabilidades_sumas_truco = []

for x in prob_dado_truco_1:
    for y in prob_dado_truco_2:
        suma_truco = x + y
        probabilidad_truco = prob_dado_truco_1[x] * prob_dado_truco_2[y]
        sumas_truco.append(suma_truco)
        probabilidades_sumas_truco.append(probabilidad_truco)

# Crear una Serie de pandas para las sumas y probabilidades
df_sumas_truco = pd.DataFrame({'Suma': sumas_truco, 'Probabilidad': probabilidades_sumas_truco})

# Agrupar por suma para obtener la probabilidad total de cada suma
pmf_truco = df_sumas_truco.groupby('Suma').sum()

# ---------------------------- Graficar Ambos PMFs ----------------------------

# Imprimir las tablas de las PMFs
print("PMF - Dados Ideales:")
print(pmf_ideales_df)
print("\nPMF - Dados de Truco:")
print(pmf_truco)


# Crear una figura con dos subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Graficar la PMF de los dados ideales en el primer subplot
axes[0].stem(pmf_ideales_df['Suma'], pmf_ideales_df['Probabilidad'], basefmt=" ")
axes[0].set_xlabel('Suma de Dos Dados (Ideales)')
axes[0].set_ylabel('Probabilidad')
axes[0].set_title('PMF - Dados Ideales')
axes[0].set_xticks(range(2, 13))
axes[0].grid(False)

# Graficar la PMF de los dados de truco en el segundo subplot
axes[1].stem(pmf_truco.index, pmf_truco['Probabilidad'], basefmt=" ")
axes[1].set_xlabel('Suma de Dos Dados (Truco)')
axes[1].set_ylabel('Probabilidad')
axes[1].set_title('PMF - Dados de Truco')
axes[1].set_xticks(range(2, 13))
axes[1].grid(False)

# Ajustar los espacios entre subplots y mostrar el gráfico
plt.tight_layout()
plt.show()

