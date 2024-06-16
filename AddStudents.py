'''https://youtu.be/Miydkti_QVE?si=viJ9EL4PI_XsRONo'''
import datetime

from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
from customtkinter import *
import re

def initializeAddStudent():
    global regex
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' ##the format ssn@gm.com
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()
    #unique=[]

def getYearListForSRN(srnData):
    yearList = []
    yearList.clear()
    q="SELECT YEAR_OF_ADMISSION FROM student_details WHERE SRN = "+srnData
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            yearList.append(j)
    #print("YEar List = ", yearList)

    return yearList

'''
srnList = []
def getSRNList():
    srnList.clear()
    q="SELECT SRN FROM student_details"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srnList.append(j)
    #print("SRN List = ", srnList)
'''

data = []
dataValidation = False
#global submitButton
#print("printing dataValidation begining", dataValidation)

def winadd():  # to open add record
    initializeAddStudent()
    global srnentry
    global nameentry
    global courseentry
    global yearentry
    global contactentry
    global yearentry
    global emailentry
    global app
    #global nex1  # next button

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("1200x600")
    app.resizable(True, True)
    app.title('Student Details')

    #getSRNList()

    #SRN details
    srn = customtkinter.CTkLabel(app, text='Student Registration Number',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985')
    srn.place(x = 10, y = 10)
    info = customtkinter.CTkLabel(app, text='(SRN)',font = ("Helvetica",20), text_color='Black', fg_color='#2CC985')
    info.place(x=10, y=45)
    colon = customtkinter.CTkLabel(app,font = ("Helvetica",20) ,  text=':', text_color='purple')
    colon.place(x=325, y=45)
    srnentry = customtkinter.CTkEntry(app)  # entry = function
    srnentry.place(x=350, y = 45)

    #Name Details
    name = customtkinter.CTkLabel(app,text='Student Name',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985')
    name.place(x=10, y=90)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='purple')
    colon.place(x=325, y=90)
    nameentry = customtkinter.CTkEntry(app)
    nameentry.place(x=350, y=90)

    #Course Details
    course = customtkinter.CTkLabel(app,text='Course Name',font = ("Helvetica",20) ,text_color='Black', fg_color='#2CC985')
    course.place(x=10, y=135)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='purple')
    colon.place(x=325, y=135)
    courseentry = customtkinter.CTkEntry(app)
    courseentry.place(x=350, y=135)

    #YOA Details
    year =customtkinter.CTkLabel(app,text='Year of Admission',font = ("Helvetica",20) ,text_color='Black',fg_color='#2CC985')
    year.place(x=10, y=175)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='purple')
    colon.place(x=325, y=175)
    yearentry = customtkinter.CTkEntry(app)
    yearentry.place(x=350, y=175)

    #Contact Details
    ContactLabel = customtkinter.CTkLabel(app,text='Contact',font = ("Helvetica",20) ,text_color='Black',fg_color='#2CC985')
    ContactLabel.place(x=10, y=215)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='purple')
    colon.place(x=325, y=215)
    contactentry = customtkinter.CTkEntry(app)
    contactentry.place(x=350, y=215)

    #Email Details
    email = customtkinter.CTkLabel(app, text='Email', font=("Helvetica", 20), text_color='Black', fg_color='#2CC985')
    email.place(x=10, y=250)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='purple')
    colon.place(x=325, y=250)
    emailentry = customtkinter.CTkEntry(app)
    emailentry.place(x=350, y=250)

    #Submit button
    submitButton = customtkinter.CTkButton(app ,text='Add Details', text_color='Black', fg_color='#2CC985', command=submitDetails)
    submitButton.place(x=240, y=360)

def serverSubmit():
    q = "insert into student_details(SRN,SNAME,COURSE,YEAR_OF_ADMISSION,contact,EMAIL) values (%s,%s,%s,%s,%s,%s)"
    v = tuple(data)
    cur.execute(q, v)
    con.commit()
    detailsentered = CTkMessagebox(message="Details Have Been successfully Entered.",icon="check", option_1="Done")
    #getSRNList()
    print("Refreshed SRN List post server submission")
    new_record()

def new_record():
    newrec = customtkinter.CTkButton(app, text='Add Another Record', fg_color='#2CC985',command=refreshApp)
    newrec.place(x = 240, y = 360)

