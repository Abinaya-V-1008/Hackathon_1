cost=[]

import json
with open('level0.json','r') as f:
    data=json.load(f)

cost.append([0]+ data['restaurants']['r0']['neighbourhood_distance'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][0]]+data['neighbourhoods']['n0']['distances'])
#print(cost)
cost.append([data['restaurants']['r0']['neighbourhood_distance'][1]] + data['neighbourhoods']['n1']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][2]] + data['neighbourhoods']['n2']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][3]] + data['neighbourhoods']['n3']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][4]] + data['neighbourhoods']['n4']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][5]] + data['neighbourhoods']['n5']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][6]] + data['neighbourhoods']['n6']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][7]] + data['neighbourhoods']['n7']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][8]] + data['neighbourhoods']['n8']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][9]] + data['neighbourhoods']['n9']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][10]] + data['neighbourhoods']['n10']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][11]] + data['neighbourhoods']['n11']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][12]] + data['neighbourhoods']['n12']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][13]] + data['neighbourhoods']['n13']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][14]] + data['neighbourhoods']['n14']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][15]] + data['neighbourhoods']['n15']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][16]] + data['neighbourhoods']['n16']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][17]] + data['neighbourhoods']['n17']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][18]] + data['neighbourhoods']['n18']['distances'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][19]] + data['neighbourhoods']['n19']['distances'])
#cost.append(data['restaurants']['r0']['neighbourhood_distance'])


print(cost)
print(len(cost))
#import numpy as np
#cost=np.array(cost)
#print(cost.shape)


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

my_dict = {'ro': 0}

for i in range(1, 21):
    key = f'n{i}'
    my_dict[key] = i

print(my_dict)
reverse_dict = {value: key for key, value in my_dict.items()}
mapped_keys = [reverse_dict[value] for value in tour]
print(mapped_keys)

output_json = {"v0": {"path": mapped_keys}}
with open('output.json', 'w') as json_file:
    json.dump(output_json, json_file, indent=2)

print("JSON file 'output.json' created successfully.")











