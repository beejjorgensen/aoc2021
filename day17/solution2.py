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

f = lambda n: n*(n+1)/2
g = lambda x: 0.5 * (math.sqrt(8*x + 1) - 1)

def get_starting_x_velocities():
	# Determine min and max x starting velocities
	xcandidates = []

	for i in range(minx, maxx+1):
		r = g(i)
		if r == int(r):
			#print(f"{i:2d} {g(i)}")
			xcandidates.append(int(r))

	#print(xcandidates)

	lowest_x_vel = xcandidates[0]
	highest_x_vel = maxx

	#print(lowest_x_vel, highest_x_vel)
	good_x_velocities = set()

	# Try them all looking for hits
	for i in range(lowest_x_vel, highest_x_vel + 1):
		xpos = 0
		vel = i
		while True:
			if xpos <= maxx and xpos >= minx:  # hit
				good_x_velocities.add(i)
				break

			if xpos > maxx:  # miss far
				break

			if vel == 0:   # miss near
				break

			xpos += vel
			vel -= 1

	return good_x_velocities
	
def get_starting_y_velocities():
	# Determine min and max y starting velocities
	lowest_y_vel = miny
	highest_y_vel = 8646  # from part 1

	good_y_velocities = set()

	# Try them all looking for hits
	for i in range(lowest_y_vel, highest_y_vel + 1):
		print(f"\r{int(100 * i / (highest_y_vel - lowest_y_vel))}%", end="", flush=True)
		ypos = 0
		vel = i
		while True:
			if ypos <= maxy and ypos >= miny:  # hit
				good_y_velocities.add(i)
				break

			if ypos < miny:  # miss far
				break

			ypos += vel
			vel -= 1

	print()

	return good_y_velocities

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

"""
minx = 20
maxx = 30

miny = -10
maxy = -5
"""

# Sample data results
good_x_velocities = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
good_y_velocities = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1}

# Real data results
good_x_velocities = {18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215}
good_y_velocities = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1}

#good_x_velocities = None
#good_y_velocities = None

if good_x_velocities is None:
	good_x_velocities = get_starting_x_velocities()
if good_y_velocities is None:
	good_y_velocities = get_starting_y_velocities()

#print(good_x_velocities)
#print(good_y_velocities)

hits = fire_broadside(good_x_velocities, good_y_velocities)

"""
for x, y in sorted(list(hits)):
	print(f"{x},{y}")
"""

print(len(hits))