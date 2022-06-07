#!/usr/bin/env python3

# Python 3.9.7

# 04_datetime_usage.py

# Dependencies
from datetime import datetime, timedelta

firstDayOfYear = datetime(2022, 1, 1)
firstSummerDay = datetime(2022, 6, 21)

diff_days = firstSummerDay - firstDayOfYear
diff_days += timedelta(1)

days = diff_days.days
days
