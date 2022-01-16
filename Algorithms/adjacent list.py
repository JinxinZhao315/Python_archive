N=int(input('Type the number of nodes:'))
E=int(input('Type the value of twice of number of edges:')) # This value should be twice the number of edges, since you need to tell the edge goes back(i.e. this way the list is undirectional
adj_list = [[] for i in range(N)]

for i in range(E):
    x,y,w = map(int, input("Type the lists in the format of 'start destination weight', seperated by space").split())
    adj_list[x-1].append((y,w))


# map function: map(function, iterables). Apply the function to every iterable.
# Return a map object. You should convert it into a list if you need to. 


for i in range(N):
    print(str(adj_list[i]))
