#!/usr/bin/env python

# Question 1 - Are rising cases due to reopening of schools? What percentage of covid cases are due to the reopening of schools?

# school cases file: row data value [0] = date
#                    row data value [1] = total cases
# total cases file: row data value [2] = date

# 1. order the total case file by date, using a list and .sort()
# 2. compare the cumulative date to the school cases date
#    a) take school date, go through the total date until the school date is <= total date
# 3. if there is a match, print:
#     a) date
#     b) % of school to total cases
# 4. visualize using bar plot

import sys
import csv
import re

def main(argv):

  # 1. open, order, store csv files
  
  total_cases_file = open("data/conposcovidloc.csv", encoding="utf-8-sig")
  total_cases_reader = csv.reader(total_cases_file)

  total_school_file = open("data/schoolCases.csv", encoding="utf-8-sig")
  total_school_reader = csv.reader(total_school_file)
  
  subList = []
  dataList = []
  dataCount = 0
  schoolList = []
  schoolCount = 0

  for rows in total_cases_reader:
    if dataCount != 0:
      tempDate = rows[2]
      tempDate = re.sub('[-]', '', tempDate)
      # convert date into an integer to compare

      dataList.append(int(tempDate))
      # ['infectionDate']
      # full data list of all row info
    dataCount += 1 # number of total cases

  dataList.sort()
  # sort function can properly sort each row (aka subList in the main list) by date

  for rows in total_school_reader:
    if schoolCount != 0:
      tempDate = rows[0]
      endDate = tempDate
      tempDate = re.sub('[-]', '', tempDate)
      
      subList.append((int)(tempDate))   
      subList.append(rows[1])
      # subList = each row in csv file
      # ['infectionDate', 'number of school cases']
      schoolList.append(subList)
      # full data list of all row info
      subList = []
    if (schoolCount == 1):
      startDate = rows[0]
    schoolCount += 1

  # 2. compare the dates
  print("Percentage of School Cases from {} - {}" .format(startDate, endDate))

  print("Date,Percentage")
  
  # process through data
  for i in range (schoolCount - 1):
    schoolDate = schoolList[i][0]
    schoolCases = schoolList[i][1]

    for j in range (dataCount - 2):
      totalDate = dataList[j]
      totalCases = j

      # 3. print output
      if (totalDate == schoolDate and dataList[j+1] != schoolDate):
        percentCases = ((int(schoolCases)) / (int(totalCases)) * 100)
        # print("{},{},{}".format(totalDate,'Total',totalCases))
        # print("{},{},{}".format(totalDate,'School',schoolCases))

        # use slice syntax in python to convert the integers into a string date format
        stringDate = str(totalDate)
        stringDate = stringDate[:4] + "-" + stringDate[4:]
        stringDate = stringDate[:7] + "-" + stringDate[7:]
        print("%s,%0.2f" % (stringDate, percentCases))
        break
      elif (totalDate > schoolDate):
        percentCases = ((int(schoolCases)) / (int(totalCases)) * 100)
        # print("{},{},{}".format(dataList[j - 1],'Total',dataList[j - 1][1]))
        # print("{},{},{}".format(dataList[j - 1],'School',schoolCases))

        # use slice syntax in python to convert the integers into a string date format
        stringDate = str(dataList[j - 1])
        stringDate = stringDate[:4] + "-" + stringDate[4:]
        stringDate = stringDate[:7] + "-" + stringDate[7:]
        print("%s,%0.2f" % (stringDate, percentCases))
        break

# 4. visualize
# python Q1/Q1SchoolTotal.py
# python Q1/Q1SchoolTotal.py > Q1/q1.csv
# python Q1/Q1Plot.py Q1/q1.csv Q1/q1.pdf

main(sys.argv)