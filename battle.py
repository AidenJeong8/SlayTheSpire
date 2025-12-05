import deck
import locations
import random
import turtle
import turtle as t
import items


card_index = int(input("Select which card to play: "))
location_index = int(input("Select a location on the map to travel to: "))
print("\n\n\n")

def fight(index, loc):
    selected_card = deck.cards[index] 
    player_hp = selected_card[1]
    player_cost1 = selected_card[3][0]
    player_dmg1 = selected_card[3][1]
    player_cost2 = selected_card[4][0]
    player_dmg2 = selected_card[4][1]

    fightvisuals(index,loc)
    
    print("Pokemon selected: " + selected_card[0])
    print("Initial HP: " + str(selected_card[1]))

    selected_loc = locations.locs[loc] 
    loc_hp = selected_loc[1]
    loc_cost1 = selected_loc[3][0]
    loc_dmg1 = selected_loc[3][1]
    loc_cost2 = selected_loc[4][0]
    loc_dmg2 = selected_loc[4][1]

    print("Location selected: " + selected_loc[0])
    print("Initial HP: " + str(selected_loc[1]))

    print("\n\n\n")



    for i in range(10):

        print("\n\nRound " + str(i+1) + "\n")

        user_attack = int(input("Attack 1 or 2\n"))
        if (user_attack == 1):
            user_attack = player_dmg1
            user_cost = player_cost1
        elif (user_attack == 2):
            user_attack = player_dmg2
            user_cost = player_cost2
        else:
            print("Invalid")
            return
        
        player_hp -= user_cost
        loc_hp -= user_attack


        print("You lost " + str(user_cost) + " HP")
        print("Location lost " + str(user_attack) + " HP\n")

        print("Your HP: " + str(player_hp))
        print("Location HP: " + str(loc_hp))

        print("\n")

        if (loc_hp <= 0):
            print("Victory!")
            return
        if (player_hp <= 0):
            print("Defeat!")
            return

        loc_attack = random.randint(1, 2)
        if (loc_attack == 1):
            loc_attack = loc_dmg1
            loc_cost = loc_cost1
        elif (loc_attack == 2):
            loc_attack = loc_dmg2
            loc_cost = loc_cost2
        else:
            print("Invalid")
            return
        
        loc_hp -= loc_cost
        player_hp -= loc_attack

        print("You lost " + str(loc_attack) + " HP")
        print("Location lost " + str(loc_cost) + " HP\n")

        print("Your HP: " + str(player_hp))
        print("Location HP: " + str(loc_hp))

        print("\n")

        if (loc_hp <= 0):
            print("Victory!")
            return
        if (player_hp <= 0):
            print("Defeat!")
            return

def fightvisuals(card_index, loc):
    screen = t.Screen()
    screen.title("Pokemon Battle!")
    screen.setup(width=800, height=600)
    pokemon = deck.cards[card_index][5]
    t.penup()
    t.goto(-200, 0)
    screen.addshape(pokemon)
    t.shape(pokemon)





fight(card_index, location_index)



