from gameComponents import gameVars

def winorlose(status):
	
	if status == "won":
		pre_message = "You are the winner!"
	else:
		pre_message = "You are the loser! "

	print(pre_message + "Would you like to play again?")
	
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		gameVars.player_lives = 3
		gameVars.computer_lives = 3
		gameVars.player = False

	elif choice == "N" or choice == "n":
		print("You chose to quit. See you next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N")
		if choice == "Y" or choice == "y":
			gameVars.player_lives = 3
			gameVars.computer_lives = 3
			gameVars.player = False

		else:
			print("You chose to quit. See you next time!")
			exit()

