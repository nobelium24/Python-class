def find_max(list):
    maxNum = list[0]
    for i in list:
        if i > maxNum:
            maxNum = i
    return maxNum            