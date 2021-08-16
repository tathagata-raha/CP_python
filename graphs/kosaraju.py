class Graph:

	def __init__(self,vertices):
		self.V= vertices
		self.graph = defaultdict(list)
	def addEdge(self,u,v):
		self.graph[u].append(v)
	def DFSUtil(self,v,visited):
		visited[v]= True
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)

	def getTranspose(self):
		g = Graph(self.V)
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g
	def isSC(self):
		visited =[False]*(self.V)
		self.DFSUtil(0,visited)
		if any(i == False for i in visited):
			return False
		gr = self.getTranspose()
		visited =[False]*(self.V)
		gr.DFSUtil(0,visited)
		if any(i == False for i in visited):
			return False
		return True
