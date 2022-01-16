value = [5,30,65,60,25]
weight = [10,60,80,50,40]
w = 120
n = 5

K = [[0 for x in range(w+1)] for y in range(n+1)] 


# w is the current capacity left of the knapsack

def knapSack(W, wt, val, n):
   for i in range(n+1):
       for w in range(W+1):
           if (i==0 or w==0):
               K[i][w] = 0
           elif (wt[i-1] <= w):
                 K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                 # =max(watch the show and have total left time being reduced by wt[i-1], or do not watch and leave a total time of w
                 # Here is a i-1 because the situation of i=0 is covered above.Use i-1 to point to the first element in the list
           else:
                 K[i][w] = K[i-1][w]
       
   return K[n][W];

# K[n][w] computes the maximum IQ gained at every given minute in the 120min. Hence K[n][W] gives the max IQ at 120min

print(knapSack(w,weight,value,n))
