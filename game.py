from random import randint

from gameComponents import gameVars, winLose, compareGame


while gameVars.player is False:
	
	print("===============*/ RPS /*====================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===================================")
	print("Choose your weapon! or type quit to exit\n")

	
	gameVars.player = input("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("You chose to quit, quitter!")
		exit()

	computer = gameVars.choices[randint(0, 2)]

	print("user chose: " + gameVars.player)

	print("AI chose: " + computer)

	compareGame.rpscompare(computer,gameVars.player)

	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

