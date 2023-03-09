def order(sentence):
    string = []
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                string.append(word)

    return " ".join(string)