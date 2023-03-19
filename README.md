In this project I've create options that allows user to make a reservation for a tennis court.

The program prompt user what to do:
-Make a reservation
-Cancel a reservation
-Print schedule
-Save schedule to a file
-Exit

I didn't use any additional libraries other than those implemented directly in python, like :
-datetime
-os
-os.path
-csv
-json

Examples:
1 Make a reservation:
Hello, in reservation panel. Remember- don't reserve past time :)
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$ 1
Please insert your name:
$ Kacper Bąkowski
Enter the time and date for which you want to reserve the court in format: (hour:min day-month-year): 
$ 17:30 19-03-2023
For how long ? 1) 30 min 2) 60 min 3) 90min
$ 2
Kacper Bąkowski reserved place 2023-03-19 17:30:00, end 2023-03-19 18:30:00



2 Cancel a reservation:
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$ 2
Enter the time and date for cancellation in the following format: (hour:min day-month-year):
$ 17:30 19-03-2023
Reservation deleted!
Have a good day :)


3.Print schedule:
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$ 3
Please insert your name: 
$ Kacper
Insert start date in format (day-month-year): 
$ 19-03-2023
Insert end date in format (day-month-year): 
$ 22-03-2023
Today:
* Kacper Dump, start: 2023-03-19 22:40:00, end: 2023-03-19 23:40:00
* Kacper Dump, start: 2023-03-19 15:45:00, end: 2023-03-19 16:45:00
* Olan, start: 2023-03-19 20:30:00, end: 2023-03-19 22:00:00
Tomorrow:
* Adam B, start: 2023-03-20 17:40:00, end: 2023-03-20 18:40:00
* Ola, start: 2023-03-20 19:30:00, end: 2023-03-20 21:00:00
* Kacper, start: 2023-03-20 21:10:00, end: 2023-03-20 22:10:00
* Paweł, start: 2023-03-20 22:20:00, end: 2023-03-20 23:20:00
Tuesday(2023-03-21):
No Reservations
Wednesday(2023-03-22):
No Reservations
Hope this schedule is accessible for You :)



4.Save schedule to a file (example files added):
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$4
Please choose file format for saving schedule: csv/json
$ csv
Insert start date in format (day-month-year): 
$ 19-03-2023
Insert end date in format (day-month-year): 
$ 23-03-2023
After closing program please check folder for your file :)
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$ 4
Please choose file format for saving schedule: csv/json
$ json
Insert start date in format (day-month-year): 
$ 19-03-2023
Insert end date in format (day-month-year): 
$ 23-03-2023
After closing program please check folder for your file :)
What you want to do(select number) : 1. Make a reservation, 2. Cancel a reservation,3. Print schedule 4. Download schedule (csv/json)  5. Exit
$5
Thanks for using our program!


When user add wrong data or option is looped back to menu with information what is wrong.
In OOP I've created only 2 metods because i thought it will be enought.
I also split the functions into different files to make them easier to read and understand.

I hope that the work I have done is satisfactory and I look forward to further contact.
Kacper Bąkowski







