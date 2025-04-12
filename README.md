Analyse de la série temporelle de température (iot-temp)
Description du projet
Ce projet contient un script Python qui analyse un jeu de données de températures (iot-temp.csv) pour extraire des informations utiles sur les variations de température dans le temps. Le fichier de données contient des mesures de température prises à différents moments, et le script effectue plusieurs analyses statistiques et graphiques pour mieux comprendre ces données.

Objectifs du projet :
Le script suit les étapes suivantes pour analyser les données :

Calculer des statistiques de base : la moyenne, la variance et l’écart-type des températures.
Tracer un graphique de la série temporelle pour visualiser l’évolution de la température.
Créer des nuages de points pour comparer la température à un moment donné avec ses valeurs passées (décalages de 1 à 8).
Tracer la fonction d’auto-corrélation (ACF) pour analyser les relations entre les températures à différents décalages (jusqu’à 50).
Proposer une méthode pour interpréter l’auto-corrélation afin de détecter une tendance ou une saisonnalité dans les données.
Utilité :
Ce projet est utile pour :

Comprendre les comportements de la température dans un environnement (par exemple, une maison ou un espace surveillé par un capteur IoT).
Identifier des motifs, comme des cycles quotidiens (saisonnalité) ou des tendances à long terme (par exemple, une augmentation progressive de la température).
Obtenir une vue d’ensemble des variations de température grâce à des graphiques clairs.
Prérequis
Pour exécuter ce projet, vous devez avoir les éléments suivants installés sur votre machine :

Python 3.6 ou supérieur : Le script est écrit en Python. Vous pouvez vérifier votre version avec la commande suivante : python --version

pip : L’outil de gestion des packages Python pour installer les bibliothèques nécessaires. Il est généralement inclus avec Python.
Bibliothèques Python nécessaires :
Le script utilise les bibliothèques suivantes. Vous devrez les installer avant d’exécuter le code :

pandas : Pour manipuler et analyser les données (lecture du fichier CSV, gestion des dates, calculs statistiques).
numpy : Pour des calculs mathématiques (utilisé par d’autres bibliothèques).
matplotlib : Pour tracer les graphiques (série temporelle, nuages de points, auto-corrélation).
statsmodels : Pour calculer et tracer la fonction d’auto-corrélation (ACF).
Installation des bibliothèques :
- pip install --upgrade pip
- pip install pandas numpy matplotlib statsmodels

Structure du projet
iot_temp_analysis.py : Le script principal qui contient le code pour analyser les données de température.
iot-temp.csv : Le fichier de données contenant les mesures de température (vous devez fournir ce fichier). Il doit avoir les colonnes suivantes :
temp : La température mesurée (en degrés Celsius).
noted_date : La date et l’heure de la mesure (format : DD-MM-YYYY HH:MM).
out/in : Une colonne indiquant si la mesure a été prise à l’intérieur ou à l’extérieur (non utilisée dans ce script).
README.md : Ce fichier, qui explique le projet et comment l’utiliser.

Résultats attendus :
Le script affichera les statistiques (moyenne, variance, écart-type) dans la console.
Il ouvrira plusieurs fenêtres de graphiques :
Un graphique de la série temporelle (température en fonction du temps).
Huit nuages de points comparant la température à ses valeurs décalées.
Un graphique de la fonction d’auto-corrélation (ACF).
Une note dans la console vous guidera pour interpréter l’ACF et détecter une tendance ou une saisonnalité.

Fonctionnement du projet
Contexte :
Le fichier iot-temp.csv contient des données de température collectées par un capteur IoT, probablement dans une maison ou un environnement surveillé. Ces données incluent des milliers de mesures (environ 10 000 lignes), avec une température enregistrée à chaque date et heure.

Fonctionnement général :
Le script lit le fichier, traite les données, et effectue des analyses pour répondre aux questions suivantes :

Quelle est la température moyenne ? Est-ce qu’elle varie beaucoup ?
Comment la température évolue-t-elle dans le temps ?
Est-ce que la température d’un moment donné est liée à celle des moments précédents ?
Y a-t-il des motifs répétitifs ou une tendance dans les données ?
Étapes détaillées :
Charger les données :
Le script lit le fichier CSV et organise les données pour que les dates soient reconnues comme des moments dans le temps.
Calculer des statistiques :
Il calcule la moyenne, la variance et l’écart-type des températures pour donner une idée générale des données.
Tracer la série temporelle :
Un graphique montre l’évolution de la température au fil du temps.
Tracer les nuages de points :
Le script compare la température actuelle avec ses valeurs passées (décalages de 1 à 8) pour voir s’il y a des relations.
Tracer la fonction d’auto-corrélation :
Un graphique montre à quel point la température est similaire à elle-même après différents décalages (jusqu’à 50).
Interpréter les résultats :
En regardant le graphique d’auto-corrélation, on peut deviner si la température suit une tendance (par exemple, elle augmente avec le temps) ou une saisonnalité (par exemple, un cycle quotidien).
