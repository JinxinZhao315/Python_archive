N = int(input('Type the number of nodes:'))

adj_matrix = [[] for i in range(N)]

for i in range(N):
    adj_matrix[i] = list(map(int, input('Input one row of the matrix, seperate values by space').split()))

for i in range(N):
    print(str(adj_matrix[i]))
