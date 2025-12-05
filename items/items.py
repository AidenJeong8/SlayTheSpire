class items: #parent item
    pass

class leftover(items): #heal 20 every round
    def get_path(self):
        return "items/leftover.gif"
    def use(self, player):
        player.notify("You have used a leftover item.")
        player.health += 20
        player.leftover_active = True
        return True
    
class potion(items): #heal 30
    def get_path(self):
        return "items/potion.gif"
    def use(self, player):
        player.notify("You have used a potion.")
        player.health += 30
        return True
    
class rocky_helmet(items): #deal 20 damage to enemy every round
    def get_path(self):
        return "items/rocky helmet.gif"
    def use(self, enemy, player):
        player.notify("You have equipped a rocky helmet.")
        enemy.health -= 20
        player.rocky_helmet_active = True
        return True
    
class picnic_basket(items): #heal 30 for both enemy and player
    def get_path(self):
        return "items/picnic basket.gif"
    def use(self, enemy, player):
        player.notify("You have used a picnic.")
        player.health += 30
        enemy.health += 30
        return True

def random_item(): #raondomly grant player item end of each round 
    import random
    item_classes = [leftover, potion, rocky_helmet, picnic_basket]
    return random.choice(item_classes)() 


