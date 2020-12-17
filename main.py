import SelectionSort
import List
import timeit
import execution





if __name__ == "__main__":
    arr = List.LoadList("list2.dat")
    print("Banyak data : {}".format(len(arr)))
    print("Data:", arr)

    # iterative section
    start = timeit.default_timer()
    SelectionSort.selectionSortIterative(arr)
    execution.calulate("Iterative selection sort", start)
    
    # recursive section
    arr = List.LoadList("list2.dat")
    start = timeit.default_timer()
    SelectionSort.selectionSortRecursive(arr,0,len(arr))
    execution.calulate("Recursive selection sort", start)