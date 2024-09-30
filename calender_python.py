import calendar 

def display_calendar (year,month):
    cal=calendar.TextCalendar(calendar.SUNDAY)
    calen=cal.formatmonth(year,month)
    print(calen)

print("Enter the year and month to display the calendar:")
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))

display_calendar(year,month)

