#
# Implement the program to solve the problem statement from the third set here

#Problem 12. Determine the age of a person, in number of days.

'''
Program description:
Imagining a 'year axis' where we place the birth date and the current date, the program calculates
the sum of all the days in the years between the birth year and the current year, then 'crops' the ends
such that it eliminates the number of days from the start of the birth year until the birth day
and the remaining days from the current day to the end of the year.
'''


def days_until(day, month, year):
    """
    Calculates the number of days from the start of the year to the date entered as a parameter
    :param day: the day
    :param month: the month
    :param year: the year
    :return: the number of days
    """
    days=0

    #we add 30 or 31 days for each month previous to the current one, according to their parity
    for i in range (1, month):
        if i<8:             #months before august
            if i%2==0:
                days+=30
            else:
                days+=31
        else:               #months after august, august including
            if i%2==1:
                days+=30
            else:
                days+=31
    if month>2:            #if the month is past february, we take into account that Februasry has 29 days
        if year%4==0:      #if the year is a multiple of 4 and 28, otherwise
            days-=1
        else:
            days-=2
    days+=day            #add the days of the current month
    return days


def days_left(day, month, year):
    """
    Calculates the number of days left in the year, starting from the date entered as a parameter
    :param day: the day
    :param month: the month
    :param year: the year
    :return: the days left
    """
    #first add the total o days of the whole year
    if year%4==0:
        days=366
    else:
        days=365

    #subtract the days from the start of the year from the total
    days-=days_until(day, month, year)
    return days


def whole_years(y1, y2):
    """
    Calculates the total of days in the years from the one year to another
    :param by: birth year
    :param cy: current yaer
    :return: number of days
    """
    alive=0;
    for y in range(y1, y2+1):
        if y % 4 == 0:       #leap year
            alive += 366
        else:                #otherwise
            alive += 365
    return alive

def calculate(date1, date2):
    """
    Calculates the days between date1 and date2
    """

    alive = whole_years(date1['year'], date2['year'])
    alive -= days_until(date1)
    alive -= days_left(date2)
    # alive+=1 this is optional, depending on whether we want to include the current day or not
    return alive

def show_result(date1, date2):
    """
    Prints the result.
    """
    alive_days=calculate(date1, date2)
    print("Jimmy has been alive for ", alive_days, " days.")

def read_birth_date():
    print("Please enter Jimmy's birth date")
    dict['day']=int(input('Day: '))
    dict['month'] = int(input('Month: '))
    dict['year'] = int(input('Year: '))
    return dict

def read_current_date():
    print('Please enter the current date')
    dict['day'] = int(input('Day: '))
    dict['month'] = int(input('Month: '))
    dict['year'] = int(input('Year: '))
    return dict


def start():
    birth = read_birth_date()
    current = read_current_date()
    show_result(birth, current)

start()