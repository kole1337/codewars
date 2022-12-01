def testit(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n & (n-1)
    return count

#https://www.codewars.com/kata/56d931ecc443d475d5000003/train/python