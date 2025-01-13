def till_map():
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			move(North)
		move(East)

def carrots():
	till_map()
	while num_items(Items.Wood) > 1:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				harvest()
				plant(Entities.Carrot)
				move(North)
			move(East)

def wood():
	clear()
	while num_items(Items.Wood) < 1000:
		for i in range(get_world_size()):
			move(East)
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				plant(Entities.Bush)
				move(North)


while True:
	if num_items(Items.Wood) > 1:
		carrots()
	else:
		wood()
