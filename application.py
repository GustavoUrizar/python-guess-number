import random

print """WELCOME TO GUESS NUMBER"""
NEWGAME = True
while NEWGAME == True:
	GENERATED = random.randint(1, 20) #variable that generates the random number. 
	print GENERATED
	COUNTER = 1
	VALIDATE = True
	while VALIDATE == True:
		COUNTER += 1 #variable that counts the turns
		if COUNTER <= 5:
			try: 
				NUMBER = input("insert a number from 1 to 20!!! ")
				if NUMBER == GENERATED:
					print "You Win"
					ANSWER = True
					while ANSWER == True:
						AGAIN = raw_input("Do you want to play again, yes or no: ")
						if AGAIN == "yes" or AGAIN == "y" or AGAIN == "Y" or AGAIN =="YES":
							ANSWER = False
							VALIDATE = False
							NEWGAME = True
						elif AGAIN == "no" or AGAIN == "n" or AGAIN == "NO" or AGAIN == "N":
							print "THANK YOU FOR PLAYING"
							ANSWER = False
							VALIDATE = False
							NEWGAME = False
						else:
							"that is not valid, try again."
				elif NUMBER > GENERATED: 
					print "The number inserted is higher than generated, please try again."
				elif NUMBER < GENERATED: 
					print "The number inserted is lower than generated, please try again."
			except SyntaxError:
				print "you only can select a number from 1 to 20"
			except NameError:
				print "you only can select a number from 1 to 20"
		else:
			print "GAME OVER"
			ANSWER = True
			while ANSWER == True:
				AGAIN = raw_input("Do you want to play again, yes or no: ")
				if AGAIN == "yes" or AGAIN == "y" or AGAIN == "Y" or AGAIN =="YES":
					ANSWER = False
					VALIDATE = False
					NEWGAME = True
				elif AGAIN == "no" or AGAIN == "n" or AGAIN == "NO" or AGAIN == "N":
					print "THANK YOU FOR PLAYING"
					ANSWER = False
					VALIDATE = False
					NEWGAME = False
				else:
					"that is not valid, try again."		
	