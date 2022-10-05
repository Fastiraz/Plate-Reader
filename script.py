import pip
import keyboard
import re
from cProfile import run
from datetime import date
from operator import sub
import os
import sys
import time
import subprocess
from termcolor import colored
#from rich import inspect
import mysql.connector as connector
from mysql.connector import Error
import signal

import string #get string num from db

global dbhost
dbhost = ""
global dbname
dbname = ""
global dbuser
dbuser = ""
global dbpasswd
dbpasswd = ""


def design():
    print("""
    ______________      _____           ________            _________
    ___  __ \__  /_____ __  /_____      ___  __ \__________ ______  /____________
    __  /_/ /_  /_  __ `/  __/  _ \     __  /_/ /  _ \  __ `/  __  /_  _ \_  ___/
    _  ____/_  / / /_/ // /_ /  __/     _  _, _//  __/ /_/ // /_/ / /  __/  /
    /_/     /_/  \__,_/ \__/ \___/      /_/ |_| \___/\__,_/ \__,_/  \___//_/

                            Dev par Léandre Chanzy
    """)

def connection(dbhost, dbname, dbuser, dbpasswd):

    config = {
        "user": "",
        "password": "",
        "host": "localhost",
        "port": 3306,
        "database": "plate"
    }

    try:
        c = connector.connect(**config)
        return c
    except:
        print("Erreur de connection")
        exit(1)


"""def connection(dbhost, dbname, dbuser, dbpasswd):
    config = {
        "user": dbuser,
        "password": dbpasswd,
        "host": dbhost,
        "port": 3306,
        "database": dbname
    }

    try:
        c = connector.connect(**config)
        return c
    except:
        print("connection error")
        exit(1)"""


"""def test1(): #no error method
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM parking;")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)
"""

def dbreadall(dbhost, dbname, dbuser, dbpasswd): #no error method
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM parking;")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)


def dbreadfromplate(dbhost, dbname, dbuser, dbpasswd): #no error method
    plate = input("\n\nEntrer une plaque : \n")
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM parking WHERE plaque = '" + plate + "';")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)


def dbreadfromdate(dbhost, dbname, dbuser, dbpasswd): #no error method
    date = input("\n\nEntrer une date au format [AAAA-MM-JJ] : ")
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM parking WHERE entree = '" + date + "';")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)


def dbreadfromid(dbhost, dbname, dbuser, dbpasswd): #no error method
    sqlid = input("\n\nEntree un id : ")
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM parking WHERE id = " + sqlid + ";")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)

def dbreadplate(dbhost, dbname, dbuser, dbpasswd):
    plate = input("\n\nPlease enter the plate : ")
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT * FROM data WHERE plate = '" + plate + "';")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)


"""def dbinsert():
    today = date.today()
    xdate = today.strftime("%Y/%m/%d")
    print(xdate)
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()
    cur.execute("SELECT MAX(id) FROM data;")
    print(cur.fetchone())
    menu_read_db(dbhost, dbname, dbuser, dbpasswd)
"""

def setupsql(dbhost, dbname, dbuser, dbpasswd):
    print("""\n\n
     ____ ____ ____
    ||S |||Q |||L ||
    ||__|||__|||__||
    |/__\|/__\|/__\|
    """)

    dbhost = input(colored("Host : ", 'yellow', attrs=['bold']))
    dbname = input(colored("Name : ", 'yellow', attrs=['bold']))
    dbuser = input(colored("User : ", 'yellow', attrs=['bold']))
    dbpasswd = input(colored("Password : ", 'yellow', attrs=['bold']))
    connection(dbhost, dbname, dbuser, dbpasswd)
    menu(dbhost, dbname, dbuser, dbpasswd)

