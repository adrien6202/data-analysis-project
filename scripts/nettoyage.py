import pandas as pd

# Charger les données
df = pd.read_csv('../data/tickets.csv')

# Nettoyer les colonnes inutiles
df_clean = df.drop(columns=['colonne_inutile'])

# Filtrer les tickets fermés
df_closed = df_clean[df_clean['statut'] == 'fermé']

print(df_closed.head())
