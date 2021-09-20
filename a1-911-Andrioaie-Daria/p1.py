#
# Implement the program to solve the problem statement from the first set here

# Problem 2. Given natural number n, determine the prime numbers p1 and p2 such that n = p1 + p2

'''
Program description:
The program uses the 'Sieve of Eratosthenes' to mark with 0 all the primes and with 1 all the non-primes
in the sequence of the first n natural numbers.
Then, for each prime number p1 up to n/2, it verifies if the number n-p1 is also a prime and when such a pair
is found, it returns the pair
'''

def sieve(n):
    """
    The function uses the 'Sieve of Eratosthenes' to mark with 0 all the primes and with 1 all the non-primes
in the sequence of the first n natural numbers.
    :param n: the natural number up to which we want to mark the primes
    :return: a list of n-1 elements, where the primes are marked with 0 and the non-primes with 1
    """
    a = []
    #all elements are initialised with 0, supposing that they are prime
    for i in range(n):
        a.append(0)

    #0 and 1 are marked non-primes by default
    a[0] = 1
    a[1] = 1

    #the multiples of each prime that we find are marked with 1. (since they have a divisor, they are not prime)
    for i in range(2, n):
        if a[i] == 0:
            for j in range(2 * i, n, i):
                a[j] = 1
    return a


def find_p1(a, n):
    """
    The function searches for the first prime number p1, such that n-p1 is also a prime
    :param a: a list with n elements, marked with 0-primes, 1- non-primes
    :param n: the number for which we must find a pair of primes
    :return: p1
    """
    for i in range(2, int(n/2)+1):
        if a[i] == 0 and a[n - i] == 0:
            return i

def find_numbers(n):
    pair_of_primes = []
    a = sieve(n)  # build the sieve
    p1 = find_p1(a, n)  # search for p1
    pair_of_primes.append(p1)
    p2 = n - p1
    pair_of_primes.append(p2)
    return pair_of_primes

def print_the_pair(n):
    pair = find_numbers(n)
    p1 = pair[0]
    p2 = pair[1]
    print("The number ", n, " can be written as the sum: ", p1, "+", p2)

def start():
    n=int(input('Please enter n: '))
    if n%2==0 and n>2:  #n must be an even number and greater than two
        print_the_pair(n)
    else:
        print("Goldbach's Hypothesis states that the number given has to be even and greater than 2.")

start()