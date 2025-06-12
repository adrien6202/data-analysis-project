import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('../data/tickets.csv')

# Nettoyer les colonnes inutiles
df_clean = df.drop(columns=['colonne_inutile'])

# Filtrer les tickets fermés
df_closed = df_clean[df_clean['statut'] == 'fermé']

# Calculer la durée de résolution (en jours)
df_closed['date_ouverture'] = pd.to_datetime(df_closed['date_ouverture'])
df_closed['date_fermeture'] = pd.to_datetime(df_closed['date_fermeture'])
df_closed['duree_resolution'] = (df_closed['date_fermeture'] - df_closed['date_ouverture']).dt.days

# Calcul du temps moyen de résolution
temps_moyen = df_closed['duree_resolution'].mean()
print(f"Temps moyen de résolution : {temps_moyen:.2f} jours")

# Affichage d’un histogramme des durées de résolution
plt.hist(df_closed['duree_resolution'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution du temps de résolution des tickets fermés')
plt.xlabel('Durée de résolution (jours)')
plt.ylabel('Nombre de tickets')
plt.show()
