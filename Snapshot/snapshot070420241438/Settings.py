import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk
import os
import csv


#checking if backup.csv exist or not
#-----------------------------------------------
os.chdir(r"C:\Users\athar\Desktop\Python\Python Projects\Autoupdater")
templist=os.listdir()
tempcheck=False
for i in range(len(templist)):
    if templist[i]=="backup_destination.csv":
        tempcheck=True
if tempcheck == False:
    target=open("backup_destination.csv","w")
    target.close("backup_destination.csv")
    target=open("logs.txt","a")
    target.write(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()))
    target.write(" File: \"backup_destination.csv\" Not Found\n")
    target.write(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()))
    target.write("Creating a New \"backup_destination.csv\"")
    target.close()
#------------------------------------------------




#application theme
#---------------------------------------------------------
def appearance(value):
    if value=="Dark":
        ctk.set_appearance_mode('Dark')
    elif value=="Light":
        ctk.set_appearance_mode('Light')
    elif value=="System":
        ctk.set_appearance_mode('System')

ctk.set_default_color_theme("dark-blue")
#---------------------------------------------------------

#declaring application
#---------------------------------------------------------
app=ctk.CTk()
app.geometry("720x480")
app.resizable(0,0)
app.title("Auto Updater Setting")
#---------------------------------------------------------



#sidebar
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sidebar=ctk.CTkFrame(master=app,width=150,height=550)
sidebar.place(relx=0,rely=0,anchor=tk.NW)

#Title
sidebar_title=ctk.CTkLabel(master=app,text="Menu",text_color="white",width=100,height=25,font=("Arial",18),bg_color='#202020',fg_color="#202020")
sidebar_title.place(relx=0.035,rely=0.05,anchor=tk.NW)

#Buttons

backup_button=ctk.CTkButton(master=app,text="Backup Files",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white")
source_button=ctk.CTkButton(master=app,text="Source Files",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white")
database_button=ctk.CTkButton(master=app,text="DataBase",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white")

#Button Placing
backup_button.place(relx=0.035,rely=0.3,anchor=tk.NW)
source_button.place(relx=0.035,rely=0.4,anchor=tk.NW)
database_button.place(relx=0.035,rely=0.5,anchor=tk.NW)


#appearance
appear=ctk.CTkComboBox(master=app,width=125,values=["Dark","Light","System"],command=appearance,bg_color="#202020",text_color="white",border_color="#8F00FF",button_color="#8F00FF",dropdown_fg_color="#202020",dropdown_text_color="white")
appear.place(relx=0.0195,rely=0.9,anchor=tk.NW)
appear.set("Dark")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Menu
#----------------------------------------------
ans=int(input("Enter value : "))
#----------------------------------------------


#directory diagong box
#-----------------------------------------------
def directory():
    option={"initialdir":r"C:\Users\athar\Desktop","title":"Select a Folder or File","mustexist":True}
    a=fd.askdirectory(**option)
    return a;
#-----------------------------------------------






# new backup destination is maked
#-----------------------------------------------
def backup_dest():
    print("Select a destination for backup")
    bkf=directory()
    os.chdir(bkf)
    templist=os.listdir()
    tempcheck = False
    for i in range(len(templist)):
        if templist[i]=="AutoBackup":
            tempcheck = True
    if tempcheck == False:
        os.makedirs("AutoBackup")
    return bkf

#-----------------------------------------------



    
#New source file is assigned
#---------------------------------------------------------
def src_file(data):
    print("Select the Source file")
    sfd=directory()
    print("Where should the backup get stored?")
    for i in range(1,len(data)+1):
        tempstring=''
        for j in range(len(data[i-1])):
            tempstring+=data[i-1][j]
        print(i,". ",tempstring)
    temp=int(input("Answer: "))
    tempstring=''
    src_path=[]
    for i in range(len(data[temp-1])):
        tempstring += data[temp-1][i]
    src_path.append(tempstring)
    src_path.append(sfd)
    return(src_path)

#---------------------------------------------------------



#backup destinatin is loaded
#-------------------------------------------------
def csv_read_backup():
    data=[]
    templist=[]
    os.chdir(r"C:\Users\athar\Desktop\Python\Python Projects\Autoupdater")
    with open("backup_destination.csv","r") as csvfile:
        csvreader= csv.reader(csvfile)
        for i in csvreader:
            templist.append(i)
        
    for i in range(len(templist)):
        if len(templist[i])== 0:
            continue
        data.append(templist[i])
    return(data)
#-------------------------------------------------



#backup destinatin is stored
#-------------------------------------------------
def csv_write_backup(data,bkf):
    tempcheck=False
    for i in range(len(data)):
        if data[i]== [bkf+"/AutoBackup"]:
            print("Folder Already Exist")
            tempcheck=True
            break
    if tempcheck==False:
        data.append([bkf+"/AutoBackup"])

    with open("backup_destination.csv","w") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)
    print("Done")
    
#-----------------------------------------------




# SRC information reading
#---------------------------------
def csv_read_src():
    data=[]
    templist=[]
    with open("dir.csv","r") as csvfile:
        csvread=csv.reader(csvfile)
        for i in csvread:
            templist.append(i)
    for i in range(len(templist)):
        if len(templist[i])==0:
            continue
        data.append(templist[i])
    return data
#-----------------------------------



#SRC Inforamtion writing
#-----------------------------------
def csv_write_src(data,src):
    tempcheck=False
    for i in range(len(data)):
        if data[i]==src:
            print("Already exist 2")
            tempcheck=True
            break
    if tempcheck==False:
        data.append(src)
    with open("dir.csv","w") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)
    print("done2")
#-----------------------------------

# executing funcitons
#--------------------------------------------------------
if (ans==1):
    bkf=backup_dest()


backup_data=csv_read_backup()
if ans==2:
    src_path=src_file(backup_data)
    src_data=csv_read_src()

if (ans==1):
    csv_write_backup(backup_data,bkf)
elif(ans==2):
    csv_write_src(src_data,src_path)
elif(ans==3):
    data=csv_read_src()
    for i in range(len(data)):
        print(data[i])

#--------------------------------------------------------





app.mainloop()
