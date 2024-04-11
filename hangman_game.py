import random
from words import words

global play_still
play_still = True

global play_once
play_once = True

print("Welcome to Hangman!")

def play_hangman():
    global play_once
    play_once = True
    global word
    word = random.choice(words)
    loop_goes = True
    display = ""
    strikes = 0
    

    letters_remaining = [""]

   
    for letter in word: 
        if letter != '':
            letters_remaining.append(letter)

    letters_remaining.remove("")

    letters_guessed = ["_"] * len(letters_remaining)


    global play_still 
    play_still = True
    
    global new_word 
    new_word = False

    while play_still:
        atleast_one = False

        if new_word: 
            word = random.choice(words)
            new_word = False
        
        def display_letters():
            display = ""
            for let in letters_guessed: 
                display += let + ""
            return display

        print(display_letters())
        guess = input("Which letter do you guess is in the word above? ")
        

        for let in letters_remaining: 
            if guess == let: 
                index = letters_remaining.index(guess)
                letters_guessed[index] = guess
                letters_remaining[index] = ""
                atleast_one = True

        if not atleast_one:
            strikes += 1
            print("That letter is not in this word! You now have", strikes, "strikes")
            display_letters()
            if strikes >= 8:
                print("Game Over!")
                print("The word was", word)
                play_again = input("Would you like to play again? y or n? ")
                if play_again == "n":
                    print("Thanks for playing!")
                    play_once = False
                    break
                else:
                    play_still = False
                    play_once = True
                    new_word = True
            else:
                continue
        else:
            if display_letters() == word:
                print("Congratulations! You have guessed the word!")
                play_again = input("Would you like to play again? y or n? ")
                if play_again == "n":
                    print("Thanks for playing!")
                    play_once = False
                    break
                else:
                    play_still = False
                    play_once = True
                    new_word = True
            else: 
                print("You guessed correctly!")
                

while play_once:
    play_hangman()