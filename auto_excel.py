import pandas as pd

#lire le fichier Excel
df =pd.read_csv("input.csv")

# Nettoyer espaces
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# supprimer Lignes Vides
df = df.dropna()

# supprimer les doublons
df = df.drop_duplicates()

# trier par nom
df = df.sort_values(by="Nom")

# Validation Email
def check_Email(x: str)-> str:
    if isinstance(x, str) and "@" in x and "." in x:
        return "OK"
    return "Erreur"

df["Statut"] = df[" Email"].apply(check_Email)

# sauvegarder dans un nouveau fichier
df.to_csv("output.csv", index=False)

print("fichier nettoyer créér !")
