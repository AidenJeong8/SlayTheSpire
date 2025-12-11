class items: #parent item
    pass

class leftovers(items): #heal 20
    def get_path(self):
        return "items/leftovers.gif"
    def use(self):
        print("You have used a leftover item.")
        return 20
    
class potion(items): #heal 30
    def get_path(self):
        return "items/potion.gif"
    def use(self):
        print("You have used a potion.")
        return 30
    
class rocky_helmet(items): #deal 20 damage to player
    def get_path(self):
        return "items/rocky helmet.gif"
    def use(self):
        print("You have equipped a rocky helmet.")
        return -20
    
class picnic_basket(items): #heal 30 for player
    def get_path(self):
        return "items/picnic basket.gif"
    def use(self):
        print("You have used a picnic.")
        return 30

import random

def random_item(): #raondomly grant player item end of each round 
    item_classes = [leftovers, potion, rocky_helmet, picnic_basket]
    return random.choice(item_classes)() 