"""def VIP(dbhost, dbname, dbuser, dbpasswd, plate):
    cn = connection(dbhost, dbname, dbuser, dbpasswd)
    cur = cn.cursor()

    cur.execute("SELECT id  FROM vip WHERE plaque = '" + plate + "';")
    print("SELECT id  FROM vip WHERE plaque = '" + plate + "';")
    num = cur.fetchone()
    print(num[0])
    if num[0] != 0:
        return
    else:
        print(colored("Accès autorisé", 'green', attrs=['bold']))
        menu(dbhost, dbname, dbuser, dbpasswd)
"""
def entree(dbhost, dbname, dbuser, dbpasswd):
        with open('/var/log/alpr.log', 'w'): #ouverture du fichier alpr.log en mode ouverture pour supprimer son contenue
                pass#stop de la manipulation du fichier

        temps = time.strftime('%Y-%m-%d %H:%M:%S')#On stock dans la variable 'temps' la date et l'heure actuelle

        os.system('timeout 10s alprd -f')#On execute sur le terminale la cmd 'alprd -f' durant 10s
        time.sleep(10)#arret du programme pendant 10s

        logfile = open('/var/log/alpr.log', 'r')#on ouvre le fichier alpr.log en mode lecture
        lines = logfile.readlines()#on lit le fichier ligne par ligne

        for line in lines:# dans une boucle for
                if 'plate' in line:# si 'plate' est trouver dans la ligne
                        platetab = line.split() #chaque mot de la ligne sont stocker dans la case d'un tableau

        logfile.close() #on ferme le fichier

        print(platetab[4])# on affiche la plaque stocker dans la 5 case du tableau 'platetab'

        """VIP(dbhost, dbname, dbuser, dbpasswd, platetab[4])"""

        cn = connection(dbhost, dbname, dbuser, dbpasswd)#on se connecte a la base de données
        cur = cn.cursor()#on navigue dans la base de données

        sqlentree = "INSERT INTO parking (plaque, entree) VALUES ('" + platetab[4] + "', '" + str(temps) + "');"
        #on stock dans la variable 'sqlentree' la requete sql permettent l'envoie de donnée dans la table parking
        print(sqlentree)#on affiche la requete
        cur.execute(sqlentree)#on execute la requete
        cn.commit()#on confirme la modification de la table

        print(colored("Accès autorisé", 'green', attrs=['bold'])) #on affiche 'acces autorisé'

        with open('/var/log/alpr.log', 'w'):#ouverture du fichier alpr.log en mode ouverture pour supprimer son contenue
                pass#stop de la manipulation du fichier

        main(dbhost, dbname, dbuser, dbpasswd)#retour au menu


def sortie(dbhost, dbname, dbuser, dbpasswd):
        with open('/var/log/alpr.log', 'w'):#ouverture du fichier alpr.log en mode ouverture pour supprimer son contenue
                pass#stop de la manipulation du fichier

        temps = time.strftime('%Y-%m-%d %H:%M:%S')#On stock dans la variable 'temps' la date et l'heure actuelle

        os.system('timeout 10s alprd -f')#On execute sur le terminale la cmd 'alprd -f' durant 10s
        time.sleep(10)#arret du programme pendant 10s

        logfile = open('/var/log/alpr.log', 'r')#on ouvre le fichier alpr.log en mode lecture
        lines = logfile.readlines()#on lit le fichier ligne par ligne

        for line in lines:# dans une boucle for
                if 'plate' in line:# si 'plate' est trouver dans la ligne
                        platetab = line.split() #chaque mot de la ligne sont stocker dans la case d'un tableau

        logfile.close() #on ferme le fichier
        print(platetab[4]) # on affiche la plaque stocker dans la 5 case du tableau 'platetab'

        cn = connection(dbhost, dbname, dbuser, dbpasswd)#on se connecte a la base de données
        cur = cn.cursor()#on navigue dans la base de données

        cur.execute("SELECT id FROM parking WHERE plaque = '" + platetab[4] +"';")# on execute la requete qui permet de trouver l'id correspondant a la plaque
        print("SELECT id FROM parking WHERE plaque = '" + platetab[4] +"';")# on affiche la requete
        vehiculeid = cur.fetchone()#on stock le resultat de la requete dans la variable 'vehiculeid'
        idnum = list(vehiculeid)#on stock dans un tableau 'idnum' le resultat de la requete
        print(idnum)#j'affiche la valeur du tableau

        cn = connection(dbhost, dbname, dbuser, dbpasswd)#on se connecte a la base de données
        cur = cn.cursor()#on navigue dans la base de données

        print("UPDATE parking set sortie = '"+ str(temps) +"' WHERE id = '"+ str(idnum[0]) +"';")
        #j'affiche la requete qui permet de modifié la date de sortie de l'id de la plaque scanner
        cur.execute("UPDATE parking set sortie = '"+ str(temps) +"' WHERE id = '"+ str(idnum[0]) +"';")#j'execute la requete
        cn.commit()#on confirme la modification de la table

        cn = connection(dbhost, dbname, dbuser, dbpasswd)#on se connecte a la base de données
        cur = cn.cursor()#on navigue dans la base de données

        print("SELECT entree FROM parking WHERE id = '"+ str(idnum[0]) +"';")
        #j'affiche la date et l'heure d'entree correspondant a l'id de la plaque scanner
        cur.execute("SELECT entree FROM parking WHERE id = '"+ str(idnum[0]) +"';")#j'execute la requete
        horaire = cur.fetchone()#je stock le resultat dans la variable 'horaire'
        print(horaire[0])#j'affiche la date

        cn = connection(dbhost, dbname, dbuser, dbpasswd)#on se connecte a la base de données
        cur = cn.cursor()#on navigue dans la base de données

        print("SELECT TIMESTAMPDIFF (minute, '"+ str(horaire[0]) + "', '"+ str(temps) +"');")
        #j'affiche la requete permettant de calculer la difference entre les deux dates en minutes
        cur.execute("SELECT TIMESTAMPDIFF (minute, '"+ str(horaire[0]) + "', '"+ str(temps) +"');")
        duree = cur.fetchone()#je stock le resultat de la requete dans la variable 'duree'
        print(""+str(duree[0])+" minutes")#j'affiche la duree

        print("UPDATE parking set duree = '"+ str(duree[0]) +"' WHERE id = '"+ str(idnum[0]) +"';")
        #j'affiche la requete qui permet de modifié la date de sortie de l'id de la plaque scanner
        cur.execute("UPDATE parking set duree = '"+ str(duree[0]) +"' WHERE id = '"+ str(idnum[0]) +"';")#j'execute la requete
        cn.commit()#on confirme la modification de la table

        print(colored("Accès autorisé", 'green', attrs=['bold']))#j'affiche acces autorisé

        with open('/var/log/alpr.log', 'w'):#j'ouvre le fichier en mode ecriture pour supprimer son contenu
                pass#je stop le processus

        main(dbhost, dbname, dbuser, dbpasswd)# retour au menu


