import math

minx = 155
maxx = 215

miny = -132
maxy = -72


f = lambda n: n*(n+1)/2
g = lambda x: 0.5 * (math.sqrt(8*x + 1) - 1)


"""
xcandidates = []

for i in range(minx, maxx+1):
	r = g(i)
	if r == int(r):
		#print(f"{i:2d} {g(i)}")
		xcandidates.append(int(r))

print(xcandidates)
"""


for i in range(5,1000):
	updist = int(f(i))

	norm_miny = updist - maxy
	norm_maxy = updist - miny

	#print(norm_miny, norm_maxy)

	for j in range(norm_miny, norm_maxy+1):
		r = g(j)
		if r == int(r):
			#print(f"up vel {i}, up dist = {updist}")
			#print(f"{j:2d} {r}")
			max_updist = updist

print(max_updist)



	

