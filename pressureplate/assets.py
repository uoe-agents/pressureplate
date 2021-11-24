"""
	For ease of use, please lay out your grid in Euclidean-plane format and NOT
	in numpy-type format. For example, if an object needs to be placed in the
	3rd row and 7th column of the gridworld numpy matrix, enter its location in your
	layout dict as [7,3]. The codebase will take care of the matrix-indexing for you.
	For example, the above object will be queried as grid[3, 7] when placed into the
	grid.

"""

LINEAR = {
	'FOUR_PLAYER_WALLS': [
		# First wall
		[0, 11],
		[1, 11],
		[2, 11],
		[3, 11],
		[4, 11],
		[5, 11],
		[8, 11],

		# Second wall
		# [7, 9],
		# [7, 10],
		# [7, 11],
		# [7, 12],
		# [7, 13],
		# [7, 14],
		[0, 7],
		[1, 7],
		[4, 7],
		[5, 7],
		[6, 7],
		[7, 7],
		[8, 7],

		# Third wall
		# [3, 9],
		# # [3, 10],
		# [3, 11],
		# [3, 12],
		# [3, 13],
		# [3, 14]
		[0, 3],
		[1, 3],
		[2, 3],
		[3, 3],
		[4, 3],
		[5, 3],
		[8, 3]

	],

	# Doors are double doors of coord [[x1,x2], [y1,y2]]
	'FOUR_PLAYER_DOORS': [
		[[6, 7], [11, 11]],
		[[2, 3], [7, 7]],
		[[6, 7], [3, 3]]
	],

	'FOUR_PLAYER_PLATES': [
		[7, 13],
		[2, 9],
		[7, 5]
	],

	'FOUR_PLAYER_AGENTS': [
		[5, 13],
		[5, 12],
		[4, 13],
		[4, 12]
	],

	'FOUR_PLAYER_GOAL': [
		[3, 1]
	]
}

FOUR_CORNERS = {
	'FOUR_PLAYER_WALLS': [
		# Top left room
		[3, 0],
		[3, 1],
		[3, 2],
		[3, 3],
		[0, 3],
		[1, 3],

		# Top right room
		[0, 8],
		[1, 8],
		[2, 8],
		[3, 8],
		[3, 10],
		[3, 11],

		# Bottom left room
		[8, 0],
		[8, 1],
		[8, 3],
		[9, 3],
		[10, 3],
		[11, 3],

		# Bottom right room
		[8, 8],
		[8, 9],
		[8, 10],
		[8, 11],
		[9, 8],
		[10, 8]
	],

	'FOUR_PLAYER_DOORS': [
		# Top left room (bottom left plate opens)
		[2, 3],

		# Top right room (top left plate opens)
		[3, 9],

		# Bottom right room (top right plate opens)
		[11, 8]
	],

	'FOUR_PLAYER_PLATES': [
		# Bottom left plate (1)
		[10, 1],

		# Top left plate (2)
		[1, 1],

		# Top right plate (3)
		[1, 10],

	],

	'FOUR_PLAYER_AGENTS': [
		# Agent 1 (bottom left plate)
		[7, 4],

		# Agent 2 (top left plate)
		[4, 4],

		# Agent 3 (top right plate)
		[4, 7],

		# Agent 4 (bottom right goal)
		[7, 7]
	],

	'FOUR_PLAYER_GOAL': [
		# Bottom right room
		[10, 10]
	]
}