import random
print("Estoy escapando de los dibujitos kagones y encuentro 2 lugares para esconderme: \n" 
      "1 - una puerta semiabierta \n"
      "2 - una escotilla \n"
      "escage rápido mrda.... xd")
    
rama= input()
if rama == "1" or rama =="2":
    if rama == "1":
        print ("abre la puerta semiabierta y entras vas caminando por ahi cuando de repente.. \n"
               " aparece la Beba y te dice dejame mid o te enfrio xd tienes 2 opciones \n"
               "1 - le dices aea sin vida \n"
               "2 - a los lejos ves una puerta oscura corres hacia ella para salvar tu vida de la bebalaria")
        rama1p1=input()
        if rama1p1 == "1" or rama1p1 =="2":
            if rama1p1 =="1":
                print("no hiciste caso a las amenzas de la beba y te contagio su fracaso y bebalaria gaaa.. \n"
                      "terrible morir con la bebalaria no c lo deseio a nadie xd :V ")
            if rama1p1 =="2":
                print("Entras a esa puerta fea y alucinas voces de los dibujitos.. \n"
                      "a los lejos ves una luz vas hacia ahi y era la salida  FIN...    ")

               
    if rama =="2":
        print ("entras a la escotilla y esta todo oscuro hasta q ves un poco de luz.... \n"
               "y ves q ahi hay un palo de 1mt xd lo coges?  \n"
               "1 - si.. tengo que defenderme con esto de los dibujitos \n"
               "2 - no.. siempre parador nunca correlon xd")
        rama2p1=input()
        palo=bool
        if rama2p1 == "1" or rama2p1 =="2":
            if rama2p1 =="1":
                print("congiste el palo ahora te sientes mas parador.... \n"
                      "vengan p ctrmes!!")
                palo = True
            if rama2p1 =="2":
                print("yo no le tengo miedo a esos dibujitos fracasados.... \n"
                      "aea les wa decir gaaa!!")
                palo = False
        print ("sigues caminando dentro de esa escotilla oscura y te encuentras con la rata de kkrius.. \n"
               "le dices safa rata e mrd.... entonces la rata t pone a prueba..\n"
               "1 - te reta una multiplicacion pa su nivel xd.. aceptas? \n"
               "2 - safa y rebajate a su nivel de esa kk...")
        rama2p2=input()
        if rama2p2 == "1" or rama2p2 =="2":
            if rama2p2 =="1":
                pruebarata=random.randint(1,12)
                print("el rata kkrius te pregunta cuanto es?.... \n"
                      "13*",pruebarata)
                legal=13*pruebarata
                mirpta=int(input())
                if mirpta == legal:
                    print("a pesar de decir la respuesta correcta...la rata te dice OK terna nada mas.. xd y sigues con tu camino")
                    print("sigues avanzando y esuchas bulla.. te acercas y resulta q los dibujitos tumbaron la salida..\n"
                    "que harias?.. \n"
                    "1 - recuerdas que cogiste el palo.. y empiezas a abrirte el paso\n"
                    "2 - recuerdas q no cogiste el palo x confiarte en q eres parador")
                    rama3p2=input("escoge rapido q los dibujitos estan enfriando a todos..")
                    if rama3p2 == "1" and palo:
                        print("te abres paso entre los escombros y escapas de ese lugar de ediondos chapas tu taxi y safas.. fin")
                    elif rama3p2 =="2" and palo == False:
                        print ("x confiado no puedes mover los escombros buscas desesperado otro camino y los dibujitos te ecnuentran y te enfrian finnn...")
                    else:
                        print("no cogiste el palo asi q te mueres encerrado ahi finn")
                else:
                    print("la rata te dice la rpta es..: ",legal ,"fallaste eres un fracasado mas... lo ignoras y sigues tu camino y mueres x los dibujitos q estaban por ahi fin...")
            
            if rama2p2 =="2":
                print("lo ignoras y sigues tu camino como fracasasdo xd....\n"
                    "estas avanzando de repente aparecen muchos dibujitos y te enfrian... FIN")
                
else:
    print("solo puedes seleccionar una de esas opciones gaaa")
