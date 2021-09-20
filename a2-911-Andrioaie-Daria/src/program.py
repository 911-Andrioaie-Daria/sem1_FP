import math

'''
def read_numbers(n):
    list=[]
    for y in range(0, n):
        r=int(input('Real part:'))
        i=int(input('Imaginary part: \n'))
        list.append(create_complex(r, i))
    return list
'''

#
#Functions that deal with a complex number
#



def create_complex(real, imaginary):
    '''
    Represents the complex number z=a+bi as a dictionary
    :param real: real part
    :param imaginary: imaginary part
    :return:
    '''
    number={'real_part':int(real), 'im_part':int(imaginary)}
    return number


def get_real(number):
    '''
    gets the real part of a complex number, represented as a dictionary
    :param number: the number
    :return:
    '''
    return number['real_part']


def get_imaginary(number):
    '''
    gets the imaginary part of a complex number, represented as a dictionary
    :param number: the number
    :return:
    '''
    return number['im_part']


def to_str(number):
    '''
    turns the complex number into a string of the form a+bi
    :param number:
    :return:
    '''
    a=get_real(number)
    b=get_imaginary(number)
    if b<0:
        return str(a)+' - '+str(-b)+'i'
    return str(get_real(number))+' + '+str(get_imaginary(number))+'i'


#
#Functions related to the two properties
#

def distinct (a, b):
    '''
    Checks if two numbers are different from one another
    :param a: first number
    :param b: second number
    :return: 1, if they are distinct, 0, otherwise
    '''
    if a!=b:
        return 1
    return 0



def prime(x):
    '''
    Checks if a number is prime
    :param x: the number
    :return: 1, if it is prime, 0, otherwise
    '''

    #we have to check if the number is an integer, because the difference of the modulus of two complex numbers might be a float
    if int(x)!=x:
        return 0
    x=int(x)

    #in case he number is negative, we calculate the absolute value
    if x<0:
        x=-x
    if x==0 or x==1:
        return 0

    #checks if the number x is divisible by number in the interval [2, sqrt(x)], in which case it is not prime
    for i in range (2, int(math.sqrt(x))+1):
        if x%i==0:
            return 0
    return 1


def modulus(a):
    '''
    The modulus of a complex number is calculated as the square root of((real_part)^2+(imaginary_part)^2
    :param a: the complex number a
    :return: its modulus
    '''
    return math.sqrt(get_real(a)**2+get_imaginary(a)**2)


def difference_of_modulus(a, b):
    '''
    checks if the difference of the modulus of two numbers is a prime number
    :param a: first number
    :param b: second number
    :return: 1, if the difference is prime, 0, otherwise
    '''
    ma=modulus(a)
    mb=modulus(b)
    if prime(ma-mb):
        return 1
    return 0




#
# Functions dealing with sequences
#


def longest_sequence(list, property):
    '''
    Goes through the list and searches for the start of the longest sequence
    :param list: the list of numbers
    :param property: the property that is to be tested
    :return: a dictionary containing the start and the length of the longest sequence
    '''

    #depending on the property tarnsmited as a parameter, the function will either call the distinct function or the difference_of_modulus
    test={'2':distinct, '3':difference_of_modulus}

    #imax keeps track of the start of the longest sequence up to the cuurent moment, and lmax the length of that sequence
    dict={'imax':0, 'lmax':1}

    #i=an index used to go through the list, l=the length o fthe current sequence, start=the start of the current sequence
    l=1
    i=0
    start=0
    while i<len(list)-1:

        #if two consecutive numbers disple=ay the property, the length is incremented
        if test[property](list[i], list[i+1]):
            l+=1

        #else: it is verified if the sequence that just ended is longer than the last-longest-sequence
        else:
            if l>dict['lmax']:
                dict['lmax'] = l
                dict['imax']=start
            l=1
            start=i+1
        i+=1

    #one last verification, in case that the last sequence is actually the longest
    if l > dict['lmax']:
        dict['imax'] = start
        dict['lmax'] = l

    return dict



#
# UI section
#


#TODO if the length of a sequence is 1, then show a special message
def modulus_ui(numbers, property):
    '''
    Prints the longest sequence with the property that the difference between the modulus of consecutive numbers is a prime number
    :param numbers: the list of numbers
    :param property: the property that is to be tested
    :return:
    '''
    print("\n")
    print('The longest sequence for which the difference between the modulus of consecutive numbers is a prime number is', end=' ')

    sequence=[]                                                             #declares a new list
    dict = longest_sequence(numbers, property)                              #finds the index imax and the length of the longest sequence
    for y in range(dict['imax'], dict['imax'] + dict['lmax']):              #appends the numbers between imax and imax+lmax to the new list
        sequence.append(numbers[y])

    for i in sequence:                                                      #prints each number in the new list
        print(to_str(i), end="  ")
    print("\n")



#TODO if the length of a sequence is 1, then show a special message
def distinct_ui(numbers, property):
    '''
    Works exactly like the function modulus_ui, differing only in the property that is tested for consecutive numbers
    :param numbers: list of numbers
    :param property: the property that is to be tested
    :return:
    '''
    print("\n")
    print('The longest sequence with distinct numbers is', end=' ')

    sequence = []
    dict = longest_sequence(numbers, property)
    for y in range(dict['imax'], dict['imax'] + dict['lmax']):
        sequence.append(numbers[y])

    for i in sequence:
        print(to_str(i), end="  ")
    print("\n")



#TODO put some conditions when displaying a number
def display_list_ui(numbers, property):
    '''
    Prints the list of numbers in a+bi form
    :param numbers: the list of numbers
    :param property:
    :return:
    '''
    for z in numbers:
        print(to_str(z))
    print("\n")



def print_menu():
    '''
    Prints the options available for the user
    :return:
    '''

    print('What action do you want to perform?')
    print('1. Display the list')
    print('2. Display the longest sequence of distinct numbers')
    print('3. Display the longest sequence for which the difference between the modulus of consecutive numbers is a prime number')
    print('0. Exit')


def run():
    commands={'1':display_list_ui, '2':distinct_ui, '3':modulus_ui}
    numbers=[]
    test_init(numbers)
    finished=False
    while not finished:
        print_menu()
        option=input('Enter command:')
        if option in commands.keys():
            commands[option](numbers,option)
        elif option=='0':
            print('See you another time!')
            finished=True
        else:
            print('Sorry. Invalid command')


def test_init(list):
    '''
    Testing-purposed function. Adds numbers to a list
    :param list: the list
    :return:
    '''
    list.append(create_complex(1, 0))
    list.append(create_complex(3, 0))
    list.append(create_complex(5, 0))
    list.append(create_complex(7, 0))
    """
    list.append(create_complex(1, 0))
    list.append(create_complex(1, 0))
    list.append(create_complex(4, 0))
    list.append(create_complex(1, 0))
    list.append(create_complex(4, 0))
    list.append(create_complex(7, 0))
    """
    return list

run()