def refreshApp():
    #app.update()
    print("adding another record")
    refresh(app)

def refresh(self):
    #self.withdraw()
    #self.__init__()
    app.withdraw()
    winadd()
    app.mainloop()

def submitDetails():
    dataValidation = validateAllData()
    print ("DataValidtion in last step = ", dataValidation)

    if(dataValidation) :
        # get yes/no answers
        print("printing data[] before Confirmation checkbox", data)
        msg = CTkMessagebox(title="Ready to Submit?", message="Do you want to Submit the data?",
                        icon="question", option_1="No", option_2="Yes")
        response = msg.get()
        if response == "Yes":
            #print("printing data[] before submission", data)
            serverSubmit()
        else:
            #print("printing data[] BEFORE user cancelleation", data)
            data.clear()
            validateAllData()
            print("Operation cancelled by User")
            #print("printing data[] AFTER user cancelleation", data)

    else :
        #print("printing data[] -> Data Validation Error", data)
        data.clear()
        CTkMessagebox(title="Error!", message = 'Data Validation Error', icon = "cancel")

def validateAllData():
    data.clear()
    dataValidation = validateSrnData()
    if(dataValidation):
        dataValidation = validateNameData()
    if(dataValidation):
        dataValidation = validateCourseData()
    if(dataValidation):
        dataValidation = validateYOAData()
    if(dataValidation):
        dataValidation = validateContactData()
    if(dataValidation):
        dataValidation = validateEmailData()
    return dataValidation

#we need unique combination of SRN and YEAR
def checkIfSRNExists(srnData, yoaData):
    print("getting yearlist for SRN -> ", srnData)
    yearSet = set(getYearListForSRN(srnData))
    print("YearList = ", yearSet)
    print("YOA data = ", yoaData)
    ydata = int(yoaData)
    if ydata in yearSet :
        print("NON UNIQUE YEAR and SRN COMBINATION")
        dataValidation = False
    else :
        dataValidation = True
    return dataValidation


def validateSrnData():
    dataValidation = False
    srnData = srnentry.get()
    if srnData != '':
        if srnData.isdigit():
            data.append(srnData)
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    return dataValidation

def validateNameData():
    dataValidation = False
    nameData = nameentry.get()
    if nameData != '':
        if re.match("[A-Za-z]", nameData):
            data.append(nameData)
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Student Name')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Student Name')
    return dataValidation

def validateCourseData():
    dataValidation = False
    courseData = courseentry.get()
    if courseData != '':
        if re.match("[A-Za-z]", courseData):
            data.append(courseData)
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Course Name')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Course Name')
    return dataValidation

def validateYOAData():
    dataValidation = False
    yoaData = yearentry.get()
    srnData = srnentry.get()
    #print("SRN data ", srnData)
    current_year = datetime.datetime.today().year
    if yoaData != '':
        if yoaData.isdigit():
            dataValidation = checkIfSRNExists(srnData, yoaData)
            #print("DataValidation to check uniqueness ", dataValidation)
            print("current year ",current_year)
            print("yoa, ",yoaData)
            if int(yoaData) <= int(current_year):
                dataValidation = True

                if(dataValidation) :
                    data.append(yoaData)
                    dataValidation = True
                else :
                    dataValidation = False
                    CTkMessagebox(title="Error", message='SRN and YEAR of ADMISSION NOT Unique')
            else:
                dataValidation = False
                CTkMessagebox(title="Error", message='Year of Admission cannot be more than Current Year.')
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Year of Admission')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Year Of Admission Data')
    return dataValidation

def validateContactData():
    dataValidation = False
    contactData = contactentry.get()
    if contactData != '':
        if contactData.isdigit():
            if len(contactData) > 10 or len(contactData) < 10:
                dataValidation = False
                CTkMessagebox(title="Error", message='Mobile Number should be 10 digits')
            else :
                data.append(contactData)
                dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Contact Details')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Contact Details')
    return dataValidation

def validateEmailData():
    dataValidation = False
    emailData = emailentry.get()
    if emailData != '':
        if (re.fullmatch(regex, emailData)):  # to check if email is in the form of aaaa@lllll.com
            data.append(emailData)
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Email Details')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Email Details')
    return dataValidation

def drawAddStudentApp():
    winadd()
    app.mainloop()
#drawAddStudentApp()

drawAddStudentApp()
