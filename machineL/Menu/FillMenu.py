import pandas as pd
import re
from machineL.Utils.Lutils import *
from machineL.Tools.CleanTools import  *

def fillDataMenu(df):
    fillDf = df

    userInput = ""
    while userInput != "OK":
        # Affichage du menu de remplissage des NaN
        print("\n=====\nBoucle de remplissage des données")
        print("Pour visualiser un apercu du dataset, taper view")
        print("Pour visualiser un apercu des Nan, taper nan")
        print("Pour remplacer les Nan d'une colonne par une valeur fixe, taper le nom de la colonne")
        print("Pour remplacer les Nan d'une colonne par la moyenne de la colonne, taper mean + le nom de la colonne")

        print("Pour terminer la boucle de remplissage, taper OK")
        userInput = input(":")

        # Visualisation du dataset
        if userInput == "view":
            showData(fillDf)

        # Visualisation des Nan
        if userInput == "nan":
            showNan(fillDf)

        # Remplissage fixe des Nan
        if userInput in fillDf.columns:
            fillDf = fixFillCol(userInput, fillDf)

        # Remplissage moyen des Nan
        if userInput.startswith("mean "):
            remainer = userInput.split("mean ")[1]
            print("Cette fonction ne marchera que si la colonne ne contient que des données numeriques")
            if remainer in fillDf.columns:
                if testNumeric(fillDf[remainer]):
                    fillDf = meanFillCol(remainer, fillDf)

    return fillDf