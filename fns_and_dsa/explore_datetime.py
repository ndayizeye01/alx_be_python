import datetime


def display_current_datetime():
    return datetime.datetime.now()

current_date = display_current_datetime()
print(f"Current date and time: {current_date}")

days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    return datetime.date.today() + datetime.timedelta(days=days)

future_date = calculate_future_date()
print(f"Future date: {future_date}")