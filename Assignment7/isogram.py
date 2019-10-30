def is_isogram(xword):
    found = {}
    for i in xword:
        if i in found:
            return False
        else:
            found[i] = 1
    return True

if __name__ == "__main__":
    words = ["dermatoglyphics","palindrome", "anagram"]
    for w in words:
        print(is_isogram(w))