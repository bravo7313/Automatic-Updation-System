import csv
import os
import time



# Source and Backup Directory Check
#----------------------------------------------------------------------------------------------
templist=[]
with open("dir.csv","r") as csvfile:
    csvreader=csv.reader(csvfile)
    for i in csvreader:
        if len(i)==0:
            continue
        templist.append(i)

# Source Directory check

for i in range(len(templist)):
    dirchk = os.path.isdir(templist[i][0])
    if dirchk == False:
        target=open("logs.txt","a")
        target.write(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()))
        target.write(" File: \"")
        target.write(templist[i][0])
        target.write("\" Not Found\n")
        target.close()


# Backup Directory Check
#Note: This only check backup directoru which will be used or assigned, this might cause a issue in future

    dirchk = os.path.isdir(templist[i][1])
    if dirchk == False:
        target=open("logs.txt","a")
        target.write(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()))
        target.write(" File: \"")
        target.write(templist[i][0])
        target.write("\" Not Found\n")
        target.close()
#----------------------------------------------------------------------------------------------
