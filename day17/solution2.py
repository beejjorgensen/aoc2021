import math, sys

# real
minx = 155
maxx = 215

miny = -132
maxy = -72

"""
# practice (112)
minx = 20
maxx = 30

miny = -10
maxy = -5
"""

g = lambda x: 0.5 * (math.sqrt(8*x + 1) - 1)

def get_starting_x_velocities():
	lowest = math.ceil(g(minx))
	return list(range(lowest, (maxx + 1) // 2 + 1)) + list(range(minx, maxx + 1))
	
def get_starting_y_velocities():
	return list(range(miny, abs(miny)))

def fire_broadside(good_x_velocities, good_y_velocities):
	hits = set()

	for starting_xv in good_x_velocities:
		for starting_yv in good_y_velocities:
			# Fire!
			x = 0
			y = 0

			xv = starting_xv
			yv = starting_yv

			while x <= maxx and y >= miny:
				if x >= minx and x <= maxx and y >= miny and y <= maxy:
					hits.add((starting_xv, starting_yv))
					break

				x += xv
				y += yv

				xv -= 1
				yv -= 1

				if xv < 0: xv = 0

	return hits

good_x_velocities = get_starting_x_velocities()
good_y_velocities = get_starting_y_velocities()

hits = fire_broadside(good_x_velocities, good_y_velocities)

print(len(hits))