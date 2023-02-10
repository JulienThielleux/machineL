import matplotlib.pyplot as plt
import pandas as pd

def openFile(filename, filepath="./csvFiles/"):
    print("\n====================\nouverture du fichier " + filename)
    fileContent = pd.read_csv(filepath + filename)
    print("Ouverture terminée")
    showData(fileContent)

    return fileContent

def showData(df):
    print("\nCi dessous un apercu du dataset:")
    print(df.head())
    rows,columns = df.shape
    print(str(rows) + " lignes et " + str(columns) + " colonnes")

def showNan(df):
    print("\nCi dessous un apercu des données manquantes")
    nanTotal = df.isnull().sum().sum()
    rows,columns = df.shape
    print("\nLe dataset contient " + str(nanTotal) + " données manquantes sur " + str(df.size) + ". Soit un pourcentage de " + str(100*(nanTotal / (rows * columns))))
    print("Ci dessous le nombre de données manquantes par colonnes:")
    colsWithNan = [col for col in df.columns if df[col].isnull().sum() > 0]
    for col in colsWithNan:
        print(col + " : " + str(df[col].isnull().sum()) + " soit un pourcentage de: " + str(100*(df[col].isnull().sum()/rows)))

def showColumn(columnName,df):
    columnData = df[columnName]
    print("\nAffichage de la colonne " + columnName)
    print(columnData.head().to_string(index=True))
    print("...")
    print(columnData.tail().to_string(index=True))

    print("\nDescription statistique de la colonne")
    print(columnData.describe().to_string())

    print("\nNombre de NaN trouvé et index des 5 premiers")
    print(columnData.isnull().sum())
    print(columnData[columnData.isna()].index.tolist()[:5])

def showLine(rowNumber,df):
    rawData = df.iloc[rowNumber]
    print("\nAffichage de la ligne dans son contexte" + str(rowNumber))
    start = max(0,rowNumber-2)
    end = min(len(df),rowNumber+3)
    print(df.iloc[start:end])
    print("\nNombre de NaN dans la ligne et nom des colonnes concernées: ")
    print(rawData.isna().sum())
    print(rawData[rawData.isna()].index.tolist())

def plotCol(columnName,df):
    min_value = df[columnName].min()
    max_value = df[columnName].max()

    plt.hist(df[columnName], bins='auto', range=(min_value, max_value))
    plt.xlabel(columnName)
    plt.ylabel('Frequence')
    plt.title('Histogramme de ' + columnName)
    plt.show()

def findLine(columnName, df, value):
    rowNumber = df.loc[df[columnName] == int(value)].index[0]
    print("La valeur: " + value + " a été trouvée en ligne: " + str(rowNumber))

def checkLineExist(rowNumber,df):
    if rowNumber >= df.shape[0]:
        print("Il n'existe pas de ligne à l'index " + str(rowNumber))
        print("le dernier index du dataset est: " + str(df.shape[0] - 1))
        return False
    else:
        return True

