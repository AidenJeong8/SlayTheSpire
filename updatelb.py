# updates leaderboard with a new score and name; simple sorting algorithm
def update_leaderboard(new_score, new_name):  
  leaderboard_list = []
  
  leaderboard_read = open("leaderboard.txt", "r")
  
  lines = leaderboard_read.readlines()
  
  for line in lines:
    score, name = line.strip().split(",")
    leaderboard_list.append([int(score), name])

  leaderboard_list.append([new_score, new_name])
  leaderboard_list.sort(reverse = True)
  
  leaderboard_write = open("leaderboard.txt", "w")

  for spot in leaderboard_list:
    name = spot[1]
    score = spot[0]
    leaderboard_write.write(str(score)+","+name)
    leaderboard_write.write("\n")
