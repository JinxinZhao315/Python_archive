def max_heapify(A,i,size=len(A)):
    left = 2*int(i)
    right = 2*int(i)+1
    if left <= size and A[left-1]>A[i-1]:
        largest = left
    else:
        largest = i
    if right <= size and A[right-1] > A[largest-1]:
        largest = right
    if largest != i:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        max_heapify(A,largest)
    return A


def build_max_heap(A):
    size=len(A)
    for i in range((size//2)-1,-1,-1):
        max_heapify(A,i)
