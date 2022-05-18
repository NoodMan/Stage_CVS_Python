#CODE QUI AFFICHE LIGNE PAR LIGNE sans les 2 premiers lignes
filename = "export_contacts_1652774627_2.csv"
lineCount = 0
with open(filename) as F:
    for line in F:
        if (lineCount >= 2): #pour enlever les deux premiers lignes
           x = line.replace(";", ",") 
           print (x)
            #print(x[1])# me donne uniquement un caractere et non la ligne!!!!
            #print(line)
        lineCount += 1






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







#CODE POUR LIRE UN FICHIER CSV SANS TABLEAU (Me donne uniquement la dernier ligne???What's!!!!!!)
# import csv

# sample_csv = 'export_contacts_1652774627_2.csv'

# with open(sample_csv, "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     count = 0
#     for line in csv_reader:
#        if (count > 0):
#            count +=1
       
# print(line)




#CODE POUR ECRITE MAIS NE FONCTIONNE PAS
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
# from itertools import count


# # fichier à lire en mode r (reading)
# filename = r'export_contacts_1652774627_2.csv'
# data = []  # on déclare un tableau vide pour les datas

# with open(filename) as csvfile:  # on lit le fichier que je renomme avec un alias (as)
#     csvreader = csv.reader(csvfile, delimiter=',')
#     count = 0 # le compteur
#     for row in csvreader:
#         if count > 1: #on ignore les lignes avec le nom du fichier et les entete des colonnes= 1 / juste le nom =0...
#             # if row[0] != ' ':
#             data.append(row)  # on ajoute chaque ligne dans le [] data
#         count += 1 #on incremante de 1

#     for d in data:  # itération via le [] ligne par ligne

#         print(d)  # impression du resultat ligne par ligne
