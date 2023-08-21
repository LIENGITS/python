#I have the list: [[1,2],[2,3],[3,4]] and I need to subtract a value from the second value in each list inside this list.

coordinate = [[1,2],[2,3],[3,4]]

def coordinates(y):
    new_list = [ ]
    for i in (y):
        new_list += [[i[0],i[1]-1]]
    print (new_list)

coordinates(coordinate)
