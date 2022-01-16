path = []
path_len_list = []

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def Paths(root):
    PathsRec(root, path, 0)
    return max(path_len_list) 
  

def PathsRec(root, path, pathLen):
    if root is None:
        return 0

    if len(path) > pathLen:
        path[pathLen] = root.data
    else:
        path.append(root.data) 

    pathLen = pathLen + 1
  
    if root.left is None and root.right is None:
        path_len_list.append(count_distinct_values(path))
    else: 
        PathsRec(root.left, path, pathLen) 
        PathsRec(root.right, path, pathLen) 
  
def count_distinct_values(path):
    distinct_list =[]
    for m in range(0,len(path)):
        if path[m] not in distinct_list:
            distinct_list.append(path[m])
    return len(distinct_list)

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2)
