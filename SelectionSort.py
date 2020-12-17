# Function recursive selection sort
def selectionSortRecursive(A, i, n):
    min = i
    for j in range(i + 1, n):
        if A[j] < A[min]:
            min = j
    temp = A[min]
    A[min] = A[i]
    A[i] = temp
    if i + 1 < n:
        selectionSortRecursive(A, i + 1, n)

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