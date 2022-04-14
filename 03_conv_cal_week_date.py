#!/bin/env python3

# Python 3.9.7

# 03_conv_cal_week_date.py

# Purpose: Convert the date dd.mm.yyyy into yyyymmww

# Dependency
from datetime import datetime

def convert_date(date):
    date_convert = datetime.strptime(date, '%d.%m.%Y')
    year = date_convert.year
    month = date_convert.month
    cal_week = date_convert.isocalendar()[1]

    if month < 10:
        month = "0" + str(month)
    if cal_week < 10:
        cal_week = "0" + str(cal_week)
    cal_week_date = str(year) + str(month) + str(cal_week)

    return cal_week_date

if __name__ == '__main__':
    date = '14.04.2022'
    cal_week_date = convert_date(date)
    print(cal_week_date)
