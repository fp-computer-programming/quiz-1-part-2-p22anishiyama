# Author: ATN 10/19/21

year_of_century = int(input("Enter the year of the date: ")) + 1
month = int(input("Enter the month of the date: "))
day_of_month = int(input("Enter the day of the date: "))
century = year_of_century // 100

# All division is rounded
day_of_week = (day_of_month + ((26 * (month + 1)) // 10) + year_of_century + (year_of_century // 4) + (century // 4) + 5 * century) % 7

if(day_of_week == 0):
    day_of_week = ("Saturday")
elif(day_of_week == 1):
    day_of_week = ("Sunday")
elif(day_of_week == 2):
    day_of_week = ("Monday")
elif(day_of_week == 3):
    day_of_week = ("Tuesday")
elif(day_of_week == 4):
    day_of_week = ("Wednesday")
elif(day_of_week == 5):
    day_of_week = ("Thursday")
elif(day_of_week == 6):
    day_of_week = ("Friday")

# January / February
if(month >= 13):
    year_of_century -= 1

# Somehow changing the year of the century twice made the solution work. Maybe the year is wrong?
year_of_century -= 1

print(str(month) + "/" + str(day_of_month) + "/" + str(year_of_century) + " was a " + str(day_of_week))
