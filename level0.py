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
cost.append(data['restaurants']['r0']['neighbourhood_distance'])

print(cost)






