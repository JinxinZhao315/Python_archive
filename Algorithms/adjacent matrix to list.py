# Convert an adjacent matrix to an adjacent list
N = int(input('Type the number of nodes:'))
adj_list = [[] for i in range(N)]
adj_matrix = [[] for i in range(N)]

for i in range(N):
    adj_matrix[i] = list(map(int, input('Input one row of the matrix, seperate values by space').split()))

for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 0:
            continue
        else:
            adj_list[i].append((j,adj_matrix[i][j]))

for i in range(N):
    print(adj_list[i])
        
