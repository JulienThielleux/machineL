import pandas as pd
import re

from machineL.Menu.DeleteMenu import deleteDataMenu
from machineL.Menu.FillMenu import fillDataMenu
from machineL.Utils.Lutils import *


def cleanDataMenu(df):
    print("\n====================\nNettoyage des données")
    print("\nLe nom des colonnes sont les suivantes:")
    print(list(df.columns))

    userInput = ""
    while userInput != "OK":
        # Impression du menu cleanData
        print("\n\n*****************\nBoucle de nettoyage des données")
        print("Pour visualiser un apercu du dataset, taper view")
        print("Pour visualiser un apercu des Nan, taper nan")
        print("Pour visualiser un recapitulatif d'une colonne en particulier, taper simplement son nom")
        print("Pour plot une colonne, taper plot + son nom")
        print("Pour visualiser une ligne en particulier, taper line n")
        print("Pour trouver une ligne contenant une valeur en particulier dans une colonne, taper find + nom  + valeur")
        print("Pour accéder au menu de suppression , taper delete")
        print("Pour accéder au menu de remplissage, taper fill")
        print("Pour terminer la boucle de nettoyage, taper OK")
        userInput = input(":")

        # Visualisation du dataset
        if userInput == "view":
            showData(df)

        # Visualisation des Nan
        if userInput == "nan":
            showNan(df)

        # Visualisation d'une colonne.
        if userInput in df.columns:
            showColumn(userInput, df)

        # Plot d'une colonne sous forme d'histogramme.
        if userInput.startswith("plot "):
            remainer = userInput.split("plot ")[1]
            if remainer in df.columns:
                plotCol(remainer, df)

        # Visualisation d'une ligne.
        if re.match(r'^line \d+$', userInput):
            lineNumber = int(re.search(r'\d+$', userInput).group())
            if checkLineExist(lineNumber,df):
                showLine(lineNumber, df)

        # Trouver une valeur particulière dans une colonne.
        if userInput.startswith("find "):
            splits = userInput.split(" ")
            if splits[1] in df.columns:
                columnName = splits[1]
                toFindValue = splits[2]
                findLine(columnName,df,toFindValue)

        # Supprimer lignes ou colonnes.
        if userInput == "delete":
            df = deleteDataMenu(df)

        # Menu de traitement des Nan.
        if userInput == "fill":
            df = fillDataMenu(df)
