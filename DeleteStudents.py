from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
from tkinter import *


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

        closeButton = customtkinter.CTkButton(mainScreen, text='Close',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985', command=closemain)
        closeButton.place(x=100, y=200)

        deleteButton = customtkinter.CTkButton(mainScreen, text='Delete',font = ("Helvetica",20) ,text_color='Black', fg_color='#ff0000', command=delrecord)
        deleteButton.place(x=400, y=200)

def delrecord():
    delrec(srnData, yearData)

def delrec(srnData, yearData) :
    initialise()
    # get yes/no answers
    #print("get choicebox")
    msg = CTkMessagebox(title="Ready to Delete?", message="Do you want to Delete the data?",
                        icon="question", option_1="No", option_2="Yes")
    response = msg.get()
    #print("got choice")
    if response == "Yes":
        #print("get choicebox, submitting for deletion")
        submitForDelete(srnData, yearData)
    else:
        print("Operation cancelled by User")
        #print("printing data[] AFTER user cancelleation", data)

def submitForDelete(srnData, yearData):
    q = "Delete from student_details where SRN = %s and YEAR_OF_ADMISSION = %s"
    value = (srnData, yearData,)
    cur.execute(q, value)
    con.commit()
    print(cur.rowcount, "record(s) deleted")
    if(cur.rowcount == 1) :
        CTkMessagebox(message="Record has been successfully deleted.",icon="check", option_1="Close")
        closemain()
    else :
        CTkMessagebox(message="Record Deletion FAILED. Try again OR contact Administrator",icon="error", option_1="Close")

def closemain():
    mainscreen.withdraw()

def initialise():
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()

def mainScreen(srnData, yearData):
    initialise()
    global mainscreen, studentList
    mainscreen = Toplevel(intermediateScreen)

    #mainScreen = customtkinter.CTk()
    mainscreen.resizable(True, True)
    mainscreen.title("Delete Student")
    mainscreen.geometry("1500x700")

    studentList = getStudentDetails(srnData, yearData)
    #print("student list : ", studentList)
    t = Table(mainscreen)

def IntermediateScreen():
    global intermediateScreen
    intermediateScreen = customtkinter.CTk()  # create CTk window like you do with the Tk window
    intermediateScreen.geometry("700x500")
    intermediateScreen.resizable(True, True)
    intermediateScreen.title('Search by SRN and Year')
    initialise()

    global srnentry, yearentry
    srn = customtkinter.CTkLabel(intermediateScreen, text='Enter SRN to Search',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985')
    srn.place(x = 100, y = 100)
    colon = customtkinter.CTkLabel(intermediateScreen,font = ("Helvetica",20) ,  text=':', text_color='purple')
    colon.place(x=325, y=100)
    srnentry = customtkinter.CTkEntry(intermediateScreen)  # entry = function
    srnentry.place(x=350, y = 100)

    year = customtkinter.CTkLabel(intermediateScreen, text='Enter YEAR to Search',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985')
    year.place(x = 100, y = 200)
    colon = customtkinter.CTkLabel(intermediateScreen,font = ("Helvetica",20) ,  text=':', text_color='purple')
    colon.place(x=325, y=200)
    yearentry = customtkinter.CTkEntry(intermediateScreen)  # entry = function
    yearentry.place(x=350, y = 200)

    #Search button
    serachButton = customtkinter.CTkButton(intermediateScreen,text='Search', font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985', command=searchStudentbysrnAndYear)
    serachButton.place(x=150, y=300)

    #Close button
    closeb = customtkinter.CTkButton(intermediateScreen,text='Close', font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985', command=closeint)
    closeb.place(x=300, y=300)

def closeint():
    intermediateScreen.withdraw()

def searchStudentbysrnAndYear():
    initialise()
    global srnData, yearData
    srnData = srnentry.get()
    yearData = yearentry.get()

    #Validate if both are present
    if (srnData != '' and yearData != '') :
        if (srnData.isdigit() and yearData.isdigit()) :
            dataExists = checkIfDataExists(srnData, yearData)
            if(dataExists) :
                mainScreen(srnData, yearData)
            else :
                CTkMessagebox(title="Error", message='NO Records found, please enter valid SRN and YEAR')
        else :
            CTkMessagebox(title="Error", message='SRN and YEAR of should be only INTEGERS')
    else :
            CTkMessagebox(title="Error", message='SRN and YEAR are both MANDATORY fields')

def checkIfDataExists(srnData, yearData) :
    q = "select count(*) from student_details where SRN = %s and YEAR_OF_ADMISSION = %s"
    value = (srnData, yearData,)
    cur.execute(q, value)
    rows = cur.fetchall()
    #con.close() #dont close, as the con would be used later
    for row in rows:
        if (row[0] == 0) :
            print("NO DATA EXISTS for SRN and YEAR COMBINATION", row[0])
            return False
        else :
            print("Data exists : ", row[0])
            return True

def getStudentDetails(srnData, yearData):
    global studentdetails
    studentdetails = [("SRN", "NAME", "COURSE", "ADMISSION YEAR", "CONTACT", "EMAIL")]
    q = "select * from student_details where SRN = %s and YEAR_OF_ADMISSION = %s"
    value = (srnData, yearData,)
    cur.execute(q, value)
    rows = cur.fetchall()
    for row in rows:
        #print("Rows : ", row)
        studentdetails.append(row)
    con.close()
    return studentdetails

def drawDeleteStudentApp():
    IntermediateScreen()
    intermediateScreen.mainloop()
    print("drawDeleteStudentApp")

drawDeleteStudentApp()
