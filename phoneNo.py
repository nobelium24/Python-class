phone = input("Enter your Number: ")
dic = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
       "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": "Zero"}
dic2 = {}
for i in dic:
    for j in phone:
        if i == j:
            print(dic.get(i))
