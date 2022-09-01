from audioop import add


LAB_SOURCE_FILE = __file__
this_file = __file__

# --------------------------------------- Q2 ----------------------------- #
def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    total = 0
    """
    while n > 0:
        total += n
        n -= 2
    return total 
    """
    total += n
    if n >= 2:
        n -= 2
        return skip_add(n) + total
    else:
        return total





# --------------------------------------- Q3 ----------------------------- #
def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    total = 0
    total += term(n)
    if n > 1:
        return summation(n-1,term) + total 
    else:
        return total





# --------------------------------------- Q4 ----------------------------- #
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    # if there is only 1 row or 1 column
    if m == 1 or n == 1:
        return 1
    else:
        # the insect kann only go up (m-1) or go right (n-1)
        return paths(m-1, n) + paths(m, n-1)





# --------------------------------------- Q5 ----------------------------- #
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    the_size = len(str(n))

    if n == 0 or t == 0:
        return 0
    elif the_size == t or the_size+1 == t or the_size == 1:
        return n

    with_ones = max_subseq(n//10, t-1) * 10 + n % 10
    without_ones = max_subseq(n//10, t)
    if with_ones > without_ones:
        return with_ones
    else:
        return without_ones









def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    if w1 == '':
        return w2
    
    # if the first index is not the same
    if w1[0] != w2[0]:
        # then take it out from w2 and search for the next 
        # every time will 1 char shorter since w2[1:] into function 
        # will use as w2[0:]
        return w2[0] + add_chars(w1[:], w2[1:])
    else:
        return add_chars(w1[1:], w2[1:])