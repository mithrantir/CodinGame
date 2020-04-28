import sys
import math


months = ["Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec"]

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekDays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


def DaysFromStart(month, day, leap):
    ans = day
    for i in range(12):
        if months[i] == month: break
        else:
            if i == 1: ans += leap
            ans += monthDays[i]
    return ans


leap_year = int(input())
source_day_of_week, source_month, source_day_of_month = input().split()
source_day_of_month = int(source_day_of_month)
target_month, target_day_of_month = input().split()
target_day_of_month = int(target_day_of_month)

source = DaysFromStart(source_month, source_day_of_month, leap_year)
target = DaysFromStart(target_month, target_day_of_month, leap_year)

dif = (700 + target - source) % 7

for i in range(7):
    if source_day_of_week == weekDays[i]:
        answer = weekDays[(i + dif) % 7]
        break

print(answer)
