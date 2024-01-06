cost=[]

import json
with open('level0.json','r') as f:
    data=json.load(f)

cost.append(data['neighbourhoods']['n0']['distances'])
cost.append(data['neighbourhoods']['n1']['distances'])
cost.append(data['neighbourhoods']['n2']['distances'])
cost.append(data['neighbourhoods']['n3']['distances'])
cost.append(data['neighbourhoods']['n4']['distances'])
cost.append(data['neighbourhoods']['n5']['distances'])
cost.append(data['neighbourhoods']['n6']['distances'])
cost.append(data['neighbourhoods']['n7']['distances'])
cost.append(data['neighbourhoods']['n8']['distances'])
cost.append(data['neighbourhoods']['n9']['distances'])
cost.append(data['neighbourhoods']['n10']['distances'])
cost.append(data['neighbourhoods']['n11']['distances'])
cost.append(data['neighbourhoods']['n12']['distances'])
cost.append(data['neighbourhoods']['n13']['distances'])
cost.append(data['neighbourhoods']['n14']['distances'])
cost.append(data['neighbourhoods']['n15']['distances'])
cost.append(data['neighbourhoods']['n16']['distances'])
cost.append(data['neighbourhoods']['n17']['distances'])
cost.append(data['neighbourhoods']['n18']['distances'])
cost.append(data['neighbourhoods']['n19']['distances'])
#cost.append(data['restaurants']['r0']['neighbourhood_distance'])


#print(cost)
print(len(cost))


import math
def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance

tour, total_distance = solve_tsp_nearest(cost)

print("Tour:", tour)
rd=min(data['restaurants']['r0']['neighbourhood_distance'])
print(rd)
print("Total distance:", total_distance + 2*rd)









