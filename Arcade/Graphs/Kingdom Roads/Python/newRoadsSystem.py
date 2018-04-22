def newRoadSystem(roadRegister):

    to_city = roadRegister
    from_city = list(zip(*roadRegister))
    
    for i in range(len(roadRegister)):
        if to_city[i].count(True) != from_city[i].count(True):
            return False
    return True