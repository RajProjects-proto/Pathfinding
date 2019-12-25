'''
The graph is defined by a 2D array.
The array can have obstacles which are represented with 'o'

'''
from array import *

#The lowest number that represents a valid coordinate
MIN = 0
#The largest X coordinate
MAX_X = 0
#The largest Y coordinate
MAX_Y = 0

class Graph:
    #Define the dimensions of the graph
    def __init__(self, dim_x, dim_y):
        self.rows, self.cols = (dim_x, dim_y)
        global MAX_X, MAX_Y
        MAX_X = dim_x
        MAX_Y = dim_y
        #Defining a 2D array
        self.graph = [['*' for i in range(self.rows)] for j in range(self.cols)]

    def printGraph(self):
        for item in self.graph:
            print(item)

    def setPointAs(self, x_coord, y_coord, val):
        self.graph[x_coord][y_coord] = val

    #traverse a path diven the starting and ending position in the graph
    def traverse(self, x_start, y_start, x_end, y_end):
        for coord in [x_start, x_end]:
            if (coord < MIN or coord > MAX_X):
                raise ArithmeticError("Entered x coordinate exceeds map limits")
        for coord in [y_start, y_end]:
            if (coord < MIN or coord > MAX_Y):
                raise ArithmeticError("Entered y coordinate exceeds map limits")
        #Make the map look more intuitive as to where the start and end are
        self.setPointAs(x_start, y_start, "S")
        self.setPointAs(x_end, y_end, "E")

if __name__ == "__main__":
    graph = Graph(18, 18)
    graph.printGraph()
    graph.traverse(2, 2, 5, 5)
    print("\n\n\n")
    graph.printGraph()
