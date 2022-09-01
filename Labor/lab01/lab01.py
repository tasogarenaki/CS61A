def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    product = n
    if k != 0 :
        for m in range(k-1):
            product = product * (n-m-1)
        return product 
    else:
        return 1

print(falling(6,3))







def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # int to string
    n1 = str(y)
    length = len(n1)
    the_sum = 0
    for n in range(length):
        the_sum = the_sum + int(n1[n])
    return the_sum

print(sum_digits(4224))







def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = 0    # no 8 (no module = 8)
    while n > 0:
        n, d = n // 10, n % 10  # n div 10 -> module d = n % 10
        if d == 8 and flag == 1:    # has 8 and already has one more 8 (marked as flag)
            return True
        elif d == 8:    # if has 8, mark the flag
            flag = 1
        else:   # if does not have 8, move flag
            flag = 0
    return False

print(double_eights(880088))