def menu(dbhost, dbname, dbuser, dbpasswd):#fonction menu
    tab_num_menu = ["\n\n[0] ", "[1] ", "[2] ", "[3] ", "[x] "]#tableazu avec le numero des option
    tab_option = ["- Parametrer la Base de données", "- Entree", "- Sortie", "- Lire la Base de données", "- Quitter"]#tableau avec le nom des option

    for i in range(5):#boucle permettant l'affichage des numero d'option et l'option
        print(colored(tab_num_menu[i], 'magenta', attrs=['bold']), colored(tab_option[i]))

    reponse = input("\nChoisir une option -> ")#récupérer dans la variable reponse la valeur saisir par l'utilisateur

    if reponse == "0":#si la valeur de reponse est '0' alors lancer la fonction 'setupsql'
        setupsql(dbhost, dbname, dbuser, dbpasswd)
    elif reponse =="1":
        entree(dbhost, dbname, dbuser, dbpasswd)
    elif reponse =="2":
        sortie(dbhost, dbname, dbuser, dbpasswd)
    elif reponse == "3":
        menu_read_db(dbhost, dbname, dbuser, dbpasswd)
    elif reponse == "x":
        exit()
    else:
        print(colored("Choisissez une option existante !!!", 'red', attrs=['bold']))
        menu(dbhost, dbname, dbuser, dbpasswd)


def main(dbhost, dbname, dbuser, dbpasswd):#fonction principale
    design()#lancement de la fonction design qui affiche la bannière
    menu(dbhost, dbname, dbuser, dbpasswd)#lancement de la fonction 'menu' qui affiche le menu


def menu_read_db(dbhost, dbname, dbuser, dbpasswd):
    tab_num_menu = ["\n\n[0] ", "[1] ", "[2] ", "[3] ", "[x] "]
    tab_option = ["- Tout afficher", "- Afficher en fonction date ", "- Afficher en fonction de l'ID", "- Afficher en fonction de la plaque", "- Quitter"]

    for i in range(5):
        print(colored(tab_num_menu[i], 'magenta', attrs=['bold']), colored(tab_option[i]))

    reponse = input("\nChoisir une option -> ")

    if reponse == "0":
        #dbreadfromplate()
        dbreadall(dbhost, dbname, dbuser, dbpasswd)
    elif reponse =="1":
        dbreadfromdate(dbhost, dbname, dbuser, dbpasswd)
    elif reponse == "2":
        dbreadfromid(dbhost, dbname, dbuser, dbpasswd)
    elif reponse == "3":
        dbreadplate(dbhost, dbname, dbuser, dbpasswd)
    elif reponse == "x":
        #dbinsert(dbhost, dbname, dbuser, dbpasswd)
        exit()
    else:
        print(colored("Choisissez une option existante !!!", 'red', attrs=['bold']))
        menu_read_db(dbhost, dbname, dbuser, dbpasswd)


if __name__=='__main__':
    main(dbhost, dbname, dbuser, dbpasswd)
