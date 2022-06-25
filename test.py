from msvcrt import kbhit


loc = [[1],[2],[3]] # Location xyz
# Dictionary of locations
loc_dict = {
    "1": [[3],[3],[3]],
    "2": [[4],[4],[4]],
    "3": [[5],[5],[5]],
}

loc_list = [
    [3,2,4],
    [4,4,4],
    [5,5,5],
]

loc_list[0][0]

# # loop trough the loc_list
# for i in loc_list:
#     #print(i)
#     # loop trough the list in the list
#     for j in i:
#         # replace loc with the list in the list
#         #print(j)
#         loc = j


# Looping trough the loc_list
print("\n", loc)
for i in loc_list:
    # replacing loc with the list in the list
    for j in range(3):
        loc[j] = i[j]
    print(loc)
#print(loc)
    
    