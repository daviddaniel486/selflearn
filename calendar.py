"""
File: calendar.py
-----------------
This program prints out a calendar, to show the days of the
week in each month.
"""

NUM_MONTHS = 12
NUM_DAYS_IN_WEEK = 7


def is_leap_year(year):
    """
    Returns Boolean indicating if given year is a leap year.
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def days_in_month(month, year):
    """
    Returns the number of days in the given month and year.
    Assumes that month 1 is January, month 2 is February, and so on.
    """
    # Days in February depends on whether it's a leap year
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    # April, June, September, November have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    # All other months have 31 days
    else:
        return 31


def print_month_header(month):
    month_name = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }
    month = month_name.get(month)
    print(str(month))
    print("Sun Mon Tue Wed Thu Fri Sat")
def format_number(num):
    """
    Formats a one or two digit integer to fit in four spaces.
    Returns a string of the formatted number string.
    """
    result = " " + str(num) + " "
    if num < 10:
        result = result + " "
    return result


def print_month(first_day, month, year):
    """
    Prints a daily calendar for the given month and year.  It is
    also given the day of the week that this month starts on
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)

    Returns the day of the week that the *following* month would start on
    """
    print_month_header(month)
    days = days_in_month(month, year)

    # Print leading space before the first day in this month
    for i in range(first_day):
        print("    ", end="")       # four spaces per day

    # Print numbers for all the days in the month
    for i in range(0, days):
        print(format_number(i + 1), end="")
        # Add a new line at end of the week
        if ((first_day + i) % NUM_DAYS_IN_WEEK) == (NUM_DAYS_IN_WEEK - 1):
            print("")
    # Add a new line at the end of the month
    print("")

    # Return day of week for first day for the month after this one
    return (first_day + days) % NUM_DAYS_IN_WEEK


def first_day_of_year(year):
    """
    Returns the first day of the week for a given year, where
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    The formula in this function comes from http://mathforum.org/
    >>> first_day_of_year(2020)
    3
    """
    year -= 1
    return (year + (year // 4) - (year // 100) + (year // 400) + 1) % NUM_DAYS_IN_WEEK


def main():
    """
    Prints calendar for the year entered by the user
    """
    year = int(input("Enter year for calendar: "))
    first_day = first_day_of_year(year)

    # Loop through months 1 through 12
    for month in range(1, NUM_MONTHS + 1):
        first_day = print_month(first_day, month, year)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()