from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
from customtkinter import *
from tkinter import *
import re

def initialise():
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()

def getStudentData():
    global studentdetails
    studentdetails = [("SRN", "NAME", "COURSE", "ADMISSION YEAR", "CONTACT", "EMAIL")]
    cur.execute("select * from student_details")
    rows = cur.fetchall()
    for row in rows:
        studentdetails.append(row)
    con.close();


class Table:

    def __init__(self,root):
        initialise()
        getStudentData()
        print("Student Data from DB ", studentdetails)
        total_rows = len(studentdetails)
        total_columns = len(studentdetails[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if(i == 0) :
                    self.e = customtkinter.CTkEntry(root, width=200, font = ("Helvetica",20), text_color='White', fg_color='#852cc9')
                else :
                    self.e = customtkinter.CTkEntry(root, width=200, font = ("Helvetica",20), text_color='Black', fg_color='#2CC985')

                self.e.grid(row=i, column=j)
                self.e.insert(END, studentdetails[i][j])

        closeButton = customtkinter.CTkButton(root, text='Close',font = ("Helvetica",20) ,text_color='Black', fg_color='#80FF80', command=close)
        closeButton.place(x=450, y=600)


# take the data
lst = [(1,'Raj','Mumbai',19, 9999999999, 'e@e.com'),
       (2,'Aaryan','Pune',18, 9999999999, 'e@e.com'),
       (3,'Vaishnavi','Mumbai',20, 9999999999, 'e@e.com'),
       (4,'Rachna','Mumbai',21, 9999999999, 'e@e.com'),
       (5,'Shubham','Delhi',21, 9999999999, 'e@e.com')]

# find total number of rows and
# columns in list
#total_rows = len(lst)
#total_columns = len(lst[0])

def close():
    root.withdraw()

def drawViewStudentApp():
    # create root window
    #root = Tk()
    global root
    root = customtkinter.CTk()
    root.geometry("1200x700")
    root.resizable(True, True)
    root.title('View Student Details')
    t = Table(root)
    root.mainloop()

drawViewStudentApp()
