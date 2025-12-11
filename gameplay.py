from locationgraphics import location
from deck import cards
from battle import fight
from updatelb import update_leaderboard
import items_real
import random

print(dir(items))


print("Welcome to Slay The Spire!")
print("In this game, you will use Pokemon to conquer various levels.")

name = input("What is your username? ")
score = 0


print("We will start at the entrance.")
location("entrance")
print("Here are the cards you can play:")
for i in range(len(cards)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
score += fight(card_index, 0)

print("Congrats! You are at the middle.")
location("middle")
print("Here are the cards you can play:")
for i in range(len(cards)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
score += fight(card_index, 1)

print("Final level!")
location("end")
print("Here are the cards you can play:")
for i in range(len(cards)):
    print(str(i)+":",cards[i][0])
card_index = int(input("Select which card to play: "))
score += fight(card_index, 2)


print("Leaderboard:")
update_leaderboard(score, name)
leaderboard = open("leaderboard.txt",mode="r")

lines = leaderboard.readlines()

for line in lines:
    s, n = line.strip().split(",")
    print(n,s)



xp_file = open("xp.txt",mode="r")
xp = int(xp_file.readline())
xp += score
xp_file.close()

xp_file_w = open("xp.txt",mode="w")
xp_file_w.write(str(xp))
xp_file_w.close()


profile = input("Do you want to see your profile? (y/n) ")
if profile == "y":
    print("*** PROFILE ***")
    print("*** XP:",str(xp),"***")
