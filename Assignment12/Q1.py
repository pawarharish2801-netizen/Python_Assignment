
def ChkVowel( ch):
    if ( ch == 'a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u'
         or ch == 'A' or ch =='E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    else:
        return False
def main():
    char = input("Enter a character: ")

    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
        return
    
    bRet = ChkVowel(char)

    if (bRet ==True):
        print ("The Alphabet is Vowel ")
    else:
        print("The Alphabet is not a Vowel")

if __name__ == "__main__":
    main()