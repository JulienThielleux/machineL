import pandas as pd
import re
from machineL.Utils.Lutils import *
from  machineL.Tools.CleanTools import *

def deleteDataMenu(df):
    deleteDf = df

    userInput = ""
    while userInput != "OK":
        # Affichage du menu de delete
        print("\n=====\nBoucle de delete des données")
        print("Pour visualiser un apercu du dataset, taper view")
        print("Pour visualiser un apercu des Nan, taper nan")
        print("Pour supprimer toutes les colonnes ayant des NaN, taper col")
        print("Pour supprimer toutes les lignes ayant des Nan, taper line")
        print("Pour supprimer une colonne en particulier, taper le nom de la colonne")
        print("Pour supprimer une ligne en particulier, taper line n")
        print("Pour terminer la boucle de suppression, taper OK")
        userInput = input(":")

        # Visualisation du dataset
        if userInput == "view":
            showData(deleteDf)

        # Visualisation des Nan
        if userInput == "nan":
            showNan(deleteDf)

        # Suppression des colonnes automatiquement
        if userInput == "col":
            oldColNumber = len(deleteDf.columns)
            deleteDf = autoDeleteCol(deleteDf)
            print(str(oldColNumber - len(deleteDf.columns)) + " colonnes ont été supprimés")

        # Supression des lignes automatiquement
        if userInput == "line":
            oldLineNumber = deleteDf.shape[0]
            deleteDf = autoDeleteLine(deleteDf)
            print(str(oldLineNumber - deleteDf.shape[0]) + " lignes ont été supprimés")

        # Supression d'une colonne specifique
        if userInput in df.columns:
            deleteDf = deleteCol(userInput, deleteDf)

        # Supression d'une ligne specifique
        if re.match(r'^line \d+$', userInput):
            lineNumber = int(re.search(r'\d+$', userInput).group())
            if checkLineExist(lineNumber, df):
                deleteDf = deleteLine(lineNumber, deleteDf)

    return deleteDf
