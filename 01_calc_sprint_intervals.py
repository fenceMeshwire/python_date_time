#!/usr/bin/env python3

# Python 3.9.5

# 01_days_between.py

# Purpose: Calculate the number of working days for a sprint period.

# Dependency
import datetime

class Workdays:
    def __init__(self, begin_sprint, end_sprint):
        self.begin_sprint = begin_sprint
        self.end_sprint = end_sprint 

    def working_days(self):
        start = datetime.datetime.strptime(self.begin_sprint, '%d.%m.%Y')
        end = datetime.datetime.strptime(self.end_sprint, '%d.%m.%Y')
        total_days = abs((end - start).days)
        upcount = 0
        day = start
        work_days = 0
        while upcount <= total_days:
            upcount += 1
            if day.weekday() in [0, 1, 2, 3, 6]: # A weekday is a day within the list.
                work_days += 1
            day = day + datetime.timedelta(days=1)
        return work_days

begin_sprint = '02.08.2022'
end_sprint = '22.08.2022'

oWorkdays = Workdays(begin_sprint, end_sprint)
work_days = oWorkdays.working_days()
work_days # Returns the number of working days
