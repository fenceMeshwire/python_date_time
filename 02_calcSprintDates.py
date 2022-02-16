#!/usr/bin/env python3

# Python 3.9.5

# Purpose: 
# 1. Calculate the sprint dates for a number of sprints with a defined period for e.g. 15 working days.
# 2. Return the results an check the validity of the result.

# Dependency
import datetime

class SprintDates:
    def __init__(self, begin_sprint, sprints, sprintPeriod):
        self.begin_sprint = begin_sprint
        self.sprints = sprints
        self.sprintPeriod = sprintPeriod

    def calc_sprint_days(self):
        start = self.begin_sprint
        day = datetime.datetime.strptime(start, '%d.%m.%Y')
        sprint = 0
        work_days = 0
        begin_sprint = []
        end_sprint = []
        while sprint < sprints:
            if sprint == 0:
                begin_sprint.append(datetime.datetime.strftime(day, '%d.%m.%Y'))
            else:
                day = day + datetime.timedelta(days=1)
                begin_sprint.append(datetime.datetime.strftime(day, '%d.%m.%Y'))
            while work_days < self.sprintPeriod:
                if day.weekday() in [0, 1, 2, 3, 6]:
                    work_days += 1
                day = day + datetime.timedelta(days=1)
            work_days = 0
            day = day - datetime.timedelta(days=1)
            end_sprint.append(datetime.datetime.strftime(day, '%d.%m.%Y'))
            sprint += 1
        return begin_sprint, end_sprint

class Workdays:

    def __init__(self, begin_sprints, end_sprints):
        self.begin_sprints = begin_sprints
        self.end_sprint = end_sprints 

    def working_days(self):
        start = datetime.datetime.strptime(self.begin_sprints, '%d.%m.%Y')
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

start:str = '01.02.2022' # Start date for the first sprint
sprints:int = 10 # Number of sprints, number > 0
sprintPeriod:int = 15 # Sprint length in days, days > 0
begin_sprints:list = []
end_sprints:list = []
oSprintDates = SprintDates(start, sprints, sprintPeriod)
begin_sprints, end_sprints = oSprintDates.calc_sprint_days()

for i in range(len(begin_sprints)):
    oWorkdays = Workdays(begin_sprints[i], end_sprints[i])
    work_days = oWorkdays.working_days()
    print('Sprint from:', begin_sprints[i], 'to', end_sprints[i], '\tWorking days:', work_days)
