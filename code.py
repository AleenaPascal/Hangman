import random
import time
print("\n----- WELCOME TO HANGMAN GAME ----- \n")
name =input("Enter your name: ")
print("Hello " + name + "! Best of Luck!\n")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman! \n\n\n")
time.sleep(3)
 
def main():
    global count
    global display
    global word
    global guessed_word
    guessed_word=[]
    global length
    global key
    global play_game
    words_to_guess =["flower","book","park","fire","swing","pencil","time","pizza","plane","bottle"
                   ,"cloud"]
    word = random.choice(words_to_guess)
    key=word
    length = len(word)
    count = 0
    display = '_ ' * length
    guessed_word =""
    play_game = ""
 

def hangman():
    global count
    global display
    global word
    global guessed_word
    global play_game
    limit = 5
    guess =input("This is the Hangman Word: " + display + " Enter your guess: \n")
    if guess.isdigit():
      print("Invalid Input,Try an Alphabet\n")
      hangman()
    guess = guess.strip()
    if len(guess) != 1:
        print("Invalid Input, Try a letter\n")
        hangman()
 
 
    elif guess in word:
        guessed_word=guessed_word+guess
        index = word.find(guess)
        print(index)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index*2] + guess + display[index*2 + 1:]
        print(display + "\n")
 
    elif guess in guessed_word:
        print("Try another letter.\n")
 
    else:
        count += 1
 
        if count == 1:
            time.sleep(1)
            print("   ___ \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "_||_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n\n")
 
        elif count == 2:
            time.sleep(1)
            print("   ___ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "_||_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n\n")
 
        elif count == 3:
           time.sleep(1)
           print("   ___ \n"
                 "  ||     | \n"
                 "  ||     |\n"
                 "  ||     | \n"
                 "  ||      \n"
                 "  ||      \n"
                 "  ||      \n"
                 "_||_\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n\n")
 
        elif count == 4:
            time.sleep(1)
            print("   ___ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||     | \n"
                  "  ||     O \n"
                  "  ||      \n"
                  "  ||      \n"
                  "_||_\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n\n")
 
        elif count == 5:
            time.sleep(1)
            print("   ___ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||     | \n"
                  "  ||     O \n"
                  "  ||    /|\ \n"
                  "  ||    / \ \n"
                  "_||_\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",key)
            play_loop()
 
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
 
    elif count != limit:
        hangman()
 
def play_loop():
    global play_game
    ch =input("Do You want to play again? (y/n)")
    play_game=ch.lower()
    while play_game not in ["y", "n"]:
        play_game =input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
    else:
      print("wrong input")
    
main()
 
 
hangman()
