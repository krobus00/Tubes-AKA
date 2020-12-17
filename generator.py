import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    for _ in range(n):
        arr.append(random.randint(-1000,1700))
    return arr

List.SaveList("list2.dat",listGenerator(10))