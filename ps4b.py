from ps4a import *
import time

#
# Problem #5: Playing a game
# 
def playGameOld(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    in_play = True
    previous = False
    while in_play == True:
        menu = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if menu == "n":
            previous == True
            playHand((dealHand(HAND_SIZE)), wordList, HAND_SIZE)
        elif menu == "r":
            if not previous:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif menu == "e":
            in_play == False
            return
        else:
            print "Invalid command."


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    in_play = True
    valid_commands = ['n', 'r', 'e']
    valid_hand = None
    hand = None
    
    while in_play == True:
        user_choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_choice in valid_commands:
            #exit if the entered choice is e
            if user_choice == "e":
                in_play = False
            else:
                #Generate a new random hand if necessary
                if user_choice == "n":
                    hand = dealHand(HAND_SIZE)
                    valid_hand = True
                else:
                    if hand == None:
                        #User needs to play a new hand first before playing an r
                        print "You have not played a hand yet. Please play a new hand first!"
                        valid_hand = False
                    
                #prompt for user or computer turn
                if valid_hand == True:
                    redo_choice = True
                    valid_choices = ['u', 'c']
                
                    while redo_choice == True:
                        user_choice = raw_input("Enter u to have yourself play, c to have the computer play: ")
                        if user_choice in valid_choices:
                            #Computer or user makes next move
                            if user_choice == "u":
                                playHand(hand, wordList, HAND_SIZE)
                            else:
                                compPlayHand(hand, wordList, HAND_SIZE)
                            #End the loop
                            redo_choice = False
                        else:
                            print "Invalid command."
        else:
            #Invalid command entered
            print "Invalid command."
    
#
# Run the program
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
