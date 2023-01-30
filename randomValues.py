import random

members = ["Wole", "Ife", "Ope", "Pelumi", "Ore"]
# print (random.choice(members))

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

  
         

dip = Dice()
print(dip.roll())            
