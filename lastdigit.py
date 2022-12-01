def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

#https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python