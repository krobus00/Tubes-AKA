# Function recursive selection sort
def selectionSortRecursive(A, i):
    min = i
    n = len(A)
    if i + 1 < n:
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp    
        selectionSortRecursive(A, i + 1)

# Function iterative selection sort
def selectionSortIterative(A):
    for i in range(len(A) - 1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp