value = [5,30,65,60,25]
time = [10,60,80,50,40]
T = 120
n = 5

'''
You are to watch shows to entertain yourself. You have a total of 120min free time.
There are five shows avaliable and the utility you can gain from watching each show
is listed in the list 'value'. The length for each show is listed in the list 'time'
Find the maximum utility you can gain. 

'''

def knapSack( T, time, val, n):
   if (n == 0 or W == 0): '''If you have no show or no time'''
       return 0
   if(time[n-1] > T): '''If duration of show is longer than your time left'''
    return knapSack(T, time, val, n-1)
   else: 
    return max( val[n-1] + knapSack(T-time[n-1], time, val, n-1),
                    knapSack(T, time, val, n-1)
                  )
'''Find the max utility between: Watching show and having T-show_time left,
or not wathcing and have T time left. 
'''

'''
This problem is called O-1 knapsack
'''
