from datetime import datetime, timedelta
import csv
import json
import os


def save_as_csv(d_start, d_end):
    """
    Creates and saves to .csv chosen reservations based on start_date and end date
    :param d_start: start date provided by the user
    :param d_end: end date provided by the user
    """
    with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r+") as file:
        lines = file.readlines()
        # If file is empty
        if not lines:
            return "This schedule is empty!"
        header = ["Name", "Start Date", "End Date"]
        data = {}
        day_count = (d_end - d_start).days + 1
        # Create a file named time period
        with open(
                f"{d_start.strftime('%d')}.{d_start.strftime('%m')}-{d_end.strftime('%d')}.{d_end.strftime('%m')}",
                encoding="utf8",
                mode="w",
                newline="",
        ) as f:
            writer = csv.writer(f)
            # Adding header to first line
            writer.writerow(header)
            for single_date in (d_start + timedelta(n) for n in range(day_count)):
                for line in lines:
                    reserve_name, s_reserve, e_reserve = line.strip().split(
                        ";"
                    )
                    data["reservation_name", "reservation", "end_reservation"] = (
                        reserve_name,
                        s_reserve,
                        e_reserve,
                    )
                    reserve_date = datetime.strptime(
                        s_reserve, "%Y-%m-%d %H:%M:%S"
                    )
                    # checking if single date is matching dates in reservations
                    if single_date.date() == reserve_date.date():
                        writer.writerow(
                            data["reservation_name", "reservation", "end_reservation"]
                        )
    return "After closing program please check folder for your file :)"


def save_as_json(d_start, d_end):
    """
    Creates and saves to .json chosen reservations based on start_date and end date
    :param d_start: start date provided by the user
    :param d_end: end date provided by the user
    """
    with open(os.path.dirname(__file__) + "/../reservations.txt", encoding="utf8", mode="r") as file:
        lines = file.readlines()
        # If file is empty
        if not lines:
            return "This schedule is empty!"
        # Create a file named time period
        with open(
                f"{d_start.strftime('%d')}.{d_start.strftime('%m')}-{d_end.strftime('%d')}.{d_end.strftime('%m')}.json",
                encoding="utf8", mode="w+") as json_file:
            dates = {}
            day_count = (d_end - d_start).days + 1
            for single_day in (d_start + timedelta(n) for n in range(day_count)):
                empty = True  # If in this day there are no reservations makes empty list
                day_month = f"{single_day.strftime('%d')}.{single_day.strftime('%m')}"
                daily_info = list()
                for line in lines[:-1]:
                    reserve_name, s_reserve, e_reserve = line.strip().split(";")
                    s_reserve_date = datetime.strptime(s_reserve, "%Y-%m-%d %H:%M:%S")
                    e_reserve_date = datetime.strptime(s_reserve, "%Y-%m-%d %H:%M:%S")
                    if single_day.date() == s_reserve_date.date():
                        empty = False
                        # Writing time to a variable in json format
                        client_data = {"name": reserve_name,
                                       "start_time": f"{s_reserve_date.hour}:{s_reserve_date.minute}",
                                       "end_time": f"{e_reserve_date.hour}:{e_reserve_date.minute}"
                                       }
                        daily_info.append(client_data)
                        dates[day_month] = daily_info
                if empty:
                    dates[day_month] = []
            # Updating json file
            json_file.write(json.dumps(dates, indent=2))
    return "After closing program please check folder for your file :)"
