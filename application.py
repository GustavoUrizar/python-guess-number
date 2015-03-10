import random

NEWGAME = True
while NEWGAME == True:
	GENERATED = random.randint(1, 20) #variable that generates the random number. 
	print GENERATED
	COUNTER = 1
	VALIDATE = True
	while VALIDATE == True:
		
		NUMBER = input("insert a number from 1 to 20!!! ")
		if NUMBER == GENERATED:
			print "You Win"
			ANSWER = True
			while ANSWER == True:
				AGAIN = raw_input("Do you want to play again, yes or no: ")
				if AGAIN == "yes":
					ANSWER = False
					VALIDATE = False
					NEWGAME = True
				elif AGAIN == "no":
					ANSWER = False
					VALIDATE = False
					NEWGAME = False
		elif NUMBER > GENERATED: 
			print "The number inserted is higher than generated, please try again."
			COUNTER += 1
		elif NUMBER < GENERATED: 
			print "The number inserted is lower than generated, please try again."
			COUNTER += 1
		if COUNTER == 5:
			print "GAME OVER"
			VALIDATE = False
			NEWGAME = True
			ANSWER = True
			while ANSWER == True:
				AGAIN = raw_input("Do you want to play again, yes or no: ")
				if AGAIN == "yes":
					ANSWER = False
					VALIDATE = False
					NEWGAME = True
				elif AGAIN == "no":
					ANSWER = False
					VALIDATE = False
					NEWGAME = False
