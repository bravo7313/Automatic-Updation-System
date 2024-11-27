import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk
import os
import csv
import time as t


#checking if backup.csv exist or not
#-----------------------------------------------
os.chdir(r"C:\Users\athar\Desktop\Projects\Python Projects\Autoupdater")
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








#backup destinatin is loaded
#-------------------------------------------------
def csv_read_backup():
    data=[]
    templist=[]
    os.chdir(r"C:\Users\athar\Desktop\Projects\Python Projects\Autoupdater")
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





    

#Backup Button Event
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def backup():
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

    #-------------------------------------------------


    #backup destinatin is stored
    #-------------------------------------------------
    def csv_write_backup(data,bkf):
        tempcheck=False
        for i in range(len(data)):
            if data[i]== [bkf+"/AutoBackup"]:
                filecheck="Folder Already Exist"
                tempcheck=True
                break
        if tempcheck==False:
            data.append([bkf+"/AutoBackup"])
            filecheck="Process Completed"

        with open("backup_destination.csv","w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerows(data)
        return filecheck
    
    #-----------------------------------------------
    
    #execution
    #-----------------------------------------------
    def exefunc():

        print_label=ctk.CTkLabel(master=app,text="",text_color="white",font=("Arial",10),fg_color="#202020",bg_color="#202020")
        print_label.place(x=200,y=410)

        print_label.destroy()

        
        bkf=backup_dest()
        backup_data=csv_read_backup()
        filecheck=csv_write_backup(backup_data,bkf)

        #printlabel
        #------------------------------
        print_label=ctk.CTkLabel(master=app,text=filecheck,text_color="white",font=("Arial",10),fg_color="#202020",bg_color="#202020")
        print_label.place(x=200,y=410)
        #------------------------------
    #-----------------------------------------------


        
    #MainFrame
    #-----------------------------------------------
    mainfrm=ctk.CTkFrame(master=app,width=490,height=400,corner_radius=10,fg_color="#202020")
    mainfrm.place(x=190,y=40)

    backup_title=ctk.CTkLabel(master=app,text="Backup Files Settings",text_color="white",font=("Arial",18),fg_color="#202020",bg_color="#202020")
    backup_title.place(x=355,y=70)

    filecus=ctk.CTkLabel(master=app,text="Choose File Location",text_color="white",font=("Arial",12),fg_color="#202020",bg_color="#202020")
    filecus.place(x=380,y=200)

    brwloc=ctk.CTkButton(master=app,text="Brower",text_color="white",font=("Atial",12),hover_color="green",bg_color="#202020",command=exefunc,width=100)
    brwloc.place(x=390,y=240)

    #-----------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Source Button Event
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def source():
    #New source file is assigned
    #---------------------------------------------------------
    def src_file(sfd,dir_values):
        src_path=[]
        src_path.append(dir_values)
        src_path.append(sfd)
        return(src_path)
        
    #---------------------------------------------------------



    #SRC Inforamtion writing
    #-----------------------------------
    def csv_write_src(data,src):
        tempcheck=False
        for i in range(len(data)):
            if data[i]==src:
                already_label=ctk.CTkLabel(master=app,text="Already Exist",text_color="#FFFF00",font=("Arial",12),fg_color="#202020",bg_color="#202020")
                already_label.place(x=400,y=400)
                tempcheck=True
                break
        if tempcheck==False:
            data.append(src)
        with open("dir.csv","w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerows(data)
        return tempcheck
    #-----------------------------------

    #Execution
    #-----------------------------------
    
    def exefunc(dir_values):
        progressbar.start()
        progressbar.set(0.25)
        t.sleep(1)


        src_data=csv_read_src()


        progressbar.set(0.5)
        app.update_idletasks()
        t.sleep(1)


        src_path=src_file(sfd,dir_values)


        progressbar.set(0.75)
        app.update_idletasks()
        t.sleep(2)


        tempcheck=csv_write_src(src_data,src_path)
        if tempcheck==False:
            progressbar.set(1)
            app.update_idletasks()
            progressbar.stop()

            already_label=ctk.CTkLabel(master=app,text="Completed",text_color="#FFFF00",font=("Arial",12),fg_color="#202020",bg_color="#202020")
            already_label.place(x=400,y=400)
        else:
            progressbar.set(0)
            app.update_idletasks()
            progressbar.stop()
        


    def exedir():        
        global sfd
        sfd=directory()
        if len(sfd)==0:
            exit()

            
        backup_data=csv_read_backup()
        dirlist=[]
        for i in range(0,len(backup_data)):
            dirlist.append(backup_data[i][0])

    #-----------------------------------

        #Backup Folder Selection
        #---------------------------------------------------
        loc_chose=ctk.CTkLabel(master=app,text="Choose a location to store the backup file",text_color="white",font=("Atial",12),fg_color="#202020",bg_color="#202020")
        loc_chose.place(x=330,y=250)
        
        loc_option=ctk.CTkComboBox(master=app,values=dirlist,command=exefunc)
        loc_option.place(x=370,y=300)
        #---------------------------------------------------

    #MainFrame
    #-----------------------------------------------
    mainfrm=ctk.CTkFrame(master=app,width=490,height=400,corner_radius=10,fg_color="#202020")
    mainfrm.place(x=190,y=40)

    backup_title=ctk.CTkLabel(master=app,text="Source Files Settings",text_color="white",font=("Arial",18),fg_color="#202020",bg_color="#202020")
    backup_title.place(x=355,y=70)

    filelabel=ctk.CTkLabel(master=app,text="Choose File Location",text_color="white",font=("Arial",12),fg_color="#202020",bg_color="#202020")
    filelabel.place(x=380,y=150)

    brwloc=ctk.CTkButton(master=app,text="Brower",text_color="white",font=("Atial",12),hover_color="green",bg_color="#202020",command=exedir,width=100)
    brwloc.place(x=390,y=190)

    progressbar=ctk.CTkProgressBar(master=app, bg_color="#202020", progress_color="#FFFF00", mode="determinate")
    progressbar.place(x=340,y=380)
    progressbar.set(0)
    #-----------------------------------------------
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#database button event
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def database():
    data=csv_read_src()
    Y=40
    mainfrm=ctk.CTkFrame(master=app,width=490,height=400,corner_radius=10,fg_color="#202020")
    mainfrm.place(x=190,y=40)
    for i in range(len(data)):
        Y+=30
        index=ctk.CTkLabel(master=app,text=i+1,text_color="white",font=("Arial",12),fg_color="#202020",bg_color="#202020")
        index.place(x=230,y=Y)
        data_display=ctk.CTkLabel(master=app,text=data[i],text_color="white",font=("Arial",12),fg_color="#202020",bg_color="#202020")
        data_display.place(x=240,y=Y)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#sidebar
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sidebar=ctk.CTkFrame(master=app,width=150,height=550)
sidebar.place(x=0,y=0,anchor=tk.NW)

#Title
sidebar_title=ctk.CTkLabel(master=app,text="Menu",text_color="white",width=100,height=25,font=("Arial",18),bg_color='#202020',fg_color="#202020")
sidebar_title.place(relx=0.035,rely=0.05,anchor=tk.NW)

#Buttons

backup_button=ctk.CTkButton(master=app,text="Backup Files",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white",command=backup)
source_button=ctk.CTkButton(master=app,text="Source Files",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white",command=source)
database_button=ctk.CTkButton(master=app,text="DataBase",width=100,height=25,hover_color="green",bg_color="#202020",font=("Arial",12),text_color="white",command=database)

#Button Placing
backup_button.place(relx=0.035,rely=0.3,anchor=tk.NW)
source_button.place(relx=0.035,rely=0.4,anchor=tk.NW)
database_button.place(relx=0.035,rely=0.5,anchor=tk.NW)


#appearance
appear=ctk.CTkComboBox(master=app,width=125,values=["Dark","Light","System"],command=appearance,bg_color="#202020",text_color="white",border_color="#8F00FF",button_color="#8F00FF",dropdown_fg_color="#202020",dropdown_text_color="white")
appear.place(relx=0.0195,rely=0.9,anchor=tk.NW)
appear.set("System")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#directory diagong box
#-----------------------------------------------
def directory():
    option={"initialdir":r"C:\Users\athar\Desktop","title":"Select a Folder or File","mustexist":True}
    a=fd.askdirectory(**option)
    return a;


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


# SRC information reading
#--------------------------------------------------------
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
#--------------------------------------------------------



#SRC Inforamtion writing
#--------------------------------------------------------
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
#--------------------------------------------------------

app.mainloop()
