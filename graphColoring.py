class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]\
						for row in range(vertices)]

	def isSafe(self, v, colour, c):
		for i in range(self.V):
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True
	
	def graphColourUtil(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m + 1):
			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				if self.graphColourUtil(m, colour, v + 1) == True:
					return True
				colour[v] = 0

	def graphColouring(self, m):
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) == None:
			return False

		print ("Coloring Indeks 0-15 (Kiri-Kanan):")
		for c in colour:
			print (c,end=" ")
		return True

"""
Food Number
Coffe :				Food :					Non-Coffe :
	[1] Espresso		[6 ] French Fries 		[11] Lemon Tea
	[2] Cappucino		[7] Croisant			[12] Taro Tea
	[3] Cafe Latte		[8] Deluxe Burger		[13] Chocoa Latte
	[4] Americano		[9] Potato Wedges		[14] Lychee Tea
	[5] Vanila Latte	[10] Cheese Burger		[15] Matcha Tea
"""

# Driver Code

g = Graph(15)
g.graph =	[
		[ 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ],
		[ 0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ],
		[ 1 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ],
		[ 1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ],
		[ 1 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ], 
		[ 1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ],
		[ 0 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ],
		[ 1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ],
		[ 1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ],
		[ 1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ],
		[ 1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ],
		[ 1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],
		[ 1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ],
		[ 0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ],
		[ 1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ],
    ]

m = 5
g.graphColouring(m)
