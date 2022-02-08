#!/usr/bin/env python3

# Python 3.9.5

# 04_strftime.py

# Dependencies
import time
lt = time.localtime()
type(lt)
len(lt) # equals 9

print('Contents of time.localtime() list')
for i in range(9):
    print(lt[i])

print('Year', lt[0])
print('Month', lt[1])
print('Day', lt[2])
print('Hour', lt[3])
print('Minute', lt[4])
print('Second', lt[5])
print('Day of the week', lt[6])
print('Day of the year', lt[7])

print('Basic date')
print(time.strftime('%Y', lt)) # Year 4 digits
print(time.strftime('%y', lt)) # Year 2 digits
print(time.strftime('%m', lt)) # Month 2 digits
print(time.strftime('%d', lt)) # Day 2 digits

print('Basic time')
print(time.strftime('%H', lt)) # Hour 2 digits
print(time.strftime('%M', lt)) # Minute 2 digits
print(time.strftime('%S', lt)) # Second 2 digits

print('Calendar week')
print(time.strftime('Begin on sunday: %U', lt))
print(time.strftime('Begin on monday: %W)', lt))
print(time.strftime('According to ISO 8601: %V', lt)) # To be prefered

print('Time zone')
print(time.strftime('timezone: %Z', lt))

print('Days of the week')
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_day_number = lt[6]
week_days[week_day_number] # Returns the day of the week for the current lt = time.localtime()
