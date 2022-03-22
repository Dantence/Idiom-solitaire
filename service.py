import draw
import turtle as t
import regex
import pypinyin



def solitaire(suffix, maxResNum):
    pinyinPattern = r'\b[a-z]*[āáǎàōóǒòêēéěèīíǐìūúǔùǖǘǚǜüńňǹɑɡ]+[a-z]*\b'
    chinesePattern = r"\p{han}+，?\p{han}+"
    words = []
    f = open("idiom.txt", encoding='utf-8')
    lines = f.readlines()
    i = 0
    while i < (len(lines)):
        pinyinList = regex.findall(pinyinPattern, lines[i])
        if not pinyinList:
            i += 1
            continue
        firstChar = pinyinList[0]
        lastChar = pinyinList[len(pinyinList) - 1]
        if (firstChar == suffix):
            word = regex.search(chinesePattern, lines[i]).group()
            words.append(word)
            suffix = lastChar
            i = -1
        i += 1
        if (len(words) >= maxResNum):
            break
    return words




