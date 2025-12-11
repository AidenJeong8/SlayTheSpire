import deck
import locations
import random
import turtle
import turtle as t
import items
import time


def fight(index, loc):
    selected_card = deck.cards[index] 
    player_hp = selected_card[1]
    player_cost1 = selected_card[3][0]
    player_dmg1 = selected_card[3][1]
    player_cost2 = selected_card[4][0]
    player_dmg2 = selected_card[4][1]

    screen, pokemon_textle, enemy_textle = fightvisuals(index, loc)
    update_battle(screen, pokemon_textle, enemy_textle, player_hp, locations.locs[loc][1], "0", "none", index)


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
            whos_turn = "player"
        elif (user_attack == 2):
            user_attack = player_dmg2
            user_cost = player_cost2
            whos_turn = "player"
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

        update_battle(screen, pokemon_textle, enemy_textle, player_hp, loc_hp, str(user_attack), whos_turn, index)

        if (loc_hp <= 0):
            print("Victory!")
            screen.bye()
            return player_hp
        if (player_hp <= 0):
            print("Defeat!")
            screen.bye()
            return 0

        loc_attack = random.randint(1, 2)
        if (loc_attack == 1):
            loc_attack = loc_dmg1
            loc_cost = loc_cost1
            whos_turn = "enemy"
        elif (loc_attack == 2):
            loc_attack = loc_dmg2
            loc_cost = loc_cost2
            whos_turn = "enemy"
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

        update_battle(screen, pokemon_textle, enemy_textle, player_hp, loc_hp, str(user_attack), whos_turn, index)

        if (loc_hp <= 0):
            print("Victory!")
            screen.bye()
            return player_hp
        if (player_hp <= 0):
            print("Defeat!")
            screen.bye()
            return 0

def fightvisuals(card_index, loc):
    t.TurtleScreen._RUNNING = True
    screen = t.Screen()
    screen.title("Pokemon Battle!")
    screen.setup(width=800, height=600)
    screen.tracer(0)  
    pokemon = deck.cards[card_index][5]
    enemy = locations.locs[loc][5]
    
    screen.addshape(enemy)
    screen.addshape(pokemon)
    
    enemy_turtle = t.Turtle()
    enemy_turtle.penup()
    enemy_turtle.goto(200, 200)
    enemy_turtle.color("red")
    enemy_turtle.write(locations.locs[loc][6], align="center", font=("Arial", 16, "normal"))
    enemy_turtle.goto(250, 0)
    enemy_turtle.shape(enemy)

    enemy_textle = t.Turtle()
    enemy_textle.penup()
    enemy_textle.goto(200, -200)
    enemy_textle.write("HP: " + str(locations.locs[loc][1]), align="center", font=("Arial", 20, "normal"))
    enemy_textle.hideturtle()
    
    pokemon_turtle = t.Turtle()
    pokemon_turtle.penup()
    pokemon_turtle.goto(-200, 200)
    pokemon_turtle.write(deck.cards[card_index][0], align="center", font=("Arial", 30, "normal"))
    pokemon_turtle.goto(-200, 0)
    pokemon_turtle.shape(pokemon)

    pokemon_textle = t.Turtle()
    pokemon_textle.penup()
    pokemon_textle.goto(-200, -200)
    pokemon_textle.write("HP: " + str(deck.cards[card_index][1]), align="center", font=("Arial", 20, "normal"))
    pokemon_textle.goto(-200, -230)
    pokemon_textle.write("Attack 1: " + str(deck.cards[card_index][3][1]) + " (Cost: " + str(deck.cards[card_index][3][0]) + ")", align="center", font=("Arial", 15, "normal"))
    pokemon_textle.goto(-200, -260)
    pokemon_textle.write("Attack 2: " + str(deck.cards[card_index][4][1]) + " (Cost: " + str(deck.cards[card_index][4][0]) + ")", align="center", font=("Arial", 15, "normal"))
    pokemon_textle.hideturtle()

    screen.update()


    return screen, pokemon_textle, enemy_textle


def update_battle(screen, pokemon_textle, enemy_textle, player_hp, loc_hp, damage, whos_turn, card_index):

    pokemon_textle.clear()
    pokemon_textle.goto(-200, -200)
    pokemon_textle.write("HP: " + str(player_hp), align="center", font=("Arial", 20, "normal"))
    pokemon_textle.goto(-200, -230)
    pokemon_textle.write("Attack 1: " + str(deck.cards[card_index][3][1]) + " (Cost: " + str(deck.cards[card_index][3][0]) + ")", align="center", font=("Arial", 15, "normal"))
    pokemon_textle.goto(-200, -260)
    pokemon_textle.write("Attack 2: " + str(deck.cards[card_index][4][1]) + " (Cost: " + str(deck.cards[card_index][4][0]) + ")", align="center", font=("Arial", 15, "normal"))
    
    enemy_textle.clear()
    enemy_textle.goto(200, -200)
    enemy_textle.write("HP: " + str(loc_hp), align="center", font=("Arial", 20, "normal"))
    
    damage_turtle = t.Turtle()
    damage_turtle.hideturtle()
    damage_turtle.penup()

    if whos_turn != "none":
        damage_turtle = t.Turtle()
        damage_turtle.hideturtle()
        damage_turtle.penup()
        damage_turtle.goto(0, 0)
        if whos_turn == "player":
            damage_turtle.color("green")
        elif whos_turn == "enemy":
            damage_turtle.color("red")
        
        damage_turtle.write("-" + damage, align="center", font=("Arial", 25, "normal"))

        screen.update()
        if whos_turn != "none":  
            time.sleep(3)
            damage_turtle.clear()
            screen.update()


