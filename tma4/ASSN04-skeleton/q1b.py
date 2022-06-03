from pyListStack import Stack

def isPalindrome(aString):
    # Modify this function
    s = Stack()
    checkString = aString.replace(" ","").lower()
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