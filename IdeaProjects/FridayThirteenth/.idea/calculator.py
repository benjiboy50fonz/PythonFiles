import calendar

calendarObj = calendar.Calendar(0)
day = calendarObj.iterweekdays()
print(str(day))
running = True
year = 1971
month = 1
dates = {0:'Monday',
         1:'Tuesday',
         2:'Wednesday',
         3:'Thursday',
         4:'Friday',
         5:'Saturday',
         6:'Sunday',
         }

months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
            }

year = input(str('Start year: '))
year = int(year)

for i in range(5):
    month = 1
    for i in range(1, 13):
        weekdayName = calendar.weekday(year, month, 13)
        if dates[weekdayName] == 'Friday':
            print('The Friday of ' + str(months[month]) + ', ' + str(year) +' is a thirteenth')
            year += 1
        month += 1

