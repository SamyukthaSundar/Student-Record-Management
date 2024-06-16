from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
from customtkinter import *
from tkinter import *
import re

class Table:
    def __init__(self, mainScreen):
        print("Student Data from DB ", studentdetails)
        total_rows = len(studentdetails)
        total_columns = len(studentdetails[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if(i == 0) :
                    self.e = customtkinter.CTkEntry(mainScreen, width=200, font = ("Helvetica",20), text_color='White', fg_color='#852cc9')
                else :
                    self.e = customtkinter.CTkEntry(mainScreen, width=200, font = ("Helvetica",20), text_color='Black', fg_color='#2CC985')

                self.e.grid(row=i, column=j)
                self.e.insert(END, studentdetails[i][j])

        closeButton = customtkinter.CTkButton(mainScreen, text='Close',font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80', command=closemain)
        closeButton.place(x=400, y=200)

def closemain():
    mainscreen.withdraw()

def initialise():
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()

def mainScreen(data, flag):
    initialise()
    global mainscreen, studentList
    mainscreen = Toplevel(intermediateScreen)

    #mainScreen = customtkinter.CTk()
    mainscreen.resizable(True, True)
    mainscreen.title("Search with SRN Screen")
    mainscreen.geometry("2500x700")

    studentList = getStudentDetails(data, flag)
    #print("student list : ", studentList)
    t = Table(mainscreen)

def IntermediateScreen():
    global intermediateScreen
    intermediateScreen = customtkinter.CTk()  # create CTk window like you do with the Tk window
    intermediateScreen.geometry("700x500")
    intermediateScreen.resizable(True, True)
    intermediateScreen.title('Search by SRN')
    initialise()

    global srnentry, nameentry
    srn = customtkinter.CTkLabel(intermediateScreen, text='Enter SRN to Search',font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80')
    srn.place(x = 100, y = 100)
    colon = customtkinter.CTkLabel(intermediateScreen,font = ("Helvetica",20) ,  text=':', text_color='White')
    colon.place(x=325, y=100)
    srnentry = customtkinter.CTkEntry(intermediateScreen)  # entry = function
    srnentry.place(x=350, y = 100)

    #Search button
    searchSbutton = customtkinter.CTkButton(intermediateScreen,text='Search', font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80', command=searchStudentbysrn)
    searchSbutton.place(x=550, y=100)

    name = customtkinter.CTkLabel(intermediateScreen, text='Enter Name to Search',font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80')
    name.place(x = 100, y = 200)
    colon = customtkinter.CTkLabel(intermediateScreen,font = ("Helvetica",20) ,  text=':', text_color='White')
    colon.place(x=325, y=200)
    nameentry = customtkinter.CTkEntry(intermediateScreen)  # entry = function
    nameentry.place(x=350, y = 200)

    #Search button
    searchSbutton1 = customtkinter.CTkButton(intermediateScreen,text='Search', font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80', command=searchStudentbyname)
    searchSbutton1.place(x=550, y=200)

    #Close button
    closeb = customtkinter.CTkButton(intermediateScreen,text='Close', font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80', command=closeint)
    closeb.place(x=300, y=400)

def closeint():
    intermediateScreen.withdraw()

def searchStudentbysrn():
    srnData = srnentry.get()
    mainScreen(srnData, "srn")
    #intermediateScreen.withdraw()

def searchStudentbyname():
    nameData = nameentry.get()
    mainScreen(nameData, "name")
    intermediateScreen.withdraw()

def getStudentDetails(data, flag):
    global studentdetails
    studentdetails = [("SRN", "NAME", "COURSE", "ADMISSION YEAR", "CONTACT", "EMAIL")]
    if(flag == "srn") :
        q = "select * from student_details where SRN = %s"
        value = (data,)
    elif(flag == "name") :
        q = "select * from student_details where SNAME = %s"
        value = (data,)
    cur.execute(q, value)
    rows = cur.fetchall()
    for row in rows:
        print("Rows : ", row)
        studentdetails.append(row)
    con.close()
    return studentdetails

def drawSearchStudentApp():
    IntermediateScreen()
    intermediateScreen.mainloop()
    print("drawSearchStudentApp")

drawSearchStudentApp()
