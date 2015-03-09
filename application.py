import random 

GENERATED = random.randint(1, 20)
print GENERATED

NUMBER = input("insert a number from 1 to 20!!! ")

if NUMBER == GENERATED:
	print "You Win"
if NUMBER > GENERATED: 
	print "The number inserted is higher than generated, please try again."
if NUMBER < GENERATED: 
	print "The number inserted is lower than generated, please try again."
