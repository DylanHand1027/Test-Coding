import datetime
import time
import statistics as stats
import commands as com
import numpy as np

print('########## TDC-DS Timer Tool ############')


##### prelim config stuff


###############################################

ts1 = time.time() ###start first query run

#### run the query once

ts2 = time.time() #end first query run

qt1 = ts2 - ts1 # first query total time 

###############################################

ts3 = time.time() ###start second query run

#### run the query a second time!

ts4 = time.time() #end second query run

qt2 = ts4 - ts3 # second query total time 

################################################

ts5 = time.time() ###start third query run

#### run the query a third time!

ts6 = time.time() #end third query run

qt3 = ts6 - ts5 # third query total time 

################################################

timelist = [str(qt1), str(qt2),str(qt3)]
median = stats.median(timelist)


f = open("TPCDS_Times.txt","w+")
#print com.getoutput('hdfs dfs -put ../test.csv ' + fileName + '.csv')

print("Query 1 Time: "  + timelist[0] + " seconds")
print("Query 2 Time: "  + timelist[1] + " seconds")
print("Query 3 Time: "  + timelist[2] + " seconds")
print("Median Query Time: " + median  + " seconds")
print("Process terminated.")