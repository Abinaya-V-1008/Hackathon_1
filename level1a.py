cost=[]
capacity=[]
import json
with open('level1a.json','r') as f:
    data=json.load(f)

max_capacity=600;
capacity.append(0)
capacity.append(data['neighbourhoods']['n0']['order_quantity'])
capacity.append(data['neighbourhoods']['n1']['order_quantity'])
capacity.append(data['neighbourhoods']['n2']['order_quantity'])
capacity.append(data['neighbourhoods']['n3']['order_quantity'])
capacity.append(data['neighbourhoods']['n4']['order_quantity'])
capacity.append(data['neighbourhoods']['n5']['order_quantity'])
capacity.append(data['neighbourhoods']['n6']['order_quantity'])
capacity.append(data['neighbourhoods']['n7']['order_quantity'])
capacity.append(data['neighbourhoods']['n8']['order_quantity'])
capacity.append(data['neighbourhoods']['n9']['order_quantity'])
capacity.append(data['neighbourhoods']['n10']['order_quantity'])
capacity.append(data['neighbourhoods']['n11']['order_quantity'])
capacity.append(data['neighbourhoods']['n12']['order_quantity'])
capacity.append(data['neighbourhoods']['n13']['order_quantity'])
capacity.append(data['neighbourhoods']['n14']['order_quantity'])
capacity.append(data['neighbourhoods']['n15']['order_quantity'])
capacity.append(data['neighbourhoods']['n16']['order_quantity'])
capacity.append(data['neighbourhoods']['n17']['order_quantity'])
capacity.append(data['neighbourhoods']['n18']['order_quantity'])
capacity.append(data['neighbourhoods']['n19']['order_quantity'])

print(capacity)
print(len(capacity))


cost.append([0]+ data['restaurants']['r0']['neighbourhood_distance'])
cost.append([data['restaurants']['r0']['neighbourhood_distance'][0]] + data['neighbourhoods']['n0']['distances'])
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


#print(cost)
print(len(cost))

"""
import numpy as np

def knapsack_paths(distance_matrix, capacity_matrix, max_capacity, num_paths=3):
    num_nodes = len(distance_matrix)

    # Create a 3D array to store the maximum capacity and minimum distance for each subproblem
    dp = np.zeros((num_nodes, max_capacity + 1, num_paths + 1), dtype=object)

    for i in range(num_nodes):
        for j in range(max_capacity + 1):
            dp[i][j][0] = (0, [])  # Initialize the base case for the first path

    for path_count in range(1, num_paths + 1):
        for capacity in range(1, max_capacity + 1):
            for node in range(num_nodes):
                best_capacity, best_distance, best_path = dp[node][capacity][path_count - 1]

                for prev_node in range(num_nodes):
                    if prev_node != node and capacity >= capacity_matrix[node]:
                        remaining_capacity = capacity - capacity_matrix[node]
                        new_capacity = best_capacity + capacity_matrix[node]
                        new_distance = best_distance + distance_matrix[prev_node][node]

                        if dp[prev_node][remaining_capacity][path_count - 1][0] + capacity_matrix[node] > new_capacity:
                            new_capacity = dp[prev_node][remaining_capacity][path_count - 1][0] + capacity_matrix[node]
                            new_distance = dp[prev_node][remaining_capacity][path_count - 1][1] + distance_matrix[prev_node][node]
                            best_path = dp[prev_node][remaining_capacity][path_count - 1][2] + [node]

                        if new_capacity > best_capacity or (new_capacity == best_capacity and new_distance < best_distance):
                            dp[node][capacity][path_count] = (new_capacity, new_distance, best_path)

    # Find the path with the maximum capacity among the last path_count
    max_capacity_path = max(dp[:, max_capacity, num_paths], key=lambda x: x[0])

    return max_capacity_path[2]


max_capacity = 600

paths = knapsack_paths(cost, capacity, max_capacity)

for i, path in enumerate(paths):
    print(f"Path {i + 1}: {path} | Capacity: {sum(capacity_matrix[node] for node in path)} | Distance: {sum(distance_matrix[path[i - 1]][path[i]] for i in range(1, len(path)))}")
"""

#print(cost)
#print(capacity)

import numpy as np

def nearest_neighbor(current_node, unvisited_nodes, distance_matrix):
    # Find the nearest neighbor from the current node
    nearest_node = min(unvisited_nodes, key=lambda node: distance_matrix[current_node][node])
    return nearest_node

def create_delivery_slots(distance_matrix, capacity_matrix):
    num_nodes = len(distance_matrix)
    depot = 0  # Assume the depot is at index 0

    # Initialize variables
    unvisited_nodes = set(range(1, num_nodes))
    delivery_slots = {}

    # Create delivery slots for each vehicle
    vehicle_count = 0
    while unvisited_nodes:
        current_node = depot
        remaining_capacity = capacity_matrix[vehicle_count]
        path = ["r{}".format(current_node)]  # path starts and ends at the depot

        while unvisited_nodes and remaining_capacity > 0:
            nearest_node = nearest_neighbor(current_node, unvisited_nodes, distance_matrix)
            path.append("n{}".format(nearest_node))
            remaining_capacity -= 1
            unvisited_nodes.remove(nearest_node)
            current_node = nearest_node

        path.append("r{}".format(depot))
        delivery_slots["v{}".format(vehicle_count)] = {"path{}".format(vehicle_count + 1): path}
        vehicle_count += 1

    return delivery_slots


result = create_delivery_slots(cost,capacity)
print(result)


    
