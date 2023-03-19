from datetime import datetime, timedelta
import os.path

now = datetime.now()
borderline_time = now + timedelta(hours=1)


def print_schedule(d_start, d_end):
    """
    Print in console schedule based on start_date and end date
    :param d_start: start date provided by the user
    :param d_end: end date provided by the user
    """
    with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r") as file:
        lines = file.readlines()
        # If file is empty
        if not lines:
            return "This schedule is empty!"
        # Adding up the number of given days
        day_count = (d_end - d_start).days + 1
        for single_day in (d_start + timedelta(n) for n in range(day_count)):
            counter = 0
            empty = True
            for line in lines[:-1]:
                reserve_name, s_reserve, e_reserve = line.strip().split(";")
                reservation_date = datetime.strptime(s_reserve, "%Y-%m-%d %H:%M:%S")
                # Checking how close date is to current
                if counter == 0:
                    counter += 1
                    delta = single_day.day - now.day

                    if delta == 0:
                        print("Today:")
                    elif delta == 1:
                        print("Tomorrow:")
                    else:
                        print(f"{single_day.strftime('%A')}({single_day.date()}):")
                # Printing every line in this time interval
                if single_day.date() == reservation_date.date():
                    empty = False
                    print(
                        f"* {reserve_name}, start: {s_reserve}, end: {e_reserve}"
                    )
            if empty:
                print("No Reservations")
        return f"Hope this schedule is accessible for You :)"


def reservation_count(name, new_reserve_start, lines):
    """
    Checking if same user don't have in this week too many reservations. If reservation is later than week
    can be added
    :param name: Username
    :param new_reserve_start: Date implemented by user
    :param lines: lines from file

    """
    counter = 0  # counting how many times this user is already registered
    for line in lines:
        (
            booked_name,
            reserve_booked_start,
            _,
        ) = line.strip().split(";")
        # Checking if the same user don't have more than 2 reservations this week
        if name == booked_name:
            reserve = datetime.strptime(
                reserve_booked_start, "%Y-%m-%d %H:%M:%S")
            day_count = (reserve - now).days + 1
            new_day_count = (new_reserve_start - now).days + 1
            if new_day_count > 7:
                return False
            if day_count <= 7:
                counter += 1
                if counter >= 2:
                    return True


def overlapping_time(name, new_reserve_start, new_reserve_end):
    """
    :param name: Username
    :param new_reserve_start: Date implemented by user
    :param new_reserve_end: Ending date implemented by user
    """
    with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r+") as file:
        lines = file.readlines()
        for line in lines:
            (
                booked_name,
                reserve_booked_start,
                reserve_booked_end,
            ) = line.strip().split(";")
            # Checking if the given date does not conflict with others
            if (
                    reserve_booked_start
                    <= str(new_reserve_start)
                    <= reserve_booked_end
            ) or (
                    reserve_booked_start
                    <= str(new_reserve_end)
                    <= reserve_booked_end

            ):
                print(
                    f"{booked_name} already reserved place {reserve_booked_start}, end {reserve_booked_end}"
                )
                # making propose date
                proposed_date = datetime.strptime(
                    reserve_booked_end, "%Y-%m-%d %H:%M:%S"
                ) + timedelta(minutes=10)
                propose_accept = input(
                    f" We can give you a reservation at date: {proposed_date}. yes/no"
                )
                if propose_accept == "yes":
                    how_long = int(
                        input("For how long ? 1) 30 min 2) 60 min 3) 90min ")
                    )
                    if how_long in (1, 2, 3):
                        propose_end = proposed_date + timedelta(
                            minutes=30 * how_long
                        )
                        file.write(
                            f"{name};{proposed_date};{propose_end}\n"
                        )
                        print(f"{name} reserved place {proposed_date}, end {propose_end}")
                        return True
                    else:
                        print("No such option")
                        return True
                else:
                    print("Understand, choose other date")
                    return True

        return None


class Reservations:
    def __init__(self, name):
        self.name = name

    def apply_reservation(self, new_reserve_start):
        """
        We check the reservations in the file, whether the given
        time is already taken, if so, we suggest another one, if we do not book a place
        :param new_reserve_start: date and time provided by the user
        """
        with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r+") as file:
            lines = file.readlines()
            # If file is empty
            if not lines:
                how_long = int(input("For how long ? 1) 30 min 2) 60 min 3) 90min "))
                if how_long in (1, 2, 3):
                    new_reserve_end = new_reserve_start + timedelta(
                        minutes=30 * how_long)
                    file.write(
                        f"{self.name};{new_reserve_start};{new_reserve_end}\n"
                    )
                    return f"{self.name} reserved place {new_reserve_start}, end {new_reserve_end}"
            # Checking for more than two reservations this week
            if reservation_count(self.name, new_reserve_start, lines):
                return "No one can have more than 2 reservations per week"
            how_long = int(
                input("For how long ? 1) 30 min 2) 60 min 3) 90min ")
            )
            # Adding
            if how_long in (1, 2, 3):  # adding end time so that the times don't overlap
                new_reserve_end = new_reserve_start + timedelta(
                    minutes=30 * how_long
                )
                # Checking for conflicts
                overlapping = overlapping_time(self.name, new_reserve_start, new_reserve_end)
                if overlapping is None:
                    # If there was no conflict simply add date to schedule
                    file.write(f"{self.name};{new_reserve_start};{new_reserve_end}\n")
                    return f"{self.name} reserved place {new_reserve_start}, end {new_reserve_end}"
                else:
                    return "Thanks for registration"
            else:
                return "No such option"

    def cancel_reservation(self, close_reserve):
        """
        We check whether there is a reservation for the given time and date,
         if there is more than an hour from the current time, we remove it.
        :param close_reserve: date and time provided by the user
        """
        close = False
        with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r+") as file:
            lines = file.readlines()
            # If file is empty
            if not lines:
                return "This schedule is empty!"
        with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="w") as file:
            for line in lines:
                (
                    booked_name,
                    reservation_booked_start,
                    reservation_booked_end,
                ) = line.strip().split(";")
                reservation_booked_start_date = datetime.strptime(
                    reservation_booked_start, "%Y-%m-%d %H:%M:%S"
                )
                # First checking if name is same as in schedule
                if booked_name != self.name:
                    file.write(line)
                else:
                    # Next check - if the date is same as in schedule and if its no closer than 1 hour to current time
                    if (
                            close_reserve == reservation_booked_start_date
                            and reservation_booked_start_date >= borderline_time):
                        close = True
                        print("Reservation deleted!")
                    elif close_reserve == reservation_booked_start_date \
                            and reservation_booked_start_date < borderline_time:
                        file.write(line)
                        print("Too late, you can't cancel the reservation")
                        close = True
                    else:
                        close = True
                        file.write(line)
            if not close:
                return "There is no reservation on your name and date"
        return "Have a good day :)"
