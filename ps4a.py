# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/Users/pollygee/Documents/6001x/problem set 4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    if word == "":
        return 0
    else:
        score = 0 
        for char in word:
            letter_val = SCRABBLE_LETTER_VALUES[char]
            score += letter_val
        score = score * len(word)
        if len(word) == n:
            score += 50
        return score



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for char in word:
        occurnum = new_hand[char]
        occurnum -= 1
        new_hand[char] = occurnum
    return new_hand
        



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    is_valid = True
    new_hand = hand.copy()
    if word in wordList:
        for letter in word:
            if letter in new_hand:
                if new_hand[letter] < 1 :
                    is_valid = False
                else:
                    new_hand[letter] -= 1
            else:
                is_valid = False
    else:
        is_valid = False
    return is_valid


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for card in hand:
        if hand[card] > 0:
            length += hand[card]
    return length
        



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while hand > 0:                
        if calculateHandlen(hand) == 0:
            print "Run out of letters. Total score:", total_score
        else:
            print "Current hand :",
            displayHand(hand)
            
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total_score += getWordScore(word, n)
                print word, "earned", getWordScore(word, n), "points.  " "Total:", total_score
                print
                # Update the hand 
                hand = updateHand(hand, word)
         
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if hand == 0:
        print "Run out of letters. Total score: ", total_score, "points."
    elif word == ".":
        print "Goodbye! Total score: ", total_score

                        
#Quick function to preprocess word list
def loadWordScores(wordList, n):
    score_map = dict()
    for word in wordList:
        score_map[word] = getWordScore(word, n)
    return score_map

# Problem #6: Computer chooses a word
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            # Find out how much making that word is worth
            worth = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if worth > best_score:
                # Update your best score, and best word accordingly
                best_word = word
                best_score = worth

    # return the best word you found.
    return best_word
    
# Computer plays a hand    
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    #The hand keeps going as long as compChooseWord does not return None, it's inished when it returns None
    total_score = 0
    word_score = 0
    stopFlag = False
    
    while stopFlag != True:
        print "Current hand: ", 
        displayHand(hand)    
        word = compChooseWord(hand, wordList, n)

        if word != None:
            word_score = getWordScore(word, n)
            total_score += word_score
            #print the word and the points for the word as well as the total points
            print "'%s' earned %d points. Total: %d" %(word, word_score, total_score)
            print

            # Update the hand 
            hand = updateHand(hand, word)
            if calculateHandlen(hand) == 0:
                stopFlag = True
        else:
            stopFlag = True
        
    print "Total score: %s points." % total_score


# Problem #6: Computer chooses a word
def compChooseWordEx(hand, wordDict, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word, value in wordDict:
        # If you can construct the word from your hand
        if isValidWordEx(word, hand, wordDict):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            # Find out how much making that word is worth
            worth = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if worth > best_score:
                # Update your best score, and best word accordingly
                best_word = word
                best_score = worth

    # return the best word you found.
    return best_word

# Computer plays a hand    
def compPlayHandEx(hand, wordDict, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordDict: dictionary (string -> int)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    #The hand keeps going as long as compChooseWord does not return None, it's inished when it returns None
    total_score = 0
    word_score = 0
    stopFlag = False
    
    while stopFlag != True:
        print "Current hand: ", 
        displayHand(hand)    
        word = compChooseWordEx(hand, wordDict, n)

        if word != None:
            word_score = getWordScore(word, n)
            total_score += word_score
            #print the word and the points for the word as well as the total points
            print "'%s' earned %d points. Total: %d" %(word, word_score, total_score)
            print

            # Update the hand 
            hand = updateHand(hand, word)
            if calculateHandlen(hand) == 0:
                stopFlag = True
        else:
            stopFlag = True
        
    print "Total score: %s points." % total_score


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    wordScores = loadWordScores(wordlist)
    playGame(wordlist)

#print playHand({'i': 1, 'h': 1, 'm': 1, 'p': 1, 's': 1, 'r': 1}, wordList, 6)
#print playHand({'a': 1, 'z': 1}, wordList, 2)
#print playHand({'q': 1, 'i': 1, 'o': 1}, wordList, 3)
#print playHand({'y': 1, 'x': 2, 's': 1, 'z': 2, 'b': 1}, wordList, 7)
#print playHand({'y': 1, 'x': 2, 's': 1, 'z': 2, 'b': 1}, wordList, 7)