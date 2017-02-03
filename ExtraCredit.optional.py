"""Write a program that will take a Binary number and return its Whole Number Value:

example:  10011 would return (16+0+0+2+1 = 19)"""
def binaryToNumber(binary):
    num = 0
    binary2 = ''
    charCount = 0
    for ch in str(binary):
        binary2 = ch + binary2
    for ch in str(binary2):
        if ch == '0':
            power = 0
        else:
            power = (2 ** charCount)
        num += power
        charCount += 1
    return num
print(binaryToNumber(1001))




"""Write a program that would take a real number value and convert it into BINARY"""
def numberToBinary(number):
    
