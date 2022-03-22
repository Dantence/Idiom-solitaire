import pypinyin
import turtle as t
import draw
from service import solitaire

if __name__ == "__main__":
    word = input()
    suffix = pypinyin.pinyin(word)[len(word) - 1][0]
    words = solitaire(suffix, 10)
    words.insert(0, word)
    print(words)

    draw.drawAll()
    draw.drawWords(words, 550, 300)
    signature = ["计203", "殷逸维", "42024141"]
    draw.drawWords(signature, 550, -250)
    t.done()