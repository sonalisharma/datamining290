#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv
import math

total = 0
a=[]
max=0
min=0
d={}
t= 0
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])
        ###
        candidatename=str(row[2])
        if d.has_key(candidatename):
            d[candidatename].append(float(row[9]))
        else:
	    tmp=[]
	    tmp.append(float(row[9]))
	    d[candidatename]=tmp
        a.append(float(row[9]))
# TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/

###
# TODO: aggregate any stored numbers here
a.sort()
max=a[-1]
min=a[0]
mean=total/len(a)
median=a[int(math.floor(len(a))/2)]
for i in a:
    t+=math.pow((float(i)-mean),2)
sd=math.sqrt((t/len(a)))
##/

##### Print out the stats
print "Total: %s" % total
print "Minimum: %s " % min
print "Maximum: %s " % max
print "Mean: %s " % mean
print "Median:%s " % median
# square root can be calculated with N**0.5
print "Standard Deviation: %sd " %  sd

##### Comma separated list of unique candidate names
print "Candidates: ", d.keys()

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    newmin=0
    newmax=1
    norm =((value-min)/(max-min))*(newmax-newmin) + newmin
    ###/
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

def statspercandidate(key):
    d[key].sort()
    subtotal=0
    subtmp=0
    subtotal=sum(d[key])
    submin = d[key][0]
    submax = d[key][-1]
    submean = subtotal/len(d[key])
    for i in d[key]:
        subtmp+=math.pow((float(i)-submean),2)
    subsd=math.sqrt((subtmp/len(d[key])))
    submedian =d[key][int(math.floor(len(d[key])/2))]
    print key
    print "Total: %s" % subtotal
    print "Minimum: %s " % submin
    print "Maximum: %s " % submax
    print "Mean: %s " % submean
    print "Median:%s " % submedian
    print "Standard Deviation %s" % subsd	
    print "--------------------------------"
for keys in d.keys():
    statspercandidate(keys)

def zscore(value):
    tmp=(float(value)-mean)/sd
    return tmp

print "Z-score %r" % map(zscore, [2500, 50, 250, 35, 8, 100, 19])


