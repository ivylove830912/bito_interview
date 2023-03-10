def order(sentence):
    string = []
    for i in range(1, 10):
        for word in sentence.split():
            # 依序將數字小的字串加到string陣列裡
            if str(i) in word:
                string.append(word)

    return " ".join(string)
