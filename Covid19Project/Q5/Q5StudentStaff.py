#!/usr/bin/env python

# Question 5 - Is the reopening of schools affecting students or staff more?

# 1. search through data until users date range
# 2. get the total student, staff, and cumulative cases
# 3. calculate the average percentage of the student and staff cases from the total school related cases
# 4. visualize using a bar graph

import sys
import csv
import re

def main(argv):
  
  if len(argv) != 2:
    print("Usage:", "Q5/Q5StudentStaff.py <Date YYYY-MM-DD>")
    sys.exit(-1)
  
  # make sure user inputs a valid date in command line
  try: 
    userDate = (argv[1])
    userDate = (int)(re.sub('[-]', '', userDate))
  except ValueError as err:
    print("Usage:", "Q5/Q5StudentStaff.py <Date YYYY-MM-DD>")
    sys.exit(-1)
 
  schoolCount = 0
  studentCases = 0
  staffCases = 0

  school_file = open("data/schoolCases.csv", encoding="utf-8-sig")
  school_reader = csv.reader(school_file)
  
  for rows in school_reader:
    if schoolCount != 0:
    # first line is labels
      tempDate = rows[0]
      tempDate = (int)(re.sub('[-]', '', tempDate))
      # convert date to integer
      if (tempDate <= userDate):
        # find percentage of student and staff related cases to total school related cases
        studentCases = (float)(rows[2])
        staffCases = (float)(rows[3])
        totalSchoolCases = (float)(rows[1])
    
    schoolCount += 1
  
  # if the user enters a date where there are no cases
  if studentCases == 0 and staffCases == 0:
    print("There are no related student nor staff cases")
    sys.exit(-1)

  # calculate percentages
  studentCases = studentCases / totalSchoolCases * 100
  staffCases = staffCases / totalSchoolCases * 100
  print("School case summary for {}".format(argv[1]))
  print("Percentage of cases,Student and Staff")
  print("{:.2f},{}".format(studentCases,"Students"))
  print("{:.2f},{}".format(staffCases,"Staff"))
  
# 4. visualize
# python Q5/Q5StudentStaff.py <Date YYYY-MM-DD>
# python Q5/Q5StudentStaff.py <Date YYYY-MM-DD> Q5/q5.csv
# python Q5/Q5Plot.py Q5/q5.csv Q5/q5.pdf

main(sys.argv)