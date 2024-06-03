class FordFulkersonMaxFlow:

	def __init__(self, graph, s, t):
		self.flow = 0
		self.graph = graph
		self.prev = [-1]*len(graph)
		self.s = s
		self.t = t

	def ford_fulkerson(self):
		while self.path():
			v = self.t
			capacity = float('inf')
			while v != self.s:
				capacity = min(capacity, self.graph[self.prev[v]][v])
				v = self.prev[v]
			v = self.t
			while v != self.s:
				self.graph[self.prev[v]][v] -= capacity
				self.graph[v][self.prev[v]] += capacity
				v = self.prev[v]
			self.flow += capacity

	def path(self):
		queue = [self.s]
		visited = [0]*len(self.graph)
		visited[self.s] = 1
		while queue:
			v = queue.pop(0)
			for i in range(len(self.graph[v])):
				u = self.graph[v][i]
				if u > 0 and visited[i] == 0:
					visited[i] = 1
					queue.append(i)
					self.prev[i] = v
					if i == self.t: return True
		return False
		
if __name__ == '__main__':
	graph = [[0, 3, 3, 2, 0, 0],
	                [0, 0, 0, 0, 4, 0],
	                [0, 0, 0, 1, 0, 2],
	                [0, 1, 0, 0, 0, 2],
	                [0, 0, 0, 1, 0, 1],
	                [0, 0, 0, 0, 0, 0]]
	print("Number of nodes = " + str(len(graph)))
	s = int(input("Choose source node: ")) - 1
	t = int(input("Choose sink node: ")) - 1
	flow = FordFulkersonMaxFlow(graph, s, t)
	flow.ford_fulkerson()
	print("Maximum flow = " + str(flow.flow))
 