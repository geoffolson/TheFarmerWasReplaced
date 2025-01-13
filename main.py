CARROT_MIN = 1700
WOOD_MIN = 1000
WOOD_MAX = 2000
HAY_MIN = 1000
HAY_MAX = 2000

def water_tile():
	if get_water() < 0.7:
		use_item(Items.Water)

def for_each(callback):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			callback()
			water_tile()
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
	while num_items(Items.Wood) >= 3 and num_items(Items.Hay) >= 3:
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
	while num_items(Items.Wood) < WOOD_MAX:
		for_each(wood)

def hays():
	clear()
	def hay():
		if not can_harvest():
			do_a_flip()
		harvest()
	while num_items(Items.Hay) < HAY_MAX:
		for_each(hay)

def pumpkins():
	till_map()
	def pumpkin():
		if can_harvest():
			harvest()
			plant(Entities.Pumpkin)
		elif get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
	while num_items(Items.Carrot) >= 3:
		for_each(pumpkin)

while True:
	if num_items(Items.Wood) > WOOD_MIN and num_items(Items.Hay) > HAY_MIN and num_items(Items.Carrot) >= CARROT_MIN:
		pumpkins()
	elif num_items(Items.Wood) >= WOOD_MIN and num_items(Items.Hay) >= HAY_MIN and num_items(Items.Carrot) < CARROT_MIN:
		carrots()
	elif num_items(Items.Hay) <= 3:
		hays()
	else:
		woods()
