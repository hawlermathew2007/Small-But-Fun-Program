from random import randint

while True:
	print("Which one do you choose? rock, paper or scissors?")

	player = input().lower()
	computer = randint(0,2)

	if computer == 0:
		computer = "rock"
	if computer == 1:
		computer = "paper"
	if computer == 2:
		computer = "scissors"

	print("-----")
	print("You choose: " +str(player))
	print("Computer chooses: " + str(computer))
	print("-----")

	if player == computer:
		print("Draw")
	else:
		if player == "rock":
			if computer == "paper":
				print("You lose!")
			else:
				print("You win!")

		elif player == "paper":
			if computer == "scissors":
				print("You lose!")
			else:
				print ("You win!")

		elif player == "scissors":
			if computer == "rock":
				print("You lose!")
			else:
				print("You win!")

		else:
			print("try me:)?")

	play_again = input("wanna play again? yes or no?:").lower()

	if play_again != "yes":
		break