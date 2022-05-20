# CODE QUI AFFICHE LIGNE PAR LIGNE sans les 2 premiers lignes
# import csv
# filename = "export_contacts_1652774627_2.csv"
# lineCount = 0
# with open(filename) as F:
#     for line in F:
#         if (lineCount >= 2): #pour enlever les deux premiers lignes
#            x = line.replace(";", ",")
#            print (x)
#             #print(x[1])# me donne uniquement un caractere et non la ligne!!!!
#             #print(line)
#         lineCount += 1


# # CODE TEST CONVERSION EN INT (ECHEC)
# import csv # on import csv
# from itertools import count

# # fichier à lire en mode r (reading)
# filename = r'export_contacts_1652774627_2.csv'
# data = []  # on déclare un tableau vide pour les datas

# with open(filename) as csvfile:  # on lit le fichier que je renomme avec un alias (as)
#     csvreader = csv.reader(csvfile, delimiter=',')
#     count = 0
#     for row in csvreader:
#         if count > 0:
#             # if row[0] != ' ':
#             data.append([
#                 int(row[0]),
#                 int(row[1]),
#                 int(row[2]),
#                 int(row[3]),

#             ])  # on ajoute chaque ligne dans le [] data
#         count += 1

# for d in data:  # itération via le [] ligne par ligne

#     print(d)  # impression du resultat ligne par ligne


# CODE POUR LIRE UN FICHIER CSV SANS TABLEAU (Me donne uniquement la dernier ligne???What's!!!!!!)
# import csv

# sample_csv = 'export_contacts_1652774627_2.csv'

# with open(sample_csv, "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     count = 0
#     for line in csv_reader:
#        if (count > 0):
#            count +=1

# print(line)


# CODE POUR ECRITE MAIS NE FONCTIONNE PAS
# import csv

# sample_csv = 'export_contacts_1652774627_2.csv'

# with open(sample_csv, "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print("{name} habite {Address}"
#               .format(name=line["Société"],
#                       Address=line['Rue'],
#                       ))


# CODE POUR LIRE ET IGNORER LES DEUX PERMIERE LIGNES (FONCTIONNE 🎉)
# import csv # on import csv

# # fichier à lire en mode r (reading)
# filename_o = r'export_contacts_1652774627_2.csv'
# # filename_n = r'Test_python.csv'
# data = []  # on déclare une liste vide pour les datas

# with open(filename_o) as csvfile:  # on lit le fichier que je renomme avec un alias (as)
#     csvreader = csv.reader(csvfile)
#     count = 0 # le compteur
#     for row in csvreader:

#         if count > 1: #on ignore les lignes avec le nom du fichier et les entete des colonnes= 1 / juste le nom =0...
#             # if row[0] != ' ':
#             data.append(row)  # on ajoute chaque ligne dans le [] data
#         count += 1 #on incremante de 1

#     for d in data:  # itération via le [] ligne par ligne

#         print(d)  # impression du resultat ligne par ligne

# with open(filename_n) as csvfile:
#     csvreader = csv.reader(csvfile)
#     count = 0
#     for row in csvreader:

#         if count > 1:
#             data.append(row)
#         count += 1

#     for d in data:

#         print(d)

# import csv

# data = {}

# with open('export_contacts_1652774627_2.csv') as csv_file:
    
#     csv_reader = csv.DictReader(csv_file, delimiter=',') # delimiter ne fonctionne pas
#     count = 0
#     for row in csv_reader:
#         if count > 1: #pour ignorer le titre du fichier sinon le titre se repete a chaque tour de boucle
#             count += 1
#         print(row['Société']) # recherche par valeur, ne fonctionne pas j'ai pas uniqument les noms des sociéte qui resortent???


# import csv

# data = {}

# with open('export_contacts_1652774627_2.csv') as csv_file:
    
#     csv_reader = csv.DictReader(csv_file, delimiter=',') # delimiter ne fonctionne pas
  
#     for row in csv_reader:
    
      
#         print(row['Société']) 
        



#CODE POUR LIRE UN FICHIER CSV SANS LE TITRE (SANS COUNT)
# import pandas
# lire = pandas.read_csv(r"Contact_python.csv")
# print(lire)

# import csv
# reader = csv.DictReader(open(r"Contact_python.csv"))
# for raw in reader:
#     print(raw)


#CODE POUR FAIRE UNE RECHERCHE PAR VALEUR NE FONCTIONNE PAS        
# import pandas
# sortie = pandas.read_csv('Test_python.csv', usecols=['Rue']) 
# print(sortie)

#CODE POUR METTRE UN SEPARATEUR ENTRE LES VALEURS MAIS NE FONCTIONNE PAS
# import pandas
# sortie = pandas.read_csv('Test_python.csv', sep='#',)
# print(sortie)

