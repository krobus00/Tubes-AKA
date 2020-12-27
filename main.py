import sys
import SelectionSort
import List
import timeit
import execution
import time

if __name__ == "__main__":
    sys.setrecursionlimit(6000)
    if len(sys.argv) == 2:
        ldata = ["n100terbalik.dat","n100urut.dat"]
        for i in ldata:
            print("=========================")
            print("WORST CASE") if i == "n100terbalik.dat" else print("BEST CASE")
            arr = List.LoadList(i)
            print("Banyak data : {}".format(len(arr)))

            # iterative section
            start = timeit.default_timer()
            SelectionSort.selectionSortIterative(arr)
            execution.calulate("Iterative selection sort", start)

            # recursive section
            arr = List.LoadList(i)
            start = timeit.default_timer()
            SelectionSort.selectionSortRecursive(arr,0,len(arr))
            execution.calulate("Recursive selection sort", start)
    else:
        ldata = ["n10.dat","n100.dat","n500.dat","n1000.dat", "n1500.dat"]
        for i in ldata:
            print("=========================")
            arr = List.LoadList(i)
            print("Banyak data : {}".format(len(arr)))

            # iterative section
            start = timeit.default_timer()
            SelectionSort.selectionSortIterative(arr)
            
            execution.calulate("Iterative selection sort", start)

            # recursive section
            arr = List.LoadList(i)
            start = timeit.default_timer()
            SelectionSort.selectionSortRecursive(arr,0,len(arr))
            execution.calulate("Recursive selection sort", start)
