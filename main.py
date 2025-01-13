def for_each(callback):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			callback()
			move(North)
		move(East)


def till_map():
	clear()
	for_each(till)

def carrots():
	till_map()
	def carrot():
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		elif get_entity_type() != Entities.Carrot:
			plant(Entities.Carrot)
	while num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1:
		for_each(carrot)

def can_plant_tree():
	x_even = get_pos_x() % 2 == 0
	y_even = get_pos_y() % 2 == 0
	if x_even and y_even:
		return True
	if not x_even and not y_even:
		return True
	return False

def woods():
	clear()
	def wood():
		if can_harvest():
			harvest()
		if can_plant_tree():
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	while num_items(Items.Wood) < 1000:
		for_each(wood)

def hays():
	clear()
	def hay():
		if not can_harvest():
			do_a_flip()
		harvest()
	while num_items(Items.Hay) < 1000:
		for_each(hay)


while True:
	if num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1 and num_items(Items.Carrot) < 600:
		carrots()
	elif num_items(Items.Hay) <= 1:
		hays()
	else:
		woods()
