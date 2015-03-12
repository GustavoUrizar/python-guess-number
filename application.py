"""WELCOME TO GUESS NUMBER"""
import random

NEWGAME = True
while NEWGAME == True:
    GENERATED = random.randint(1, 20) #variable that generates the random number.
    print GENERATED
    COUNTER = 1
    VALIDATE = True
    while VALIDATE == True:
        COUNTER += 1 #variable that counts the turns
        if COUNTER <= 5: #if sets the number of turns
            try: #This try verifies errors in the game
                NUMBER = int(raw_input("insert a number from 1 to 20!!! "))
                #variable used to ask a number.
                if NUMBER == GENERATED: #if number is the same than generated the user wins.
                    print "You Win"
                    ANSWER = True
                    while ANSWER == True:
                    #this while handles all the option to play again.
                        AGAIN = raw_input("Do you want to play again, yes or no: ")
                        #if the user wants to play again.
                        if AGAIN == "yes" or AGAIN == "y" or AGAIN == "Y" or AGAIN == "YES":
                            ANSWER = False
                            VALIDATE = False
                            NEWGAME = True
                        elif AGAIN == "no" or AGAIN == "n" or AGAIN == "NO" or AGAIN == "N":
                            print "THANK YOU FOR PLAYING"
                            ANSWER = False
                            VALIDATE = False
                            NEWGAME = False
                        else:
                            print "that is not valid, try again."
                elif NUMBER > GENERATED: # if the user guesses higher than generated.
                    print "The number inserted is higher than generated, please try again."
                elif NUMBER < GENERATED: # if the user guesses lower than generated.
                    print "The number inserted is lower than generated, please try again."
            except SyntaxError:
                print "you only can select a number from 1 to 20"
            except NameError:
                print "you only can select a number from 1 to 20"
        else: # if the user overcomes the number of trials.
            print "GAME OVER"
            ANSWER = True
            while ANSWER == True:
            #this while handles all the options to play again.
                AGAIN = raw_input("Do you want to play again, yes or no: ")
                #give to user the option to play again.
                if AGAIN == "yes" or AGAIN == "y" or AGAIN == "Y" or AGAIN == "YES":
                    ANSWER = False
                    VALIDATE = False
                    NEWGAME = True
                elif AGAIN == "no" or AGAIN == "n" or AGAIN == "NO" or AGAIN == "N":
                    print "THANK YOU FOR PLAYING"
                    ANSWER = False
                    VALIDATE = False
                    NEWGAME = False
                else:
                    print "that is not valid, try again."
    