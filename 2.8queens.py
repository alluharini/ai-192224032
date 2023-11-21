 import copy  
  
from heapq import heappush, heappop  
  
n = 3  
  
# bottom, left, top, right  
rows = [ 1, 0, -1, 0 ]  
cols = [ 0, -1, 0, 1 ]  
   
class priorityQueue:  
       
    def __init__(self):  
        self.heap = []  
  
    # Inserting a new key 'key'  
    def push(self, key):  
        heappush(self.heap, key)  
   
    def pop(self):  
        return heappop(self.heap)  
  
    # funct to check if the Queue is empty or not  
    def empty(self):  
        if not self.heap:  
            return True  
        else:  
            return False  
  
# structure of the node  
class nodes:  
      
    def __init__(self, parent, mats, empty_tile_posi,  
                costs, levels):  
 
        self.parent = parent  
        self.mats = mats   
        self.empty_tile_posi = empty_tile_posi  
        self.costs = costs   
        self.levels = levels  
 
    def __lt__(self, nxt):  
        return self.costs < nxt.costs  
  
def calculateCosts(mats, final) -> int:  
      
    count = 0  
    for i in range(n):  
        for j in range(n):  
            if ((mats[i][j]) and  
                (mats[i][j] != final[i][j])):  
                count += 1  
                  
    return count  
  
def newNodes(mats, empty_tile_posi, new_empty_tile_posi,  
            levels, parent, final) -> nodes:  
                  
    new_mats = copy.deepcopy(mats)  
  
    # Moving the tile by 1 position  
    x1 = empty_tile_posi[0]  
    y1 = empty_tile_posi[1]  
    x2 = new_empty_tile_posi[0]  
    y2 = new_empty_tile_posi[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]  
  
    # Setting the no. of misplaced tiles  
    costs = calculateCosts(new_mats, final)  
  
    new_nodes = nodes(parent, new_mats, new_empty_tile_posi,  
                    costs, levels)  
    return new_nodes  
   
def printMatsrix(mats):  
      
    for i in range(n):  
        for j in range(n):  
            print("%d " % (mats[i][j]), end = " ")  
              
        print()  
  
def isSafe(x, y):  
      
    return x >= 0 and x < n and y >= 0 and y < n  
  
# Printing the path from the root node to the final node  
def printPath(root):  
      
    if root == None:  
        return  
      
    printPath(root.parent)  
    printMatsrix(root.mats)  
    print()  
  
# method for solving N*N - 1 puzzle algo  
# by utilizing the Branch and Bound technique. empty_tile_posi is  
# the blank tile position initially.  
def solve(initial, empty_tile_posi, final):  
      
    # Creating a priority queue for storing the live  
    # nodes of the search tree  
    pq = priorityQueue()  
  
    # Creating the root node  
    costs = calculateCosts(initial, final)  
    root = nodes(None, initial,  
                empty_tile_posi, costs, 0)  
  
    # Adding root to the list of live nodes  
    pq.push(root)  
  
    while not pq.empty():  
  
        minimum = pq.pop()  
  
        # If the min. is ans node  
        if minimum.costs == 0:  
               
            printPath(minimum)  
            return  
  
        # Generating all feasible children  
        for i in range(n):  
            new_tile_posi = [  
                minimum.empty_tile_posi[0] + rows[i],  
                minimum.empty_tile_posi[1] + cols[i], ]  
                  
            if isSafe(new_tile_posi[0], new_tile_posi[1]):  
                  
                # Creating a child node  
                child = newNodes(minimum.mats,  
                                minimum.empty_tile_posi,  
                                new_tile_posi,  
                                minimum.levels + 1,  
                                minimum, final,)  
  
                # Adding the child to the list of live nodes  
                pq.push(child)  
  

initial = [ [ 1, 2, 3 ],  
            [ 5, 6, 0 ],  
            [ 7, 8, 4 ] ]  
  
  
final = [ [ 1, 2, 3 ],  
        [ 5, 8, 6 ],  
        [ 0, 7, 4 ] ]  
  
empty_tile_posi = [ 1, 2 ]   
solve(initial, empty_tile_posi, final)  
