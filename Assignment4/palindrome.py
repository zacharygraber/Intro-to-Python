def palindrome(x: str):
    """
    Input a sentence cleaned of punctuation, spacing, and capitalization
    Output boolean is the input a palindrome?
    """
    isPalindrome = True
    for i in range(0,len(x)):
        if x[i] != x[len(x) - (i+1)]:
            isPalindrome = False
            break
    return isPalindrome

if __name__ == "__main__":
    print(palindrome("aba"))
    print(palindrome("a"))
    print(palindrome("abba"))
    print(palindrome("amanaplanacanalpanama"))
    print(palindrome("abca"))
    print(palindrome("ac"))
    print(palindrome("adabbba"))
    print(palindrome("amandaplanacanalpanama"))
    print(palindrome("racecar"))
    print(palindrome("wasitacatisaw"))