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

varible = NoVowels('Computer Science Makes the World go round but it doesn\'t make the world round itself!')
print(varible)

"""Write an encryption code that you make up and run it for the variable NoVowels"""
