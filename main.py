while True:
	for i in range(get_world_size()):
		move(East)
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			else:
				plant(Entities.Bush)
				move(North)
