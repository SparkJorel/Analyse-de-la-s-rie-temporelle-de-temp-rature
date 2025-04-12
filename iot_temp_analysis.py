import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Étape 1 : Charger le jeu de données
# Remplacez 'iot-temp.csv' par le chemin de votre fichier
df = pd.read_csv('iot-temp.csv')

# Convertir la colonne 'noted_date' en format datetime et la définir comme index
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')
df.set_index('noted_date', inplace=True)

# Extraire la colonne 'temp' pour l'analyse
temps = df['temp']

# Étape 2 : Calculer la moyenne, la variance et l'écart-type
moyenne_temp = temps.mean()
variance_temp = temps.var()
ecart_type_temp = temps.std()

print(f"Moyenne : {moyenne_temp:.2f}")
print(f"Variance : {variance_temp:.2f}")
print(f"Écart-type : {ecart_type_temp:.2f}")

# Étape 3 : Représenter la série temporelle
plt.figure(figsize=(12, 6))
plt.plot(temps, label='Température', color='blue')
plt.title('Série temporelle de la température')
plt.xlabel('Date')
plt.ylabel('Température')
plt.legend()
plt.grid()
plt.show()

# Étape 4 : Représenter les nuages de points N_1, N_2, ..., N_8
# Cela signifie tracer des nuages de points pour des décalages (lags) de 1 à 8
# Par exemple, N_1 : temp(t) vs temp(t-1), N_2 : temp(t) vs temp(t-2), etc.
plt.figure(figsize=(15, 10))
for lag in range(1, 9):  # De N_1 à N_8
    plt.subplot(4, 2, lag)
    plt.scatter(temps.shift(lag), temps, alpha=0.5, s=10)
    plt.title(f'N_{lag} : Temp(t) vs Temp(t-{lag})')
    plt.xlabel(f'Temp(t-{lag})')
    plt.ylabel('Temp(t)')
    plt.grid()
plt.tight_layout()
plt.show()

# Étape 5 : Représenter la fonction d'auto-corrélation pour k=1 à 50
plt.figure(figsize=(12, 6))
plot_acf(temps, lags=50, alpha=0.05)
plt.title('Fonction d\'auto-corrélation (ACF) de la température')
plt.xlabel('Décalage (k)')
plt.ylabel('Auto-corrélation')
plt.grid()
plt.show()

# Étape 6 : Analyser la courbe d'auto-corrélation pour détecter une tendance ou une saisonnalité
# Cette étape nécessite une inspection visuelle du graphique ACF :
# - Une décroissance lente de l'ACF indique une tendance.
# - Des pics périodiques dans l'ACF indiquent une saisonnalité.
# Je vais fournir une note pour vous aider à interpréter le graphique.

print("Interprétation de l'ACF :")
print("- Si l'ACF décroît lentement, il peut y avoir une tendance.")
print("- S'il y a des pics périodiques (par exemple, tous les 24 lags pour des données horaires), il peut y avoir une saisonnalité.")
print("Veuillez inspecter le graphique ACF pour déduire la présence d'une tendance et/ou d'une saisonnalité.")