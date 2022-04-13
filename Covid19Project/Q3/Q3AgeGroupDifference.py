#!/usr/bin/env python

# Question 3 - What age group is affected most by the virus?

# 1. keep track of cases until the user input date
# 2. add all averages (for each age group), divide averages by count
# 3. print age group and corresponding average leading up to users date of interest
# 4. visualize using bar graph

import sys
import csv
import re

def main(argv):

  age_cases = open("data/ageGroupCases.csv", encoding="utf-8-sig")
  age_reader = csv.reader(age_cases)

  if len(argv) != 2:
    print("Usage: Q3/Q3AgeGroupDifference.py <YYYY-MM-DD>")
    sys.exit(-1)

  # make sure user inputs a valid date in command line
  try:
    userDate = argv[1]
    userDate = (int)(re.sub('[-]', '', userDate))
  except ValueError as err:
    print("Usage: Q3/Q3AgeGroupDifference.py <YYYY-MM-DD>")
    sys.exit(-1)
  
  age13Avg = 0
  age17Avg = 0
  age24Avg = 0
  age64Avg = 0
  age65Avg = 0
  ageCount = 0
  count = 0 # to count # of averages

  for rows in age_reader:
    if ageCount != 0:
      tempDate = rows[0]
      tempDate = (int)(re.sub('[-]', '', tempDate))

      if (tempDate <= userDate):
        # date must be before input date
        if (rows[1] == "0to13"): # add up average for each age group
          count = count + 1 # number of times an average was added
          age13Avg += float(rows[2])
        elif (rows[1] == "14to17"):
          age17Avg += float(rows[2])
        elif (rows[1] == "18to24"):
          age24Avg += float(rows[2])
        elif (rows[1] == "25to64"):
          age64Avg += float(rows[2])
        elif (rows[1] == "65+"):
          age65Avg += float(rows[2])
    ageCount += 1

  if age13Avg == 0 and age17Avg == 0 and age24Avg == 0 and age64Avg == 0 and age65Avg == 0:
    print("Unable to find data for {}". format(argv[1]))
    sys.exit(-1)

  # average for each age group leading up to users date:
  age13Avg = (age13Avg / count) 
  age17Avg = (age17Avg / count)
  age24Avg = (age24Avg / count)
  age64Avg = (age64Avg / count)
  age65Avg = (age65Avg / count)

  # print statements:
  print("Positive Tested Cases on {} by Age Group".format(argv[1]))
  print("Age group,Average Percent Testing postive up to entered date")
  print("{},{:.2f}".format("0 - 13", age13Avg))
  print("{},{:.2f}".format("14 - 17", age17Avg))
  print("{},{:.2f}".format("18 - 24", age24Avg))
  print("{},{:.2f}".format("25 - 64", age64Avg))
  print("{},{:.2f}".format("65+", age65Avg))

# 4. visualize
# python Q3/Q3AgeGroupDifference.py <Date>
# python Q3/Q3AgeGroupDifference.py <Date> > Q3/q3.csv
# python Q3/Q3Plot.py Q3/q3.csv Q3/q3.pdf

main(sys.argv)