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
# filename_n = r'Contact_python.csv'
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
# sortie = pandas.read_csv('Contact_python.csv', usecols=['Rue']) 
# print(sortie)

#CODE POUR METTRE UN SEPARATEUR ENTRE LES VALEURS MAIS NE FONCTIONNE PAS
# import pandas
# sortie = pandas.read_csv('Contact_python.csv', sep='#',)
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

#CODE POUR MINI API QUI DONNE UN FRUIT AU HASARD A CHAQUE REACTIALISATION
from crypt import methods
from flask import Flask
import json
import random
from pip import main

app = Flask(__name__)
@app.route("/get-fruit", methods=['GET'])

def getFruit():
    
    listFruit = ['apple', 'orange', 'banana']
    choiseFruit = listFruit[random.randint(0, 2)]
    
    return json.dumps({"fruit": choiseFruit})

if __name__ == '__main__':
    app.run(debug=True)
    print("api Start !")
    
    
#CODE POUR ECRIR TON NOM ET AGE DANS URL DU NAVIGATEUR   
# from crypt import methods
# from flask import Flask
# import json
# import random

# from pip import main

# app = Flask(__name__)

# @app.route("/get/<name>/<years>", methods=['GET'])

# def getInfo(name, years):
#     return "tu t'appelle " + name + " et tu as " + years

# if __name__ == '__main__':
#     app.run(debug=True)
#     print("api Start !")
    

# from crypt import methods
# from flask import Flask, request
# import json
# import requests

# app = Flask(__name__)

# playerList = []

# @app.route('/add-player', methods=['POST'])
# def addPlayer():
#     data = request.get_json()
#     if "Username" in data : 
#         playerList.append(data["Username"])
#         return"Created !", 200
#     else: 
#         return 'Bad request', 400

# if __name__ == '__main__':
#     app.run(debug=True)
 
