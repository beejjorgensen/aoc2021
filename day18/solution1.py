def preorder(n, depth=0):
	if isinstance(n, int):
		print(f"{depth}: leaf: {n}")
		return n
	
	print(f">{depth}: {n}")

	left = preorder(n[0], depth+1)
	right = preorder(n[1], depth+1)

	return [left, right]

	print(f"<{depth}: {n}")
"""
inputs = (
	[1,2],
	[[1,2],3],
	[9,[8,7]],
	[[1,9],[8,5]],
)

for i in inputs:
	print("----------")
	preorder(i)
"""

#preorder([[[[[9,8],1],2],3],4])
r = preorder([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])

print(r)
