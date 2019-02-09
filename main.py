from itertools import islice
from graph import *
import time

#input the name of the graph file.
txt_file = 'graph_ADS2018_200.txt'


#Storing the city count, road count and destination
with open(txt_file, 'r') as file:
    first_line = file.readline()
    city = first_line.split(" ")
    city_count = city[0]
    road_count = city[1]

    last_line = file.readlines()[-1]
    last_line.split(" ")
    dest = last_line.split(" ")
    destination = dest[0]
    destination = destination.replace("\n", "")



#Create a graph with the values found from text file
num_lines = len(list(open(txt_file)))
g = Graph(int(city_count))

with open(txt_file, 'r') as file:
    for line in islice(file, 1, num_lines - 1):
         n1, n2, w = line.split()
         add_edge(g, int(n1),int(n2), int(w))




start = time.time()

print("the path is:" , bfs(kruskal(g), 1, int(destination)))
print("the highest point is: ", get_highest(kruskal(g), bfs(kruskal(g), 1, int(destination))))

stop = time.time()

print("total operation time: ", stop-start)