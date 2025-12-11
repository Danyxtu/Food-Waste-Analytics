import pandas as pd

# Dataset
faostat_commodities_csv = 'Datasets/faostat-commodities.csv'
annex2_urban_vs_rural_csv = 'Datasets/annex2.csv'

# Read CSVs
df_commodities = pd.read_csv(faostat_commodities_csv)
df_urban_rural = pd.read_csv(annex2_urban_vs_rural_csv)