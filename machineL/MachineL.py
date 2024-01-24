from machineL.Tools.CleanTools import *
from machineL.Menu.CleanMenu import *

pd.options.display.max_columns = None

print("Assistant de machine learning\n=================")
print("Assurez vous que le fichier est bien présent dans le répertoire ./csvFiles")
#filename = input("Quel est le nom du fichier de données ? \n:")
filename = "melb_data.csv"

print("Le fichier " + filename + " va être traité")

# Ouverture
data = openFile(filename)

# Nettoyage
cleanedData = cleanDataMenu(data)

# Formatage

