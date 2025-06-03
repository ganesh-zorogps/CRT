class GraphList:
    def __init__(self,graph):
        self.graph={}
    def edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    def display(self):
        print("Adjacent List:")
        for i in self.graph:
            print(f"{i}-->{self.graph[i]}")
    def bfs(self,start):
        visited=set()
        queue=[start]
        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex,end=' ')
                for i in self.graph[vertex]:
                    if i not in visited:
                        queue.append(i)
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start,end=' ')
        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i,visited)
                        
g=GraphList({})
g.edge(1,2)
g.edge(1,3)
g.edge(2,4)
g.edge(3,4)
g.edge(4,5)
g.edge(5,6)
g.edge(6,7)
g.display()
g.bfs(1)
print("\n")
g.dfs(1)
