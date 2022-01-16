from collections import deque


n = int(input("Number of vertices"))
e = int(input("Number of edges"))
visited = [False for i in range(n)]

# Edges are given in the next e lines in the format (a, b),
# meaning that the edge is connecting vertices a and b
# Do your own input!

adj_list = [] 

def dfs(a):
    '''depth first search'''
    if visited[a]:
        return
    visited[a] = True
    for x in adj_list[a]:
        dfs(x)
    # Assume the edges are 'weightless' (i.e. all weight = 1 ) so there is not need to store weight.
    # There is only [(destination),(destination),....] in any adjacency list. 
        

def bfs(a):
    '''breadth first search'''
    Q = deque()
    Q.append(a)
    
    while len(Q) != 0:
        x = Q.popleft() # .popleft() removes and returns the head of the queue. 
        visited[x] = True
        
        for nx in adj_list[x]:
            if visited[nx]:
                continue
            
            Q.append(nx)
            # This for loop iterates through all immediate children of any node
            # And push any children unvisited into the queue
