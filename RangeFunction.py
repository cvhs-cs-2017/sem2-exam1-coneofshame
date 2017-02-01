"""Use the range function to print the numbers from 40 to 1 (backwards)"""
def count():
    for i in range(40, 0, -1):
        print(i)
print(count())

"""Repeat the exercise but count by 5's"""
def count():
    for i in range(40, 0, -5):
        print(i)
print(count())



"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
def multiples():
    x = 1
    n = int(input('Enter a number... '))
    a = n
    for i in range(10):
        n = n * x
        print(n)
        x += 1
        n = a
print(multiples())
