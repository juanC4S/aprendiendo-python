import os
import random
import readchar

pos_x = 0
pos_y = 1

num_of_map_objects = 4

obstacle_definition = """\
##########################
########          ########
########          ########
########          ########
########          ########
#                        #
#                        #
#                        #
#                        #
#                        #
#########         ########
#########         ########
#########         ########
#########         ########
##########################\
"""

my_position = [13, 1]

map_objects = []
generated_objects = 0  # contador de objetos generados al inicio

#create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)

# generar objetos aleatorios
while generated_objects < num_of_map_objects:
    new_position = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]
    if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
        map_objects.append(new_position)
        generated_objects += 1

for cantireal in map_objects:
    cantireal= list(map_objects)

end_game = False
died = False
#main lopp
while not end_game:
    os.system("cls")
    
    # Draw Map
    print("+" + "-" * map_width *2 + "+")
    for coordinate_y in range(map_height):
        print("|", end="")
        for coordinate_x in range(map_width):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object
                    
            if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell == cantireal[0]:
                    
                    # map_objects.remove(object_in_cell)
                    # tail_lengt += 1
                    # question = readchar.readkey()
                    print ("PELEA DE INVALIDOS!!!")
                    print ("Un RAICHU salvaje aparecio! ¡Preparate para la batalla!!")
                    ##zona de duelos
                    # os.system("cls")
                    question =input("Deseas enfrentare a RAICHU? q/n: ")
                    if question =="q":
                        duelo1 = True
                        if duelo1:
                            print ("Esta mrda funciona!! :V ")
                            cpu = random.randint(1 ,3)
                            atk= 0
                            print("Tu pokemon es PIKACHU y tu oponente es RAICHU \n")
                            lifepikachu=100
                            liferaichu=100
                            while lifepikachu > 0 and liferaichu > 0:
                                opcion = input("PIKACHU usa: \n"
                                    "1 - Impactrueno \n"
                                    "2 - Gruñido Growl \n"
                                    "3 - Ataque Rápido \n"        
                                            )
                                if opcion == "1" :             
                                    print ("PIKACHU usa Impactrueno contra RAICHU\n")
                                    atk = 15
                                    liferaichu -=atk
                            
                    
                                elif opcion == "2":
                                    print ("PIKACHU usa Gruñido Growl contra RAICHU\n")
                                    atk = 18
                                    liferaichu -=atk
                    
                                elif opcion == "3":
                                    print ("PIKACHU usa Ataque Rápido contra RAICHU\n")
                                    atk = 23
                                    liferaichu -=atk
                                if opcion== "n" or "N":
                                    print ("PIKACHU A DECIDIDO NO ATACAR \n")
                        
                
                                if lifepikachu<0:
                                    lifepikachu=0
                                if liferaichu<0:
                                    liferaichu=0
                
                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraRaichu = liferaichu/10
                                lifepokemonR= int(barraRaichu %10)* "-"
                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de PIKACHU es:  " ,lifepikachu ,"/100" ,aea)
                                else:
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100",lifepokemonP)
                    
                                if liferaichu >=100:
                                    print ("vida de RAICHU es: " ,liferaichu,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de RAICHU es: " ,liferaichu,"/100" ,lifepokemonR,"\n")
                                
                            

                                

                                print ("Turno de RAICHU (CPU) vs PIKACHU \n")
                                print("Los ataques Raichu (CPU) son: \n"
                                    "1 - Electricidad estática   Daño  = 17 \n"
                                    "2 - Pararrayos              Daño  = 19 \n"
                                    "3 - Bolatrueno              Daño  = 21 \n"
                                    )        

                                if cpu == 1:     
                                    print ("RAICHU (CPU) usa Electricidad estática contra PIKACHU\n")
                                    atk = 17
                                    lifepikachu -=atk
                        
                                elif cpu == 2:   
                                    print ("RAICHU (CPU) usa Pararrayos contra PIKACHU\n")
                                    atk = 19
                                    lifepikachu -=atk
                        
                                elif cpu == 3:               
                                    print ("RAICHU (CPU) usa Bolatrueno contra PIKACHU\n")
                                    atk = 21
                                    lifepikachu -=atk 
                
                        
                                if lifepikachu<0:
                                    lifepikachu=0
                                if liferaichu<0:
                                    liferaichu=0

                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraRaichu = liferaichu/10
                                lifepokemonR = int(liferaichu %10)* "-"

                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,aea)
                                else:
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,lifepokemonP)
                
                                
                                if liferaichu >=100:
                                    print ("vida de RAICHU es: " ,liferaichu,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de RAICHU es: " ,liferaichu,"/100" ,lifepokemonR,"\n")
            
                            if lifepikachu > liferaichu:
                                print ("Raichu [NO PUEDE SEGUIR]")
                                print ("el ganador es PIKACHU")
                                map_objects.remove(object_in_cell)
                            else:
                                print("Pikachu [NO PUEDE SEGUIR]")
                                print ("el ganador es RAICHU")
                                
                                
                            #tail_lengt += 1
                    elif question == "n":
                        continue
                    continue

                if object_in_cell == cantireal[1]:

                    print ("PELEA DE INVALIDOS!!!")
                    print ("Un CHARIZARD salvaje aparecio! ¡Preparate para la batalla!!")
                    question =input("Deseas enfrentare a CHARIZARD? q/n: ")
                    if question =="q":
                        duelo2 = True
                        if duelo2:
                            print ("fuciona esta webd nunca dude")
                            cpu = random.randint(1 ,3)
                            atk= 0
                            print("Tu pokemon es PIKACHU y tu oponente es CHARIZARD \n")
                            lifepikachu=100
                            lifecharizard=100
                            while lifepikachu > 0 and lifecharizard > 0:
                                opcion = input("PIKACHU usa: \n"
                                    "1 - Impactrueno \n"
                                    "2 - Gruñido Growl \n"
                                    "3 - Ataque Rápido \n"        
                                            )
                                if opcion == "1" :             
                                    print ("PIKACHU usa Impactrueno contra CHARIZARD\n")
                                    atk = 15
                                    lifecharizard -=atk
                            
                    
                                elif opcion == "2":
                                    print ("PIKACHU usa Gruñido Growl contra CHARIZARD\n")
                                    atk = 18
                                    lifecharizard -=atk
                    
                                elif opcion == "3":
                                    print ("PIKACHU usa Ataque Rápido contra CHARIZARD\n")
                                    atk = 23
                                    lifecharizard -=atk
                                if opcion== "n" or "N":
                                    print ("PIKACHU A DECIDIDO NO ATACAR \n")
                        
                
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifecharizard<0:
                                    lifecharizard=0
                
                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraCharizard = lifecharizard/10
                                lifepokemonC= int(barraCharizard %10)* "-"
                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de pikachu es:  " ,lifepikachu ,"/100" ,aea)
                                else:
                                    print ("vida de pikachu es:  " ,lifepikachu,"/100",lifepokemonP)
                    
                                if lifecharizard >=100:
                                    print ("vida de CHARIZARD es: " ,lifecharizard,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de CHARIZARD es: " ,lifecharizard,"/100" ,lifepokemonC,"\n")
                                
                            

                                

                                print ("Turno de CHARIZARD (CPU) vs PIKACHU \n")
                                print("Los ataques CHARIZARD (CPU) son: \n"
                                    "1 - Enfado             Daño  = 12 \n"
                                    "2 - Garra Dragón       Daño  = 18 \n"
                                    "3 - Cola Dragón        Daño  = 26 \n"
                                    )        

                                if cpu == 1:     
                                    print ("CHARIZARD (CPU) usa ENFADO contra PIKACHU\n")
                                    atk = 12
                                    lifepikachu -=atk
                        
                                elif cpu == 2:   
                                    print ("CHARIZARD (CPU) usa GARRA DRAGON contra PIKACHU\n")
                                    atk = 18
                                    lifepikachu -=atk
                        
                                elif cpu == 3:               
                                    print ("CHARIZARD (CPU) usa COLA DRAGON contra PIKACHU\n")
                                    atk = 26
                                    lifepikachu -=atk 
                
                        
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifecharizard<0:
                                    lifecharizard=0

                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraCharizard = lifecharizard/10
                                lifepokemonC = int(lifecharizard %10)* "-"

                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,aea)
                                else:
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,lifepokemonP)
                
                                
                                if lifecharizard >=100:
                                    print ("vida de CHARIZARD es: " ,lifecharizard,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de CHARIZARD es: " ,lifecharizard,"/100" ,lifepokemonC,"\n")
            
                            if lifepikachu > lifecharizard:
                                print ("Charizard [NO PUEDE SEGUIR]")
                                print ("el ganador es PIKACHU")
                                map_objects.remove(object_in_cell)
                            else:
                                print("Pikachu [NO PUEDE SEGUIR]")
                                print ("el ganador es CHARIZARD")
                    elif question == "n":
                        continue
                    continue

                if object_in_cell == cantireal[2]:

                    print ("PELEA DE INVALIDOS!!!")
                    print ("Un SQUIRTLE salvaje aparecio! ¡Preparate para la batalla!!")
                    question =input("Deseas enfrentare a SQUIRTLE? q/n: ")
                    if question =="q":
                        duelo3 = True
                        if duelo3:
                            print ("fuciona esta webd nunca dude")
                            cpu = random.randint(1 ,3)
                            atk= 0
                            print("Tu pokemon es PIKACHU y tu oponente es SQUIRTLE \n")
                            lifepikachu=100
                            lifesquirtle=100
                            while lifepikachu > 0 and lifesquirtle > 0:
                                opcion = input("PIKACHU usa: \n"
                                    "1 - Impactrueno \n"
                                    "2 - Gruñido Growl \n"
                                    "3 - Ataque Rápido \n"        
                                            )
                                if opcion == "1" :             
                                    print ("PIKACHU usa Impactrueno contra SQUIRTLE\n")
                                    atk = 15
                                    lifesquirtle -=atk
                            
                    
                                elif opcion == "2":
                                    print ("PIKACHU usa Gruñido Growl contra SQUIRTLE\n")
                                    atk = 18
                                    lifesquirtle -=atk
                    
                                elif opcion == "3":
                                    print ("PIKACHU usa Ataque Rápido contra SQUIRTLE\n")
                                    atk = 23
                                    lifesquirtle -=atk
                                if opcion== "n" or "N":
                                    print ("PIKACHU A DECIDIDO NO ATACAR \n")
                        
                
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifesquirtle<0:
                                    lifesquirtle=0
                
                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraSquirtle = lifesquirtle/10
                                lifepokemonS= int(barraSquirtle %10)* "-"
                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de pikachu es:  " ,lifepikachu ,"/100" ,aea)
                                else:
                                    print ("vida de pikachu es:  " ,lifepikachu,"/100",lifepokemonP)
                    
                                if lifesquirtle >=100:
                                    print ("vida de SQUIRTLE es: " ,lifesquirtle,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de SQUIRTLE es: " ,lifesquirtle,"/100" ,lifepokemonS,"\n")
                                
                            

                                

                                print ("Turno de SQUIRTLE (CPU) vs PIKACHU \n")
                                print("Los ataques SQUIRTLE (CPU) son: \n"
                                    "1 - Placaje            Daño  = 14 \n"
                                    "2 - Burbujas           Daño  = 19 \n"
                                    "3 - Pistola de agua    Daño  = 24 \n"
                                    )        

                                if cpu == 1:     
                                    print ("SQUIRTLE (CPU) usa PLACAJE contra PIKACHU\n")
                                    atk = 14
                                    lifepikachu -=atk
                        
                                elif cpu == 2:   
                                    print ("SQUIRTLE (CPU) usa BURBUJAS contra PIKACHU\n")
                                    atk = 19
                                    lifepikachu -=atk
                        
                                elif cpu == 3:               
                                    print ("SQUIRTLE (CPU) usa PISTLA DE AGUA contra PIKACHU\n")
                                    atk = 24
                                    lifepikachu -=atk 
                
                        
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifesquirtle<0:
                                    lifesquirtle=0

                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraSquirtle = lifesquirtle/10
                                lifepokemonS = int(lifesquirtle %10)* "-"

                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,aea)
                                else:
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,lifepokemonP)
                
                                
                                if lifesquirtle >=100:
                                    print ("vida de SQUIRTLE es: " ,lifesquirtle,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de SQUIRTLE es: " ,lifesquirtle,"/100" ,lifepokemonS,"\n")
            
                            if lifepikachu > lifesquirtle:
                                print ("Squirtle [NO PUEDE SEGUIR]")
                                print ("el ganador es PIKACHU")
                                map_objects.remove(object_in_cell)
                            else:
                                print("Pikachu [NO PUEDE SEGUIR]")
                                print ("el ganador es SQUIRTLE")
                    elif question == "n":
                        continue
                    continue

                if object_in_cell == cantireal[3]:

                    print ("PELEA DE INVALIDOS!!!")
                    print ("Un BOLBASOR salvaje aparecio! ¡Preparate para la batalla!!")
                    question =input("Deseas enfrentare a BOLBASOR? q/n: ")
                    if question =="q":
                        duelo4 = True
                        if duelo4:
                            print ("fuciona esta webd nunca dude")
                            cpu = random.randint(1 ,3)
                            atk= 0
                            print("Tu pokemon es PIKACHU y tu oponente es BOLBASOR \n")
                            lifepikachu=100
                            lifebolbasor=100
                            while lifepikachu > 0 and lifebolbasor > 0:
                                opcion = input("PIKACHU usa: \n"
                                    "1 - Impactrueno \n"
                                    "2 - Gruñido Growl \n"
                                    "3 - Ataque Rápido \n"        
                                            )
                                if opcion == "1" :             
                                    print ("PIKACHU usa Impactrueno contra BOLBASOR\n")
                                    atk = 15
                                    lifebolbasor -=atk
                            
                    
                                elif opcion == "2":
                                    print ("PIKACHU usa Gruñido Growl contra BOLBASOR\n")
                                    atk = 18
                                    lifebolbasor -=atk
                    
                                elif opcion == "3":
                                    print ("PIKACHU usa Ataque Rápido contra BOLBASOR\n")
                                    atk = 23
                                    lifebolbasor -=atk
                                if opcion== "n" or "N":
                                    print ("PIKACHU A DECIDIDO NO ATACAR \n")
                        
                
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifebolbasor<0:
                                    lifebolbasor=0
                
                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraBolbasor = lifebolbasor/10
                                lifepokemonB= int(barraBolbasor %10)* "-"
                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de pikachu es:  " ,lifepikachu ,"/100" ,aea)
                                else:
                                    print ("vida de pikachu es:  " ,lifepikachu,"/100",lifepokemonP)
                    
                                if lifebolbasor >=100:
                                    print ("vida de BOLBASOR es: " ,lifebolbasor,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de BOLBASOR es: " ,lifebolbasor,"/100" ,lifepokemonB,"\n")
                                
                            

                                

                                print ("Turno de BOLBASOR (CPU) vs PIKACHU \n")
                                print("Los ataques BOLBASOR (CPU) son: \n"
                                    "1 - Latigo cepa        Daño  = 17 \n"
                                    "2 - Ataque rapido      Daño  = 21 \n"
                                    "3 - Bomba lodo         Daño  = 27 \n"
                                    )        

                                if cpu == 1:     
                                    print ("SQUIRTLE (CPU) usa LATIGO CEPA contra PIKACHU\n")
                                    atk = 17
                                    lifepikachu -=atk
                        
                                elif cpu == 2:   
                                    print ("SQUIRTLE (CPU) usa ATAQUE RAPIDO contra PIKACHU\n")
                                    atk = 21
                                    lifepikachu -=atk
                        
                                elif cpu == 3:               
                                    print ("SQUIRTLE (CPU) usa BOMBA LODO contra PIKACHU\n")
                                    atk = 27
                                    lifepikachu -=atk 
                
                        
                                if lifepikachu<0:
                                    lifepikachu=0
                                if lifebolbasor<0:
                                    lifebolbasor=0

                                barraPikachu=lifepikachu/10
                                lifepokemonP = int(barraPikachu % 10) * "-"
                                barraBolbasor = lifebolbasor/10
                                lifepokemonB = int(lifebolbasor %10)* "-"

                                if lifepikachu >=100:
                                    aea = 10 *"-"
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,aea)
                                else:
                                    print ("vida de PIKACHU es:  " ,lifepikachu,"/100" ,lifepokemonP)
                
                                
                                if lifebolbasor >=100:
                                    print ("vida de BOLBASOR es: " ,lifebolbasor,"/100" ,aea ,"\n")
                                else:    
                                    print ("vida de BOLBASOR es: " ,lifebolbasor,"/100" ,lifepokemonB,"\n")
            
                            if lifepikachu > lifebolbasor:
                                print ("Bolbasor [NO PUEDE SEGUIR]")
                                print ("el ganador es PIKACHU")
                                map_objects.remove(object_in_cell)
                            else:
                                print("Pikachu [NO PUEDE SEGUIR]")
                                print ("el ganador es BOLBASOR")
                    elif question == "n":
                        continue
                    continue

                if map_objects == []:
                    end_game = True
                    died = True
            if coordinate_y < len(obstacle_definition) and coordinate_x < len(obstacle_definition[coordinate_y]) and obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"
            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * map_width * 2 + "+")
    print (map_objects)
    print(cantireal)

    #ask user where he wants to move
    #direction = input("¿Dónde te quieres mover? [WASD]:")
    direction = readchar.readkey()

    new_position = None

    if direction == "w":
        new_position = [my_position[pos_x], (my_position[pos_y] - 1)]
    elif direction == "s":
        new_position = [my_position[pos_x], (my_position[pos_y] + 1)]
    elif direction == "a":
        new_position = [my_position[pos_x] - 1, my_position[pos_y]]
    elif direction == "d":
        new_position = [my_position[pos_x] + 1, my_position[pos_y]]
    elif direction == "q":
        end_game = True
    if new_position:
        if obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
            my_position = new_position
    
           
if died:
    print("GANASTE!!!")