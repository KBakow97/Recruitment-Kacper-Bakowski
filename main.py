from core.reservations import Reservations
from Recruitment.menu_with_checks import check_file_exist, menu

if __name__ == "__main__":
    print("Hello, in reservation panel. Remember- don't reserve past time :)")

    num = input(
        " What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,"
        "3. Print schedule 4. Download schedule (csv/json)  5. Exit"
    )
    if num == "5":
        quit("Bye!")
    client_name = input(" Please insert your name: ").title()
    reservation = Reservations(name=client_name)
    check_file_exist()
    menu(num, reservation)
    print("Thanks for using our program!")
