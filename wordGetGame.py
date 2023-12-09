import random

# 単語リスト
words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'watermelon', 'strawberry']

def select_word(word_list):
    # 単語リストからランダムに単語を選択する
    return random.choice(word_list)

def guess_word(secret_word):
    guessed = False
    attempts = 0
    guessed_letters = []
    max_attempts = 6  # 最大試行回数

    while not guessed and attempts < max_attempts:
        # 正解の単語とユーザーの推測を比較する
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess not in secret_word:
                print("Letter is not in the word!")
                attempts += 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word!")
                guessed_letters.append(guess)
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                guessed = True
            else:
                print("Sorry, that's not the word!")
                attempts += 1
        else:
            print("Invalid guess. Please enter a single letter or the whole word.")

        status = ''
        for letter in secret_word:
            if letter in guessed_letters:
                status += letter
            else:
                status += '_'

        print("\nCurrent word status: " + status)

        if status == secret_word:
            guessed = True
        elif attempts == max_attempts:
            print("You ran out of attempts! The word was '{}'.".format(secret_word))
        else:
            print("Attempts left:", max_attempts - attempts)

    if guessed:
        print("Congratulations! You guessed the word '{}' in {} attempts.".format(secret_word, attempts))
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    selected_word = select_word(words)
    print("Welcome to the Word Guessing Game!")
    print("The word contains {} letters.".format(len(selected_word)))
    guess_word(selected_word)