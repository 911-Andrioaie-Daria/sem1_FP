#
# Implement the program to solve the problem statement from the second set here

#Problem 8. Find the smallest number m from the Fibonacci sequence, larger than the given natural number n.

def fibonacci(n):
    """
    The function generates and keeps track of the last 2 members of the Fibonacci ssequence
    until the last member becomes greater than n.
    :param n: The natural number up to which the sequence is generated
    :return: The member of the sequence greater than n
    """
    a = 0
    b = 1
    while b <= n:
        a, b = b, a + b
    return b

def show_result(n):
    m = fibonacci(n)
    print("The smallest number from the Fibonacci sequence, larger than ", n, " is ", m)

def start():
    n = int(input("Please enter n: "))
    show_result(n)

start()
