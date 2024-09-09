import random
import  hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

print("Your word to guess: " + chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
correct_letters = []

print(placeholder)
game_over = False
while not game_over:
    print(f"****************{lives}/6 LIVES LEFT****************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}!")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        print(f"You guessed: {guess}, that's not in the word. You lose a life.")

    if "_" not in display:
        game_over = True
        print('****************You win****************')

    if guess not in chosen_word:
        lives-= 1

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word}!")
            print("****************You loose!****************")



    stages = hangman_art.stages
    print(stages[lives])