from locationgraphics import location
from deck import cards
from battle import fight
from updatelb import update_leaderboard

from items import items_real
import random
import math

# Welcomes
print("Welcome to Slay The Spire!")
print("In this game, you will use Pokemon to conquer various levels.")

name = input("What is your username? ")
score = 0

inventory = []

# instantiates XP
xp_file = open("xp.txt",mode="r")
xp = int(xp_file.readline())
xp_file.close()

# X is part of progression system; determines how many cards user can play
X = math.log(xp)/10

# entrance
print("We will start at the entrance.")
boost = location("entrance")
print("Here are the cards you can play:")
for i in range(math.floor(len(cards)*X)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
cards[i][1] += boost
score += fight(card_index, 0, inventory)
cards[i][1] -= boost

# middle
print("Congrats! You are at the middle.")
boost = location("middle")
print("Here are the cards you can play:")
for i in range(math.floor(len(cards)*X)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
cards[i][1] += boost
score += fight(card_index, 1, inventory)
cards[i][1] -= boost

# end
print("Final level!")
boost = location("end")
print("Here are the cards you can play:")
for i in range(math.floor(len(cards)*X)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
cards[i][1] += boost
score += fight(card_index, 2, inventory)
cards[i][1] -= boost


# update and print leaderboard
print("Leaderboard:")
update_leaderboard(score, name)
leaderboard = open("leaderboard.txt",mode="r")

lines = leaderboard.readlines()

for line in lines:
    s, n = line.strip().split(",")
    print(n,s)


# update xp
xp_file = open("xp.txt",mode="r")
xp = int(xp_file.readline())
xp += score
xp_file.close()

xp_file_w = open("xp.txt",mode="w")
xp_file_w.write(str(xp))
xp_file_w.close()

# show profile
profile = input("Do you want to see your profile? (y/n) ")
if profile == "y":
    print("*** PROFILE ***")
    print("*** XP:",str(xp),"***")
    print("*** Cards you can access",math.floor(len(cards)*X),"***")
