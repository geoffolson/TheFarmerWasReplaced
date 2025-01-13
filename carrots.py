# Till the land
clear()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        till()
        move(North)
    move(East)


while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            harvest()
            plant(Entities.Carrot)
            move(North)
        move(East)
