# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y análisis
# ==============================================================================
import statsmodels.api as sm
import pingouin as pg
from scipy import stats
from scipy.stats import pearsonr

datos = pd.read_csv("all-weeks-global.csv")
datos = datos[['category','weekly_rank','weekly_hours_viewed','runtime','weekly_views','cumulative_weeks_in_top_10','is_staggered_launch']]
datos = datos[:1641]
from sklearn.preprocessing import OrdinalEncoder

# Creamos el codificador indicandole el orden de la variables
encoder = OrdinalEncoder(categories=[['TV (English)','TV (Non-English)','Films (English)','Films (Non-English)']])
encoder.fit(datos[["category"]])
datos["category"] = encoder.transform(datos[["category"]])
#dummies = pd.get_dummies(datos['category'], drop_first = False)
#datos = pd.concat([datos, dummies], axis = 1)
#datos = datos.drop(columns=['category'])
corr_matrix = datos.corr(method='pearson')

# Gráfico de correlaciones
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corr_matrix, annot = True, cmap='coolwarm', fmt=".2f", ax=ax)
plt.yticks(rotation=0)
plt.show()