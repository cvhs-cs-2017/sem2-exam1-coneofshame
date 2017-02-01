"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""

def count(n):
    x = 0
    while n <= 100:
        n += 5
        x += 1
    print(n)
    print('I added ' + str(x) + ' 5\'s')
print(count(101))



"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
def math():
    num = input('Enter a number... ')
    if num.startswith('1') or num.startswith('2') or num.startswith('3') or num.startswith('4') or num.startswith('5'):
        if int(num) % 2 is 0:
            num = int(num) * 3
        else:
            num = int(num) * 2
    elif num.startswith('6') or num.startswith('7') or num.startswith('8') or num.startswith('9') or num.startswith('0'):
        if int(num) % 2 is 0:
            num = int(num) * 3
        else:
            num = int(num) * 2
    else:
        num = 'That\'s not a number'
    return num
print(math())
