from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


weekdays = (Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY)
weekends = (Weekday.SATURDAY, Weekday.SUNDAY)

weekday_wake_up = "7am"
weekend_wake_up = "9am"

for day in Weekday:
    print(f'Today is {day.name.capitalize()}')
    wake_time = weekday_wake_up if day in weekdays else weekend_wake_up
    print(f'Wake up at {wake_time}\n')
