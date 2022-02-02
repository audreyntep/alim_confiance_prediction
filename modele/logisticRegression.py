# REGRESSION LOGISTIQUE

""" 1.IMPORT DES LIBRAIRIES """
# librairies classiques
import pandas as pd
import numpy as np

# packages scikit-learn
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
print(sklearn.__version__)

# packages visualisation
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# REGRESSION LOGISTIQUE

""" 2.IMPORT DU DATASET """
# Récupération du jeu de données
dataset=pd.read_csv('modele/data/clean/export_alimconfiance.csv', sep=";")

# visualisation du jeu de données
dataset.head()

""" 3.DESCRIPTION ET VISUALISATION """
# description rapide du jeu de données
dataset.info()

for column in dataset.columns:
    print(column, dataset[column].nunique())

# Affichage de la matrice de correlation
mat_corr = dataset.corr()
# en utilisant seaborn
plt.figure(figsize=(8,6))
sns.heatmap(mat_corr, annot=True) # avec seaborn
plt.show()

""" 4.SEPARATION DU DATASET EN TRAIN ET TEST SET """