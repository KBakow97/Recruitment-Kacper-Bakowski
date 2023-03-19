from core.reservations import print_schedule
from core.saving import save_as_csv, save_as_json
from datetime import datetime
import os

now = datetime.now()


def check_file_exist():
    """
    Checking if file reservations.txt is existing by checking on path.
    If yes, starts function for checking old ENDING dates(older than current time)
    """
    path = "./reservations.txt"
    check_file = os.path.isfile(path)
    if not check_file:
        open("reservations.txt", "w")
    else:
        check_old()


def check_old():
    """
    This function checks and removes end dates older than the current date
    """
    with open("reservations.txt", encoding="utf8", mode="r+") as file:
        lines = file.readlines()
        if not lines:
            return "This schedule is empty!"
    with open("reservations.txt", encoding="utf8", mode="w") as file:
        for line in lines:
            (
                _,
                _,
                reservation_booked_end,
            ) = line.strip().split(";")
            reservation_booked_end_date = datetime.strptime(
                reservation_booked_end, "%Y-%m-%d %H:%M:%S"
            )
            if reservation_booked_end_date > now:
                file.write(line)


def checking_dates(d_start=None, d_end=None, reserve_date=None):
    """
    Checking if dates are not old and checks for the end date if it is not lower than the start date
    :param d_start: start date provided by the user
    :param d_end: end date provided by the user
    :param reserve_date: the exact date provided by the user
    """
    if reserve_date is None:
        if d_start.date() < now.date():
            return None
        elif d_start.date() > d_end.date():
            return False
        else:
            return True

    elif d_end is None and d_start is None:
        if reserve_date < now:
            return False
        else:
            return True


def schedule(schedule_type):
    """
    Based on schedule_type(csv or json) returns this type of file
    """
    if schedule_type == "csv" or schedule_type == "json":
        date_start = datetime.strptime(
            input("Insert start date in format (day-month-year): "), "%d-%m-%Y"
        )
        date_end = datetime.strptime(
            input("Insert end date in format (day-month-year): "), "%d-%m-%Y"
        )
        if checking_dates(d_start=date_start, d_end=date_end):
            if schedule_type == "csv":
                return save_as_csv(date_start, date_end)
            else:
                return save_as_json(date_start, date_end)
        elif not checking_dates(d_start=date_start, d_end=date_end):
            return "The start date cannot be later than the end date"
        else:
            return "Please do not enter a past date."
    else:
        return "Wrong choose (csv or json only) "


def menu(choice, reservation=None):
    """
    Based on user choice returns different options
    """
    while choice != "5":
        try:
            match choice:
                case "1":
                    reservation_start = datetime.strptime(
                        input(
                            "Enter the time and date for which you want to reserve the court in format: (hour:min "
                            "day-month-year): "
                        ),
                        "%H:%M %d-%m-%Y",
                    )
                    if checking_dates(reserve_date=reservation_start):
                        print(reservation.apply_reservation(reservation_start))
                    else:
                        print("Please do not enter a past date.")

                case "2":
                    close_reservation = datetime.strptime(
                        input(
                            "Enter the time and date for cancellation in the following format: (hour:min "
                            "day-month-year): "
                        ),
                        "%H:%M %d-%m-%Y",
                    )
                    if checking_dates(reserve_date=close_reservation):
                        print(reservation.cancel_reservation(close_reservation))
                    else:
                        print("Please do not enter a past date.")

                case "3":
                    date_start = datetime.strptime(
                        input("Insert start date in format (day-month-year): "), "%d-%m-%Y"
                    )
                    date_end = datetime.strptime(
                        input("Insert end date in format (day-month-year): "), "%d-%m-%Y"
                    )
                    if checking_dates(d_start=date_start, d_end=date_end):
                        print(print_schedule(date_start, date_end))
                    elif not checking_dates(d_start=date_start, d_end=date_end):
                        print("The start date cannot be later than the end date.")
                    else:
                        print("Please do not enter a past date.")

                case "4":
                    schedule_type = input("Please choose file format for saving schedule: csv/json")
                    print(schedule(schedule_type))

                case _:
                    print("We dont have this option. Try Again :) \n")
            choice = input(
                " What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,"
                "3. Print schedule 4. Download schedule (csv/json)  5. Exit"
            )
        except ValueError:
            print("You entered the wrong data format, please try again!")
            choice = input(
                " What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,"
                "3. Print schedule 4. Download schedule (csv/json)  5. Exit"
            )
