import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244,1983,702,6322,5957/property/MolecularWeight,LogP,InChIKey,CanonicalSMILES/CSV"
df = pd.read_csv(url)

print("First few rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="MolecularWeight", y="LogP", hue="CID", palette="viridis", s=100)
plt.title("Molecular Weight vs LogP", fontsize=14)
plt.xlabel("Molecular Weight", fontsize=12)
plt.ylabel("LogP", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="CID", y="LogP", palette="Set2")
plt.title("LogP Values for Different Compounds", fontsize=14)
plt.xlabel("Compound CID", fontsize=12)
plt.ylabel("LogP", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Bonus Explanation:
bonus_text = """
Bonus: How trends in molecular properties support solvent selection in drug development

- LogP indicates how soluble a compound is in fat (lipophilic) or water (hydrophilic).
- Compounds with high LogP are more soluble in non-polar solvents (like oils).
- Compounds with low LogP are more soluble in polar solvents (like water).
- Molecular Weight affects solubility and permeability — lower weight usually means better absorption.
- Knowing these helps in choosing suitable solvents for drug formulation and delivery.

This analysis helps in making better decisions during drug development.
"""

print(bonus_text)
