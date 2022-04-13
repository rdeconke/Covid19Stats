#!/usr/bin/env python

import sys
import csv

# Question 2 - How well are different regions dealing / handling outbreaks in their areas?

# total cases file: row data value [10] = PHU ID 
#                   row data value [11] = case outbreak

# 1. open file, convert to csv
# 2. traverse file for PHU id of interest and count number of cumulative cases, as well as outbreaks
# 3. print result
# 4. visualize using bar plot

def main(argv):
  
  total_cases_file = open("data/conposcovidloc.csv", encoding="utf-8-sig")
  total_cases_reader = csv.reader(total_cases_file)

  if len(argv) != 3:
    print("Usage:", "Q2/Q2RegionalDifferences.py <PHU_ID1> <PHU_ID2>")
    sys.exit(-1)

  PHU1 = (argv[1])
  total_1 = 0
  total_1_outbreak = 0
  PHU2 = (argv[2])
  total_2 = 0
  total_2_outbreak = 0
  PHU1name = ""
  PHU2name = ""

  PHU1found = False
  PHU2found = False
  
  for rows in total_cases_reader:
    if rows[10] == PHU1: # for PHU ID of interest
      total_1 = total_1 + 1 # total cases
      PHU1found = True
      if rows[9] == "Yes": # total outbreak cases
        total_1_outbreak = total_1_outbreak + 1
      if PHU1name == "": # PHU name
        PHU1name = rows[13]

    if rows[10] == PHU2:
      total_2 = total_2 + 1
      PHU2found = True
      if rows[9] == "Yes":
        total_2_outbreak = total_2_outbreak + 1
      if PHU2name == "":
        PHU2name = rows[13]
  
  # if the PHU ID does not exist within the file
  if PHU1found == False and PHU2found == False:
    print("Public Health Unit {} and {} not found, please check data/PHUID file for valid IDs and their correlated regions". format(PHU1, PHU2))
    sys.exit(-1)
  if PHU1found == False:
    print("Public Health Unit {} not found, please check data/PHUID file for valid IDs and their correlated regions". format(PHU1))
    sys.exit(-1)
  if PHU2found == False:
    print("Public Health Unit {} not found, please check data/PHUID file for valid IDs and their correlated regions". format(PHU2))
    sys.exit(-1)

  # if there are no covid cases related to either of the PHU IDs
  if total_1_outbreak == 0 and total_2_outbreak == 0:
    print("No outbreak cases found related to PHU_ID {} or PHU_ID {}".format(PHU1,PHU2))
    sys.exit(-1)
  elif total_1_outbreak == 0: # print results
    print("No outbreak cases found related to PHU_ID {}".format(PHU1))
    sys.exit(-1)
  elif total_2_outbreak == 0:
    print("No outbreak cases found related to PHU_ID {}".format(PHU2))
    sys.exit(-1)
    
  print("Public Health Unit,Type,Number of cases")
  print("{},{},{}".format(PHU1name,"Outbreak",total_1_outbreak))
  print("{},{},{}".format(PHU1name,"Total",total_1))
  print("{},{},{}".format(PHU2name,"Outbreak",total_2_outbreak))
  print("{},{},{}".format(PHU2name,"Total",total_2))

# 4. visualize
# python Q2/Q2RegionalDifferences.py <PHU_ID1> <PHU_ID2>
# python Q2/Q2RegionalDifferences.py <PHU_ID1> <PHU_ID2> > Q2/q2.csv
# python Q2/Q2Plot.py Q2/q2.csv Q2/q2.pdf

main(sys.argv)