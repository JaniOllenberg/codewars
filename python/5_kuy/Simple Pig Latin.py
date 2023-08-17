import string
def pig_it(text):
    words = text.split()
    new_text = ""
    modified_words = []
    for word in words:
        if word in string.punctuation:
            modified_words.append(word)
            continue
        modified_words.append(word[1:] + word[0] + "ay")
    new_text = ' '.join(modified_words)
    return new_text