import datetime

from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
from customtkinter import *
import re

global dataValidation
dataValidation = False

def initialise():
    global regex
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' ##the format ssn@gm.com
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()
    #unique=[]

#to understand the index
'''
dataSet.append(nameentry.get()) = 0
dataSet.append(courseentry.get()) = 1
dataSet.append(int(contactentry.get())) = 2
dataSet.append(emailentry.get()) = 3
dataSet.append(int(srnentry.get())) = 4
dataSet.append(int(yearentry.get())) = 5
'''

def validateAllData(dataSet):
    initialise()
    dataValidation = validateSrnData(dataSet)
    if(dataValidation):
        dataValidation = validateNameData(dataSet)
    if(dataValidation):
        dataValidation = validateCourseData(dataSet)
    if(dataValidation):
        dataValidation = validateYOAData(dataSet)
    if(dataValidation):
        dataValidation = validateContactData(dataSet)
    if(dataValidation):
        dataValidation = validateEmailData(dataSet)
    return dataValidation

def getYearListForSRN(srnData):
    initialise()
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

def checkIfSRNExists(srnData, yoaData):
    print("getting yearlist for SRN -> ", srnData)
    yearSet = set(getYearListForSRN(srnData))
    print("YearList = ", yearSet)
    print("YOA data = ", yoaData)
    ydata = int(yoaData)
    if ydata in yearSet :
        print("UNIQUE YEAR and SRN COMBINATION")
        dataValidation = True
    else :
        print("NON UNIQUE YEAR and SRN COMBINATION")
        dataValidation = False
    return dataValidation


def validateSrnData(dataSet):
    dataValidation = False
    srnData = dataSet[4]
    if srnData != '':
        if srnData.isdigit():
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    return dataValidation

def validateNameData(dataSet):
    dataValidation = False
    nameData = dataSet[0]
    if nameData != '':
        if re.match("[A-Za-z]", nameData):
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Student Name')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Student Name')
    return dataValidation

def validateCourseData(dataSet):
    dataValidation = False
    courseData = dataSet[1]
    if courseData != '':
        if re.match("[A-Za-z]", courseData):
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Course Name')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Course Name')
    return dataValidation

def validateYOAData(dataSet):
    dataValidation = False
    yoaData = dataSet[5]
    srnData = dataSet[4]
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

def validateContactData(dataSet):
    dataValidation = False
    contactData = dataSet[2]
    if contactData != '':
        if contactData.isdigit():
            if len(contactData) > 10 or len(contactData) < 10:
                dataValidation = False
                CTkMessagebox(title="Error", message='Mobile Number should be 10 digits')
            else :
                dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Contact Details')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Contact Details')
    return dataValidation

def validateEmailData(dataSet):
    dataValidation = False
    emailData = dataSet[3]
    if emailData != '':
        if (re.fullmatch(regex, emailData)):  # to check if email is in the form of aaaa@lllll.com
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Email Details')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Email Details')
    return dataValidation
