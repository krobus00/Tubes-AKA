import os
import random
import sys
import time

import pygame

import List


class Algorithm:
    def __init__(self, name):
        self.array = List.LoadList("n512visualizer.dat")
        self.name = name # Get name of the variable

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2) # pass the indexes to be swapped into the visualizer

    def run(self): # Start the timer and run the algorithm
        self.start_time = time.time() 
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed
class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)-1):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])

 # Set the window length and breadth  (Make sure that the breadth is equal to size of array. [512])
dimensions = [1024, 512]
# List all the Algorithm available in the project in dictionary and call the necessary functions from Algorithm.py
Algorithm = {"SelectionSort": SelectionSort()}

# Initalise the pygame library
pygame.init()
# Set the dimensions of the window and display it
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
# Fill the window with purple hue
display.fill(pygame.Color("#a48be0"))

def check_events(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update(algorithm, swap1=None, swap2=None, display=display): # The function responsible for drawing the sorted array on each iteration
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)        
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    try:
        algorithm = Algorithm['SelectionSort'] # Pass the algorithm selected
        try:
            time_elapsed = algorithm.run()[1]
            keep_open(algorithm, display, time_elapsed)
            pass
        except:
            pass
    except:
        print("Error.")        

if __name__ == "__main__":
    main()
