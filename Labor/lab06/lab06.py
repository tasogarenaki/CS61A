this_file = __file__

# -------------------------------------- Q1 -------------------------------------- #
def make_adder_inc(a):
    """ return a + b by first time, then a + b + 1, then a + b + 2, and so on."""
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    count = 0
    def adder(b):
        nonlocal count          # use count to update it 
        sum = a + b + count
        count += 1              # update 
        return sum
    return adder





# -------------------------------------- Q2 -------------------------------------- #
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    pre, pro = -1, 1
    def count_fib():
        nonlocal pre, pro
        fib = pre + pro
        pre = pro
        pro = fib
        return fib
    return count_fib





# -------------------------------------- Q4 -------------------------------------- #
def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    new_lst = lst
    flag = 0
    for i, num in enumerate(lst):
        # additional condition flag to avoid stuck in the loop
        if num == entry and flag == 0:
            # insert the value in position i + 1
            new_lst.insert(i+1, elem)
            # update flag with continue to get out of loop
            flag = 1
            continue
        flag = 0
    return new_lst