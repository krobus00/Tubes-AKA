# dataout = []
# ldata = ["n10.dat","n100.dat","n500.dat","n1000.dat", "n1500.dat"]
import List
def selectionSortRecursive(A, i):
    if i+1 == len(A):
        return A
    else:
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp
        A = selectionSortRecursive(A, i + 1)
    

arr = List.LoadList("n10.dat")
selectionSortRecursive(arr, 0)
print(arr)
