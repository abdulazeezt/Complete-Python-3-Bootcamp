from random import shuffle

##################      SHUFFLE functtion 
def shuffle_me(inputlist):

    shuffle(inputlist)
    return inputlist

##################  Player selection function

def player_selection(mylist):
    guess = ' '
    while guess not in['0','1','2']:
        guess = input("Please input a number for your GUESS 0, 1 , 2")
    #### need to return integer for further int comparisons. 
    return int(guess)

##################   Checking the guess

def check_guess(mylist,checkguess):
    #for i in mylist:
    #    print(f"hello{i}")
    #for i in mylist:
        if mylist[checkguess] == 0 :
            print(f"Correct guess")
        else:
            print("Wrong Guess")

#############3####      INITIAL LIST
mylist =['','',0]

##################      SHUFFLE LIST 
shuffle_me(mylist)
##################    USER GUESS
returnguess = player_selection(mylist)
##################     CHECK GUESS
check_guess(mylist,returnguess)
print(f"the correct guess is {mylist}")

#####################3