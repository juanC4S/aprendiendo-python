import random
import os
cpu = random.randint(1,3)

atk=0

print ("BIENVENIDOS A LA BATALLA PÓKEMON")
menu= None
escoger=None
i = input("1 - Empezar juego \n"
          "2 - Salir \n"
          )
if i=="1":
    prata=100
    ptortuga=100
    # lifeptortuga=float((ptortuga/10))*"-"
    while prata > 0 and ptortuga >0 :
        print ("Turno de PIKACHU y estas vs SQUIRTLE \n")
        opc =input("Los ataques PIKACHU son: \n"
                "1 - impactrueno daño   Daño = 15 \n"
                "2 - bola de rayo daño  Daño = 18 \n"
                "3 - rayos lokosxd daño Daño = 23 \n"
                )  
        
        if opc == "1" :             
            print ("PIKACHU usa impactrueno contra squirtle\n")
            atk = 15
            ptortuga -=atk
                    
            
        elif opc == "2":
            print ("PIKACHU usa bola de rayo contra squirtle\n")
            atk = 18
            ptortuga -=atk
            
        elif opc == "3":
            print ("PIKACHU usa rayos lokos contra squirtle\n")
            atk = 23
            ptortuga -=atk
        if opc=="n" or "N":
             print ("PIKACHU A DECIDIDO NO ATACAR \n")
                
           
        if prata<0:
             prata=0
        if ptortuga<0:
             ptortuga=0
        
        dañoprogres=prata/10
       
        lifepoker = int(dañoprogres % 10) * "-"
        barritat = ptortuga/10
        
        lifepoket = int(barritat %10)* "-"
        if prata >=100:
            aea = 10 *"-"
            print ("vida de pikachu es:  " ,prata ,"/100" ,aea)
        else:
            print ("vida de pikachu es:  " ,prata,"/100",lifepoker)
            
        if ptortuga >=100:
            print ("vida de squirtle es: " ,ptortuga,"/100" ,aea ,"\n")
        else:    
            print ("vida de squirtle es: " ,ptortuga,"/100" ,lifepoket,"\n") 
           
                
        #os.system("cls")

        print ("Turno de SQUIRTLE (CPU) vs PIKACHU \n")
        print("Los ataques SQUIRTLE (CPU) son: \n"
            "1 - hidrobomba daño    Daño  = 17 \n"
            "2 - burbujas explosivas Daño  = 19 \n"
            "3 - agua venenosa daño  Daño  = 21 \n"
            )        

        if cpu == 1:
                
                print ("SQUIRTLE (CPU) usa hidrobomba contra pikachu\n")
                atk = 17
                prata -=atk
                
        elif cpu == 2:
                
                print ("SQUIRTLE (CPU) usa burbujas explosivas contra pikachu\n")
                atk = 19
                prata -=atk
                
        elif cpu == 3:
            
                print ("SQUIRTLE (CPU) usa agua venenosa contra pikachu\n")
                atk = 21
                prata -=atk 
        
                 
        if prata<0:
             prata=0
        if ptortuga<0:
             ptortuga=0

        dañoprogres=prata/10
       
        lifepoker = int(dañoprogres % 10) * "-"
        barritat = ptortuga/10
        
        lifepoket = int(barritat %10)* "-"
        if prata >=100:
            aea = 10 *"-"
            print ("vida de pikachu es:  " ,prata,"/100" ,aea)
        else:
            print ("vida de pikachu es:  " ,prata,"/100" ,lifepoker)
           
                        
        if ptortuga >=100:
            print ("vida de squirtle es: " ,ptortuga,"/100" ,aea ,"\n")
        else:    
            print ("vida de squirtle es: " ,ptortuga,"/100" ,lifepoket,"\n") 
           
                
       
    if prata > ptortuga:
        print ("SQUIRTLE NO PUEDE SEGUIR")
        print ("el ganador es pikachu")
    else:
        print("PIKACHU NO PUEDE SEGUIR")
        print ("el ganador es squirtle")  
    
else:
    print ("saliendo del juego...")
    quit()

    



