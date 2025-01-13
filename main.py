def till_map():
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			move(North)
		move(East)

def carrots():
	till_map()
	while num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
				elif get_entity_type() != Entities.Carrot:
					plant(Entities.Carrot)
				move(North)
			move(East)

def can_plant_tree():
	x_even = get_pos_x() % 2 == 0
	y_even = get_pos_y() % 2 == 0
	if x_even and y_even:
		return True
	if not x_even and not y_even:
		return True
	return False

def wood():
	clear()
	while num_items(Items.Wood) < 1000:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if can_plant_tree():
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				move(North)
			move(East)

def hay():
	clear()
	while num_items(Items.Hay) < 1000:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if not can_harvest():
					do_a_flip()
				harvest()
				move(North)
			move(East)


while True:
	if num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1:
		carrots()
	elif num_items(Items.Hay) < 1:
		hay()
	else:
		wood()
