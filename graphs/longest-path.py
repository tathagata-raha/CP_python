def topologicalSortUtil(v):
	global Stack, visited, adj
	visited[v] = True
	for i in adj[v]:
		if (not visited[i[0]]):
			topologicalSortUtil(i[0])
	Stack.append(v)

def longestPath(s):
	global Stack, visited, adj, V
	dist = [-10**9 for i in range(V)]
	for i in range(V):
		if (visited[i] == False):
			topologicalSortUtil(i)
	dist[s] = 0
	while (len(Stack) > 0):
		u = Stack[-1]
		del Stack[-1]
		if (dist[u] != 10**9):
			for i in adj[u]:
				if (dist[i[0]] < dist[u] + i[1]):
					dist[i[0]] = dist[u] + i[1]
	for i in range(V):
		print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")

