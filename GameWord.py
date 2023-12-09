import random

words = ['boy', 'gril', 'woman', 'man', 'male', 'female']

def select_word(word_list):
    return random.choice(word_list)

def guess_word(secret_word):
    guessed = False
    attempts = 0
    guessed_letters = []
    max_attempts = 6

    while not guessed and attempts < max_attempts:
        guess = input("推測された文字:").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("お前一回答えた文字だろ！これはカウントしねーよ！")
            elif guess not in secret_word:
                print("ないのよーん！どんまい〜")
                attempts += 1
                guessed_letters.append(guess)
            else:
                print("この文字は入っているよ！！！正解に近づいたね〜")
                guessed_letters.append(guess)
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                guessed = True
            else:
                print("これは正解じゃないのよー！一文字ずつじっくりと当てていきな！")
                attempts += 1
        else:
            print("このゲームのルールは単語を一文字ずつ当てていき、推測できたらその単語全文を入力するものなの。出直せい！")

        status = ''
        for letter in secret_word:
            if letter in guessed_letters:
                status += letter
            else:
                status += '_'

        print("\n現在の単語: " + status)

        if status == secret_word:
            guessed = True
        elif attempts == max_attempts:
            print("回答制限切れで〜す！正解は'{}'でした".format(secret_word))
        else:
            print("残りの回答弾数:", max_attempts - attempts)
    if guessed:
        print("正解でーす！正解単語:'{}' 回答数:'{}'".format(secret_word, attempts))
    else:
        print("不正解でーす！またの挑戦を待ってます！")

if __name__ == "__main__":
    selected_word = select_word(words)
    print("ゲームを始めるよ！")
    print("文字数は'{}'だよ！".format(len(selected_word)))
    guess_word(selected_word)