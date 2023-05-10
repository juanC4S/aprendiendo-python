# en la version que me fallaba me botaba este error en la linea 80 el codigo era:
    import readchar
    import os
    import random
    pos_x = 0
    pos_y = 1



    num_of_map_objets=11
    tail_length = 0
    tail = []
    map_objets = []

    end_game=False
    died = False

    obstacle_definition = """\
    #######################
                    #####
    ############     #####
    #############     #####
    #######
    ##############   ######  
    ##########
    ##############   ####
    #####   #######      ##
    ######
    ########  ######
    #####   #######   #####
    ######################\
    """

    my_position =[0,1]


    #create obstacle map
    obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

    map_width = len(obstacle_definition[0])
    map_height = len(obstacle_definition)




    #Main loop
    while not end_game:
        os.system("cls")
        #generate random objets on the map
        while len(map_objets) < num_of_map_objets:
            new_position=[random.randint(0,map_width-1), random.randint(0, map_height-1)]
            if new_position not in map_objets and new_position != my_position:
                map_objets.append(new_position)
    #draw map
        print ("+"+"-" * map_width*3 +"+")
        for coordinate_y in range(map_height):
            print ("|", end="")
            for coordinate_x in range(map_width):
                char_to_draw= " "
                objet_in_cell = None
                tail_in_cell = None
                for map_object in map_objets:
                    if map_object[pos_x]== coordinate_x and map_object[pos_y] == coordinate_y:
                        char_to_draw ="*"
                        objet_in_cell = map_object

                for tail_piece in tail:
                    if tail_piece[pos_x] == coordinate_x and tail_piece[pos_y] == coordinate_y:
                        char_to_draw="@"
                        tail_in_cell = tail_piece
                if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:
                    
                    char_to_draw ="@"

                    if objet_in_cell:
                        map_objets.remove(objet_in_cell)
                        tail_length +=1
                    if tail_in_cell:
                        
                        died=True
                        end_game = True
                
                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "#"

                print (" {} ".format(char_to_draw), end="")
                
        
            print ("|")
        print ("+"+"-" * map_width*3 +"+")
        

        #Ask user where he wants to move

        #direction = input("¿Donde te quieres mover? [WASD]: ")
        direction = readchar.readchar()

        if direction =="w":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[pos_y] -=1
            my_position[pos_y] %= map_height

        elif direction =="s":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[pos_y] +=1
            my_position[pos_y] %= map_height

        elif direction =="a":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[pos_x] -=1
            my_position[pos_x] %= map_width
        elif direction =="d":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[pos_x] +=1
            my_position[pos_x] %= map_width   
        elif direction =="q":
            end_game=True

    

    if died:
        print ("Has muerto!")
        end_game = True
    line 80, in <module>
        if obstacle_definition[coordinate_y][coordinate_x] == "#":       
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    IndexError: list index out of range

# LA SOLUCION ERA: 
    El error se produce porque estás accediendo a un índice de una lista fuera de rango.
    Esto puede deberse a que el valor de coordinate_x o coordinate_y está siendo mayor que las dimensiones de la matriz obstacle_definition.
    Una posible solución es agregar una comprobación antes de acceder a la lista obstacle_definition para asegurarte de que los índices no estén fuera del rango.
    Puedes probar reemplazando la línea 80 con lo siguiente:

        if coordinate_y < len(obstacle_definition) and coordinate_x < len(obstacle_definition[coordinate_y]) and obstacle_definition[coordinate_y][coordinate_x] == "#":

    Esto primero comprueba que coordinate_y está dentro del rango de la lista obstacle_definition, luego comprueba que coordinate_x está dentro del rango de la fila correspondiente en la lista, y finalmente verifica si el elemento es un obstáculo. Y FUNCIONO GAAAA
