import Utils

list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8]
wole = Utils.find_max(list)
print(wole)
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)





unique = []
for i in list:
    if i not in unique:
        unique.insert(0, i)
# print(unique)
        
number = [1,2,3]
x,y,z = number
# print(y)        
