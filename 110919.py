# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


def spin_words(sentence):
    sentence = sentence.split()
    new_sentence = ""
    for i in range(len(sentence)):
        if len(sentence[i]) >= 5:
            new_sentence += sentence[i][::-1]
            if i != len(sentence)-1:
                new_sentence += " "
        else:
            new_sentence += sentence[i]
            if i != len(sentence)-1:
                new_sentence += " "
    return new_sentence


def spin_words_bp(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
