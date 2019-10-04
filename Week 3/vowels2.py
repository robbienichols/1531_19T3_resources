import sys

if __name__ == "__main__":
    #new dictionary
    dictionary = {}
    #initialise vowel counts to zero
    for vowel in 'aeiou':
        dictionary[vowel] = 0
    #read from standard input
    wordList = sys.stdin.readline().split(' ')
    #loop the list of words
    #['this', 'is', 'a', 'rabbit']
    for word in wordList:
        for character in word:
            if character in dictionary:
                dictionary[character] += 1
    #print vowel dictionary
    print(dictionary)
    