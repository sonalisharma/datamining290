#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
from collections import defaultdict 
from collections import Counter 
import math
(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variablesIOJ
# TODO: declare datastructures
tmpcnt = 0  
weightedcnt =0.0
weightedindx= 0.0
tmpcalc=0.0
d = defaultdict(list)
totalsquare = 0.0
totalrec = 0.0
gini = 0
zipcode = defaultdict(list)
countsum = 0
zipcnt=0.0
weightedcnt=0.0
############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        #Creating a dictionary of candidate names along with their zip codes, this is used in Part 1
        d[row[2]].append(row[contbr_zip])

        #Creating a dictionary of zip codes along with their candidate names, this is used in Part 1
        zipcode[row[contbr_zip]].append(row[cand_nm])

for key in d.keys():
    d[key] = Counter(d[key])
    countsum = sum(d[key].values())
    totalrec = totalrec + countsum
    totalsquare=totalsquare+math.pow(countsum,2)

 # current Gini Index using candidate name as the class
gini = 1 - (totalsquare/math.pow(totalrec,2))

for key in zipcode.keys():
    #print key
    a = Counter(zipcode[key])
    totalsum =  sum(a.values())
    #print ("totalsum",totalsum)
    for x in a.values():
        #print ("square: " , math.pow(x,2))
        tmpcnt = tmpcnt + math.pow(x,2)
    #print ("inter ",tmpcnt/math.pow(totalsum,2))
    tmpcalc = 1 - tmpcnt/math.pow(totalsum,2)
    #print ("tt ",tmpcalc)
    #print ('%d * (%d/%d))',tmpcalc,totalsum,totalrec)
    weightedindx = (tmpcalc * (totalsum/totalrec))
    #print ("k ", weightedindx)
    #print "***********************************"
    tmpcnt =0.0
    weightedcnt = weightedcnt + weightedindx
    
split_gini = weightedcnt

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
