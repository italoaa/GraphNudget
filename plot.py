#!/usr/bin/env python3

import csv
from uniplot import plot

entries=[]


# format : YYYYMMDDHHMMSS
originday = 20220200000001

with open('./data.csv') as datafile:
    readdata =  csv.reader(datafile, delimiter=',')
    line_count = 0
    for row in readdata:
        if line_count != 0:
            entries.append({"DATE":row[0],"COST":row[1],"TAG":row[2],"id":line_count})
        line_count += 1

def DateToNumber(date):
    # dateformat : YYYY-MM-DD HH:MM:SS +xxxx
    # numberformat : days.time (10.5) relative 10 days to id 1 plus 5 hours
    days, time, offset = date.split()
    hours, minutes, seconds = time.split(':')
    days = days.replace("-","")
    output = f"{days}{hours}{minutes}{seconds}"
    return int(output)

def MakeRelativeDate(date):
    return date - originday

for entry in entries:
    entry['DATE'] = DateToNumber(entry['DATE'])
    entry['DATE'] = MakeRelativeDate(entry['DATE'])
    entry['COST'] = float(entry['COST'])

date = [entry['DATE'] for entry in entries]
costs = [entry['COST'] for entry in entries]
budgetchange = [250]


budget = 250
for cost in costs:
    budgetchange.append(budget-cost)
    budget = budget-cost

budgetchange.remove(250)

ylines = [x for x in range(250,0,-10)]

plot(xs=date,ys=budgetchange,y_unit=" £",y_gridlines=ylines,lines=True,height=25,title="Spending money over time")
