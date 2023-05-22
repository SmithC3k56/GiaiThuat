import calendar


def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]


if __name__ == "__main__":
    # Get the date from the user.
    arr_input = input().split(' ')

    month = int(arr_input[0])
    day = int(arr_input[1])
    year = int(arr_input[2])
    # Get the day of the week on the given date.
    day_of_week = get_day_of_week(year, month, day)

    # Print the day of the week.
    print(day_of_week.upper())

# input is a string '08 05 2015' result is day of weeks