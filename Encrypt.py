"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def NoVowels(plaintext):
    ciphertext = ''
    for ch in plaintext:
        if ord(ch) is 65 or ord(ch) is 97 or ord(ch) is 69 or ord(ch) is 101 or ord(ch) is 73:
            ciphertext = ciphertext
        elif ord(ch) is 105  or ord(ch) is 79 or ord(ch) is 111 or ord(ch) is 85 or ord(ch) is 117:
            ciphertext = ciphertext
        else:
            ciphertext += ch
    return ciphertext

variable = NoVowels('Computer Science Makes the World go round but it doesn\'t make the world round itself!')
print(variable)

"""Write an encryption code that you make up and run it for the variable NoVowels"""
def scribble(plaintext):
    ciphertext = ''
    halflength = int(len(plaintext) / 2)
    fronthalf = plaintext[:halflength]
    backhalf = plaintext[halflength:]
    fronthalf2 = ''
    for ch in fronthalf:
        fronthalf2 = ch + fronthalf2
    charCount = 0
    even = ''
    odd = ''
    for ch in fronthalf2:
        if charCount % 2 is 0:
            even += ch
        else:
            odd += ch
        charCount += 1
    fronthalf = even + odd
    backhalf2 = ''
    for ch in backhalf:
        backhalf2 = ch + backhalf2
    ciphertext = backhalf2 + fronthalf2
    return ciphertext
print(scribble(variable))
