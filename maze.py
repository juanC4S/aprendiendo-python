import os
import random
import readchar

pos_x = 0
pos_y = 1

num_of_map_objects = 11

obstacle_definition = """\
##########################
                     #####
################     #####
################     #####
##########                
#################   ######
##########              ##
##############        ####
##############            
####################   ###
########    ######        
######                 ###
#######   ##########      
#####    #########       #
##########################\
"""

my_position = [0, 1]
tail_lengt = 0
tail = []
map_objects = []

end_game = False
died = False

#create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)
#main lopp
while not end_game:
    os.system("cls")
    #generate random objects on the map
    while len(map_objects) < num_of_map_objects:
        new_position = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)
    # Draw Map
    print("+" + "-" * map_width * 2 + "+")
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
            for tail_piece in tail:
                if tail_piece[pos_x] == coordinate_x and tail_piece[pos_y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece
            if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lengt += 1
                if tail_in_cell:
                    end_game = True
                    died = True
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"
            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * map_width * 2 + "+")

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
            tail.insert(0, my_position.copy())
            tail = tail[:tail_lengt]
            my_position = new_position

if died:
    print("Has muerto!")