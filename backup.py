import csv
import os
import time
import shutil


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


#Backup
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
data=[]
with open("dir.csv","r") as csvfile:
    csvreader=csv.reader(csvfile)
    for i in csvreader:
        if len(i)==0:
            continue
        data.append(i)
for i in range(len(data)):
    print(data[i][0])
    print(data[i][1])
    tempstring=""
    tempstring1=""
    for j in range(len(data[i][0])):
        if data[i][0][j]=='/':
            tempstring+='\\'
            continue
        tempstring+=data[i][0][j]
    data[i][0]=tempstring
    for j in range(len(data[i][1])):
        if data[i][1][j]=='/':
            tempstring1+='\\'
            continue
        tempstring1+=data[i][1][j]
    data[i][1]=tempstring1

    target=open('backup.bat','w')
    target.write('copy "{a}" "{b}"\nexit'.format(a=data[i][1],b=data[i][0]))
    target.close()
    print("done wrting")
    os.system('start backup.bat')
    print("started")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
