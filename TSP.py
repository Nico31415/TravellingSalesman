import random
import numpy as np
import copy
import matplotlib.pyplot as plt
from itertools import permutations as per
import math


def print_pop(population):
    for i in population:
        print(i)

def minIndex(list):
    min = math.inf
    index = 0
    for i in range(len(list)):
        if(list[i] < min and list[i] > 0):
            min = list[i]
            index = i
    return index, min

def initialize_points(N):
    points = []
    for i in range(N):
        x = round(random.random()*100)
        y = round(random.random()*100)
        points.append([x,y])
    return points


def initialize_map(N): #initialize a map of the distances between points.

    points = initialize_points(N)

    distance_map = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            distance_map[i][j] = distance

    return points, distance_map

def pick_random(points):
    x = len(points)
    order = []
    for i in range(x):
        order.append(i)
    random.shuffle(order)
    return order

def goBack(order):  #fixes the fact that the salesman doesn´t go back to the original city
    order = list(order)
    order.append(order[0])
    return order


def connectpoints(x,y,p1,p2):
    x1,x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2])

def plot_points(map_points,points,order):
    px = []
    py = []

    print(points)
    for i in range(len(points)):
        px.append(points[i][0])
        py.append(points[i][1])
    for i in range(len(order)-1):
        connectpoints(px,py,order[i], order[i+1])
    plt.scatter(px,py)

def total_distance(map_points,order):
    distance = 0
    for i in range(len(order)-1):
        distance += map_points[order[i]][order[i+1]]
    return distance

def bruteForce(points,map_points):
    #find all the possible total distances that would take to travel to all the
    #points, and display the graph with the shortest distance_map
    distances = []
    orders = []
    order = pick_random(map_points)
    orders = (list(per(order)))
    for i in range(len(orders)):
        orders[i] = goBack(orders[i])
    print(orders)
    orders = orders[:int(len(orders)/2)]
    for i in range(len(orders)):
        distance = total_distance(map_points, orders[i])
        distances.append(distance)
    minDistIndex, minDist = minIndex(distances)
    minOrder = orders[minDistIndex]
    print(max(distances))
    return minDist, minOrder

def minEach(points,map_points):
    #start at the first point, then go to the point closest to it, then to the point closest to it
    #repeat until the second to last point, and then go to the last point
    #this is not the best method because closeness is a non transistive property
    order = [0]
    order[0],distance = minIndex(map_points[0])

    for i in range(1,len(map_points)):
        #list = map_points[int(order[i-2])]
        #list = list.pop(int(order[i-3]))
        print(order[i-1])
        index, min = minIndex(map_points[order[i-1]])
        distance += min
        #remove paths already taken
        order.append(index)

    distance = total_distance(map_points, order)
    return distance, order


def plotAll(map_points,points):
    order = pick_random(points)
    orders = list(per(order))
    for i in range(len(orders)):
        orders[i] = goBack(orders[i])
    orders = orders[:int(len(orders)/2)]
    #orders = orders[:int(len(orders)/2)]
    for i in range(len(orders)):
        distance = str(total_distance(map_points,orders[i]))
        plt.figure(i)
        plt.title(distance)
        plot_points(map_points,points,orders[i])


points, distance_map = initialize_map(8)
#distance, order = bruteForce(distance_map)
print('distance map ', distance_map)
#plotAll(distance_map,points)
distance, order= bruteForce(points,distance_map)
#distance, order = minEach(points,distance_map)
plot_points(distance_map,points,order)
#print(distance)
plt.show()
#total_distance()

def fitness():
    return True


def fitness(map_p ):
    return 1


def mutate(member):
    return member

def create_new_member():
    return member

def create_next_generation(population):
    return population

def main(number_of_iterations):
    return True
