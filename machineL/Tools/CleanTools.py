import pandas as pd
from machineL.Utils.Lutils import *

def autoDeleteCol(df):
    return df.dropna(axis=1, how='any')


def autoDeleteLine(df):
    return df.dropna(axis=0, how='any')


def deleteCol(columnName, df):
    return df.drop(columns=columnName)


def deleteLine(lineNumber, df):
    return df.drop(index=lineNumber)

def testNumeric(column):
    try:
        pd.to_numeric(column)
        return True
    except ValueError:
        return False

def fixFillCol(columnName, df):
    showColumn(columnName, df)
    print("\nPar quoi voulez vous remplacer les Nan de cette colonne ?")
    userInput = input(":")
    print(str(df[columnName].isnull().sum()) + " NaN sont remplacés par: " + userInput)
    df[columnName].fillna(userInput, inplace=True)
    return df

def meanFillCol(columnName, df):
    mean = df[columnName].mean()
    print(str(df[columnName].isna().sum()) + " NaN sont remplacés par: " + str(mean))
    df[columnName].fillna(mean, inplace=True)
    return df
