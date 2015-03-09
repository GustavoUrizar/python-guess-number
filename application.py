import random 

GENERATED = random.randint(1, 20)
print GENERATED


COUNTER = 1
while COUNTER <= 4:
	NUMBER = input("insert a number from 1 to 20!!! ")
	if NUMBER == GENERATED:
		print "You Win"
		AGAIN = raw_input("Do you want to play again, yes or no")
		if AGAIN == "yes":
			COUNTER += 1
		elif AGAIN == "no":
			break
	if NUMBER > GENERATED: 
		print "The number inserted is higher than generated, please try again."
		COUNTER += 1
	if NUMBER < GENERATED: 
		print "The number inserted is lower than generated, please try again."
		COUNTER += 1
