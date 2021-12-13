"""
	For ease of use, please lay out your grid in Euclidean-plane format and NOT
	in numpy-type format. For example, if an object needs to be placed in the
	3rd row and 7th column of the gridworld numpy matrix, enter its location in your
	layout dict as [7,3]. The codebase will take care of the matrix-indexing for you.
	For example, the above object will be queried as grid[3, 7] when placed into the
	grid.

	NOTE: the origin (0,0) is the top-left corner of the grid. The positive direction
	along the x-axis counts to the right and the positive direction along the y-axis

"""

LINEAR = {
	'FOUR_PLAYERS': {
		'WALLS': [
			# First wall
			[0, 11],
			[1, 11],
			[2, 11],
			[3, 11],
			[4, 11],
			[5, 11],
			[8, 11],

			# Second wall
			[0, 7],
			[1, 7],
			[4, 7],
			[5, 7],
			[6, 7],
			[7, 7],
			[8, 7],

			# Third wall
			[0, 3],
			[1, 3],
			[2, 3],
			[3, 3],
			[4, 3],
			[5, 3],
			[8, 3]

		],

		# Doors are double doors of coord [[x1,x2], [y1,y2]]
		'DOORS': [
			[[6, 7], [11, 11]],
			[[2, 3], [7, 7]],
			[[6, 7], [3, 3]]
		],

		'PLATES': [
			[7, 13],
			[2, 9],
			[7, 5]
		],

		'AGENTS': [
			[5, 13],
			[5, 12],
			[4, 13],
			[4, 12]
		],

		'GOAL': [
			[3, 1]
		]
	},
	'FIVE_PLAYERS': {
		'WALLS': [
			# First wall
			[0, 15],
			[1, 15],
			# [4, 15],
			[5, 15],
			[6, 15],
			[7, 15],
			[8, 15],

			# Second wall
			[0, 11],
			[1, 11],
			[2, 11],
			[3, 11],
			[4, 11],
			# [5, 11],
			[8, 11],

			# Third wall
			[0, 7],
			[1, 7],
			# [4, 7],
			[5, 7],
			[6, 7],
			[7, 7],
			[8, 7],

			# Fourth wall
			[0, 3],
			[1, 3],
			[2, 3],
			[3, 3],
			[4, 3],
			# [5, 3],
			[8, 3],
		],

		# Doors are double doors of coord [[x1,x2], [y1,y2]]
		'DOORS': [
			[[2, 3, 4], [15, 15, 15]],
			[[5, 6, 7], [11, 11, 11]],
			[[2, 3, 4], [7, 7, 7]],
			[[5, 6, 7], [3, 3, 3]]
		],

		'PLATES': [
			[2, 17],
			[7, 13],
			[2, 9],
			[7, 5]
		],

		'AGENTS': [
			[6, 16],
			[5, 17],
			[5, 16],
			[4, 17],
			[4, 16]
		],

		'GOAL': [
			[3, 1]
		]
	},

	'SIX_PLAYERS': {
		'WALLS': [
			# First wall
			[0, 19],
			[1, 19],
			[2, 19],
			[3, 19],
			[4, 19],
			# [5, 19],
			[8, 19],

			# Second wall
			[0, 15],
			[1, 15],
			# [4, 15],
			[5, 15],
			[6, 15],
			[7, 15],
			[8, 15],

			# Third wall
			[0, 11],
			[1, 11],
			[2, 11],
			[3, 11],
			[4, 11],
			# [5, 11],
			[8, 11],

			# Fourth wall
			[0, 7],
			[1, 7],
			# [4, 7],
			[5, 7],
			[6, 7],
			[7, 7],
			[8, 7],

			# Fifth wall
			[0, 3],
			[1, 3],
			[2, 3],
			[3, 3],
			[4, 3],
			# [5, 3],
			[8, 3],
		],

		# Doors are double doors of coord [[x1,x2], [y1,y2]]
		'DOORS': [
			[[5, 6, 7], [19, 19, 19]],
			[[2, 3, 4], [15, 15, 15]],
			[[5, 6, 7], [11, 11, 11]],
			[[2, 3, 4], [7, 7, 7]],
			[[5, 6, 7], [3, 3, 3]]
		],

		'PLATES': [
			[7, 21],
			[2, 17],
			[7, 13],
			[2, 9],
			[7, 5]
		],

		'AGENTS': [
			[6, 21],
			[6, 20],
			[5, 21],
			[5, 20],
			[4, 21],
			[4, 20]
		],

		'GOAL': [
			[3, 1]
		]
	}
}
