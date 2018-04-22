def roadsBuilding(cities, roads):
    return [[i,j] for i in range(cities-1) for j in range(i+1, cities) if [i,j] not in roads and [j,i] not in roads]