#CODE POUR CHANGER LES CLES (ENTETE) ne fonctionne pas
# import pandas as pd
# df = pd.read_csv("export_contacts_1652774627_2.csv",skiprows=1) # a utiliser pour ignore la premier ligne (titre du fichier)
# #df = pd.read_csv("export_contacts_1652774627_2.csv") # pour afficher tout
# correct_df = df.copy()
# correct_df.rename(columns={'Id de la société': 'Id société', 'Société': 'Société','Rue': 'Rue','Code postal': 'Code postal','Ville': 'Ville'}, inplace=True)
# print(correct_df)
# #Exporting to CSV file
# correct_df.to_csv(r'Contact_python.csv', index=False,header=True)






#CODE TEST FUSION ENTRE DEUX FICHIER CSV ECHEC!!

#import pandas as pd

# # set files path
# sales1 = "Test_CSV_Python/export_contacts_1652774627_2.csv"
# sales2 = "Test_CSV_Python/Test_python.csv"

# print("*** Merging multiple csv files into a single pandas dataframe ***")

# # merge files
# dataFrame = pd.concat(
#    map(pd.read_csv, [sales1, sales2]), ignore_index=True)
# print(dataFrame)


# import pandas as pd
  
# # merging two csv files
# df = pd.concat(
#     map(pd.read_csv, ['Test_CSV_Python/export_contacts_1652774627_2.csv', 'Test_CSV_Python/Test_python.csv']), ignore_index=True)
# print(df) 


# import pandas as pd

# a = pd.read_csv ('Test_CSV_Python/export_contacts_1652774627_2.csv')
# b = pd.read_csv ('Test_CSV_Python/Test_python.csv')
# b = b.dropna(axis=1)
# merged = a.merge(b, on='title')
# merged.to_csv("output.csv", index=False)

# import glob

# interesting_files = glob.glob("*.csv") 

# header_saved = False
# with open('export_contacts_1652774627_2.csv','Test_python.csv') as fout:
#     for filename in interesting_files:
#         with open(filename) as fin:
#             header = next(fin)
#             if not header_saved:
#                 fout.write(header)
#                 header_saved = True
#             for line in fin:
#                 fout.write(line)

from datetime import datetime
import json
import requests
import sys
import os
import csv

response = r'export_contacts_1652774627_2.csv'
stats = json.loads(response)

stats = list(stats)

newObject = {
    "Id de la société": 'int',
    "Société": "string",
    "Rue": "string",
    "Code postal": "int",
    "Ville": "string",
    "Pays": "string",
    "Siret": "int",
    "TVA intracommunautaire": "int",
    "Code tier": "int",
    "Langue": "string",
    "Commentaires": "string",
    "Catègories": "string",
    "Statut client": "string",
    "Statut prospect": "string", 
    "Commercial responsable": "string", 
    "Identifiant du contact" :"int", 
    "Civilitè": "string",
    "Prènom du contact":"string",
    "Nom du contact" :"string",
    "Email du contact" : "string",
    "Tèlèphone fixe":"int", 
    "Tèlèphone portable": "int", 
    "Poste/job du contact":"string", 
    "funnelStep":"string", 
    "facebook":"string", 
    "turnover":"int", 
    "turnoverThisYear":"int", 
    "creationDate":"int", 
    "firstInvoiceDate":"int"  
}

listOfLineToModify = list()

for _obj in stats:
    with open("export_contacts_1652774627_2.csv", 'r') as csv_file:
        lines = csv.reader(csv_file, delimiter=';')

        for index, row in enumerate(lines):
            if index < 1:
                continue

            if int(_obj["id"]) == int(row[0]):
                newObject["Id de la société"] = _obj["Id de la société"]
                newObject["Société"] = row[1]
                newObject["Rue"] = row[2]
                newObject["Code postal"] = row[3]
                newObject["Ville"] = row[4]
                newObject["Pays"] = row[5]
                newObject["Siret"] = row[6]
                newObject["TVA intracommunautaire"] = row[7]
                newObject["Code tier"] = row[8]
                newObject["Langue"] = row[9]
                newObject["Commentaires"] = row[10]
                newObject["Catègories"] = row[11]
                newObject["Statut client"] = row[12]
                newObject["Statut prospect"] = row[13]
                newObject["Statut fournisseur"] = row[14]
                newObject["Commercial responsable"] = row[15]
                newObject["Identifiant du contact"] = row[16]
                newObject["Civilitè"] = row[17]
                newObject["Prènom du contact"] = row[18]
                newObject["Nom du contact"] = row[19]
                newObject["Email du contact"] = row[20]
                newObject["Tèlèphone fixe"] = row[21]
                newObject["Tèlèphone portable"] = row[22]
                newObject["Poste/job du contact"] = row[23]
                newObject["funnelStep"] = row[24]
                newObject["facebook"] = row[25]
                newObject["turnover"] = row[26]
                newObject["turnoverThisYear"] = row[27]
                newObject["creationDate"] = row[28]
                newObject["firstInvoiceDate"] = row[29]
                
                listOfLineToModify.append(newObject)


print("listOfLineToModify ====> {} ".format(listOfLineToModify))

for newObject in listOfLineToModify:
    print("newObject {}".format(newObject))
    response = requests.patch(
        "Test_python.csv"+str(newObject["id"]), json=newObject)
  
    print("\n")
    print("response {}".format(response))

