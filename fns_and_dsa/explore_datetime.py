# Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.
from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)



user = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = datetime.date.today() + datetime.timedelta(days=user)
    print("Future date:", future_date)


display_current_datetime()
calculate_future_date()