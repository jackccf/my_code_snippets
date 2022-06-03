# tma4 q1b
# purpose: a python program that reads an input of string and check if it is a palindrome based on a set of given rules.
# written by Cheung Chun Fai (s1285547)
# On 4/24/2021
# For tma4 q1b (comp-s258, 2021Autumn)

from pyListStack import Stack

def isPalindrome(aString):
    
    str_lower = aString.lower()

    # convert string to list of characters
    aString_list = list(str_lower)

    # create a list containing all letters for checking
    letter_list = []
    for i in range(26):
        letter_list.append(chr(ord('a')+i))
        letter_list.append(chr(ord('A')+i))

    # regard consecurive letters as one single letter
    repeat_list = []
    for i in range(len(aString_list)):
        try:
            if aString_list[i] == aString_list[i+1]: repeat_list.append(i+1)
        except: break

    for i in repeat_list:
        del aString_list[i]
        aString_list.insert(i, '*')
        
        # remove non-letter characters
    aString_copy = aString_list.copy()
    for e in aString_copy:
        if e not in letter_list: aString_list.remove(e)\

    # conver list of character to string
    str_cache = ""
    for e in aString_list: str_cache += e

    # check isPalindrome
    checkString = str_cache

    s = Stack()
   
    for ch in checkString:
        s.push(ch)

    reversedText = ''
    while not s.isEmpty():
        reversedText = reversedText + s.pop()
    
    return checkString == reversedText


if __name__ == '__main__':
    negative_examples = ['AB', 'aAABb']
    positive_examples = ['A', 'AAa', 'AAAABBA', 'AaaBBaaaA', 'A78124832838989898934938928439A', 'A23904239483298*$#(*($#**$(#    A']

    while True:
        userText = input("Please enter the text you want to check (<ENTER> to quit): ")
        if len(userText) == 0:
            break
        if isPalindrome(userText):
            print("yes")
        else:
            print("no")
    print("Till next time!")

    # help to display result after executing the program
    input()


    # # check with hardcoding
    # if isPalindrome('AAa'): 
    #     print("yes")
    # else: 
    #     print("no")

