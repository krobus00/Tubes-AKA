import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    for i in range(n):
        # arr.append(n-i)
        arr.append(random.randint(1,512))
    return arr

List.SaveList("n512visualizer",listGenerator(512))