def factorial(n):
    '''Calculating factorial'''
    if n==1 :
        return n
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

fibo_list = []
for i in range(100):
        fibo_list.append(0)
 
def fibo(n):
    '''Fibonacci sequence'''
    if n==0 or n ==1:
        fibo_list[n] = 1
        return n      
    else:
        fibo_list[n] = fibo(n-1)+fibo(n-2)
        return fibo_list[n]
