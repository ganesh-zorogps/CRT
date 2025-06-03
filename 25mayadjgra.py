class Graphadjmat:
    def __init__(self,size=None,adjmat=None):
        if adjmat is not None:
            self.adjmat=adjmat
            self.size=len(adjmat)
        else:
            self.size=size
            self.adjmat=[[0 for _ in range(size)]for _ in range(size)]
            
    def addedge(self,u,v):
        if u < self.size and v<self.size:
            self.adjmat[u][v]=1
            self.adjmat[v][u]=1

    def display(self):
        print("Adjancy matrix")
        for row in self.adjmat:
                print("_".join(map(str,row)))
adjmat=[
[0,1,1,0,0,0,0],
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,1,0,0],
[0,0,0,1,0,1,0],
[0,0,0,0,1,0,1],
[0,0,0,0,0,1,0]
]
g=Graphadjmat(adjmat=adjmat)
g.display()
        
