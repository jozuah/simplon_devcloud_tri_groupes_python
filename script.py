#!/usr/bin/env python3

import random

import logging

import json
 
from logging.handlers import RotatingFileHandler
 
# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(logging.DEBUG)
 
# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('log.txt', 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Start log")
''' 
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
'''

### Ecrire un fichier log.txt qui va donner 
# un rapport de chaque opération + l'heure d'execution de l'action
# ecrire les groupes dans un json si je ne sais pas faire : un .txt simple
# appeller mon script avec un nom custom, python xxx.py => repartition_groupe (partager) packages 

### Petit script pour effacer mon .json systématiquement avant d'écrire dedans
# open file  
my_jason_file = open("repartition.json", "r+")    
# to erase all data  
my_jason_file.truncate() 
# to close file
my_jason_file.close() 

### Faire un clear de mon fichier log.txt ?


### Ouverture de mon fichier groupe,
# je récupère tous les noms situés dans la 1ère ligne
#dans la variable names_txt, c'est une longue string
fo = open ('groupes.txt','r')
names_txt = fo.readline()
logger.info(names_txt) #check que j'ai bien récup le texte dans le fichier externe
names = names_txt.split() # Conversion string en list
logger.info(names)

#NE PAS OUBLIER DE FERMER LE .TXT

### On peut ajouter un try/except si fichier vide

max_nb_groups = int(input("Nombre de personne par groupe:"))
logger.info(max_nb_groups)
selected = []
i = 0
my_dict={}

while (len(names) > max_nb_groups):
    
    i=i+1
    selected = random.sample(names, k= max_nb_groups)
    
    print("GROUP #%s :\n %s\n" % (i, selected))
    logger.info(selected) # check les groupes se forment
    my_dict[i] = selected
    logger.info(my_dict) # check de l'update de mon dict

    for sel in selected:
        names.remove(sel)
    
print("GROUP #%s :\n %s\n" % (i+1, names))
my_dict[i+1] = names

with open('repartition.json', 'a+') as outfile: # Se ferme automatiquement avec with
    json.dump(my_dict, outfile, indent=4)

logger.info("End Log")

