import calendar

calendarObj = calendar.Calendar(0)
day = calendarObj.iterweekdays()
print(str(day))
running = True
while running:

    year, month, day = calendar.weekday(,,13)
    month += 1
    year += 1