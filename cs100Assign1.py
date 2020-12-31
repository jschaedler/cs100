# input seconds
# output number of days, hours, minutes, and seconds
# Author: Joseph Schaedler

seconds_left = int(input("Enter the amount of time in seconds:\n"))

day_count = seconds_left // 86400
seconds_left %= 86400

Hour_count = seconds_left // 3600
seconds_left %= 3600

minute_count = seconds_left // 60
seconds_left %= 60

print(day_count, "days")
print(Hour_count, "hours")
print(minute_count, "minutes")
print(seconds_left, "seconds")
