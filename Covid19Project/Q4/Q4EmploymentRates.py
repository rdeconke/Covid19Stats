#!/usr/bin/env python

# Question 4 - How does the pandemic affect employment rates?

# 1. search through data within users date range
# 2. for every month in the users date:
#    a) make a list of the full time, part time, and unemployed number of people
#    b) make a list of the total population
# 3. calculate the average percentage of the population is employed full time, part time, and unemployed
# 4. visualize using a bar graph

import sys
import csv
import re

def main(argv):
  
  if len(argv) != 3:
    print("Usage:", "Q4/Q4EmploymentRates.py <Start date YYYY-MM> <End date YYYY-MM>")
    sys.exit(-1)
    # User enters start and ending month

  employment_file = open("data/employmentRate.csv", encoding="utf-8-sig")
  employment_reader = csv.reader(employment_file)

  # make sure user inputs a valid date in command line
  try:
    startDate = (argv[1])
    startDate = (int)(re.sub('[-]', '', startDate))
  except ValueError as err:
    print("Usage:", "Q4/Q4EmploymentRates.py <Start date YYYY-MM> <End date YYYY-MM>")
    sys.exit(-1)
  
  try:
    endDate = (argv[2])
    endDate = (int)(re.sub('[-]', '', endDate))
  except ValueError as err:
    print("Usage:", "Q4/Q4EmploymentRates.py <Start date YYYY-MM> <End date YYYY-MM>")
    sys.exit(-1)
  
  dateList = []
  populationList = []
  unemploymentList = []
  fullTimeList = []
  partTimeList = []
  employeeCount = 0
  numInfo = 0
  
  # 1. search through data within users date range
  for rows in employment_reader:
    
    if employeeCount != 0:
    # labels in first line
    
      tempDate = rows[0]
      tempDate = (int)(re.sub('[-]', '', tempDate))
      # convert date into an integer to compare
      
      if tempDate <= endDate and tempDate >= startDate:
      # between user input range
        
        # 2. list of date, full time and part time employement, and unemployment
        if rows[1] == "Population":
          populationList.append((float)(rows[2]))

          dateList.append(rows[0])
          numInfo += 1
          # only count everything once

        elif rows[1] == "Full-time employment":
          fullTimeList.append((float)(rows[2]))
        elif rows[1] == "Part-time employment":
          partTimeList.append((float)(rows[2]))
        elif rows[1] == "Unemployment":
          unemploymentList.append((float)(rows[2]))

    employeeCount += 1

  
  if numInfo == 0:
    print("Unable to find data for {} - {}". format(argv[1], argv[2]))
    sys.exit(-1)

  print("Employment Summary for {} - {}".format(argv[1], argv[2]))
  print("Date,Type,Percentage")

  # 3. calculate and display percentages
  for i in range(numInfo):
    fullTime = (fullTimeList[i] / populationList[i]) * 100.00
    partTime = (partTimeList[i] / populationList[i]) * 100.00
    unemployed = (unemploymentList[i] / populationList[i]) * 100.00
    print("{},{},{:.2f}". format(dateList[i], "Full time", fullTime))
    print("{},{},{:.2f}". format(dateList[i], "Part time", partTime))
    print("{},{},{:.2f}". format(dateList[i], "Unemployed", unemployed))

# 4. visualize
# python Q4/Q4EmploymentRates.py <Start date YYYY-MM> <End date YYYY-MM>
# python Q4/Q4EmploymentRates.py <Start date> <End date> Q4/q4.csv
# python Q4/Q4Plot.py Q4/q4.csv Q4/q4.pdf

main(sys.argv)