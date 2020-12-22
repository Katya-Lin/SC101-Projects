"""
File: hangman.py
Name: Katya Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    TODO:
    """
    ans = random_word()
    blank = ''
    wrong = 0

    for i in str(ans):
        blank += '-'
    print("The word looks like:"+str(blank))
    print("You have "+ str(N_TURNS - wrong)+ " guesses left.")

    k = 0
    while wrong < N_TURNS:
        k += 1
        letter = input("Your guess:")
        letter = letter.upper()

        if letter in ans:
            print("You are correct!")
            wrong = wrong
        else:
            print("There is no " + str(letter)+"\'s in the word")
            wrong += 1
            print("You have " + str(N_TURNS - wrong) + " guesses left.")

        my_ans = ''
        for j in str(ans):
            if letter == j:
                my_ans += j
            else:
                my_ans += '-'

        if k <= 1:    # For the first guess
            print("The word looks like:" + str(my_ans))
            old_ans = my_ans

        if k > 1:
            new_ans = ''
            for i in range(len(my_ans)):
                if my_ans[i] == '-' and old_ans[i] == '-':
                    new_ans += '-'
                else:
                    if my_ans[i] == '-':
                        new_ans += old_ans[i]
                    else:
                        new_ans += my_ans[i]
            old_ans = new_ans

            if new_ans == ans:
                wrong = N_TURNS + 1     # To stop the while loop.
                print("You win ! !")

            print("The word looks like:" + str(new_ans))

    if wrong == N_TURNS :
        print("You are completely hung : ( ")





def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
