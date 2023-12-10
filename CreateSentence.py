import random

# 英語の単語リスト
words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'watermelon', 'strawberry']

# 例文を作成する関数
def generate_sentence(words_list, length=5):
    sentence = []
    for _ in range(length):
        word = random.choice(words_list)
        sentence.append(word)
    return ' '.join(sentence).capitalize() + '.'


if __name__ == "__main__":
    example_sentence = generate_sentence(words, length=8)
    print(example_sentence)

