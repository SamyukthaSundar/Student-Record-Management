import datetime

from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector
import ModifyStudentsMain
import DataValidator
def initializeModStudent():
    #global regex
    #regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' ##the format ssn@gm.com
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    global con, cur
    con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
    cur=con.cursor()
def newwindow1():
    #def window2(): = newwindow
    initializeModStudent()
    global wind, srnentry, yearentry
    #wind = customtkinter.CTkToplevel()
    wind = customtkinter.CTk()
    wind.geometry("600x400")
    wind.resizable(True, True)
    wind.title("Modify")
    wind.config(bg='#001220')

    srn = customtkinter.CTkLabel(wind, text='SRN', font=("Helvetica", 20), text_color='Black',
                                 fg_color='#66FF66')
    srn.place(x=65, y=50)
    srnentry = customtkinter.CTkEntry(wind, width = 190)  # entry = function
    srnentry = customtkinter.CTkEntry(wind, width = 190)  # entry = function
    srnentry.place(x=205, y=50)
    year = customtkinter.CTkLabel(wind, text='Year of Admission', font=("Helvetica", 20), text_color='Black',
                                  fg_color='#66FF66')
    year.place(x=10, y=115)
    yearentry = customtkinter.CTkEntry(wind,width = 190)
    yearentry.place(x=205, y=115)

    submitbutton = customtkinter.CTkButton(wind, text='Submit',font=("Rosewood Std Regular", 21), fg_color='#66FF66',text_color='Black',command=modified)
    submitbutton.place(x = 120 , y = 300 )

def checkSRNData(srndata):
    print("srndata in checkSRNData : ", srndata)
    dataValidation = False
    if srndata != '':
        print("srndata != ''")
        if srndata.isdigit():
            print("srndata.isdigit():")
            dataValidation = True
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for SRN Data')
    print("dataValidation in checkSRNData : ", dataValidation)
    return dataValidation

def checkYoaData(srnData, yoaData):
    dataValidation = False
    current_year = datetime.datetime.today().year
    if yoaData != '':
        if yoaData.isdigit():
            dataValidation = DataValidator.checkIfSRNExists(srnData, yoaData)
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
    print("dataValidation in checkYoaData : ", dataValidation)
    return dataValidation

def checkYoaDataModify(srnData, yoaData):
    dataValidation = False
    current_year = datetime.datetime.today().year
    if yoaData != '':
        if yoaData.isdigit():
            dataValidation = DataValidator.checkIfSRNExists(srnData, yoaData)
            #print("DataValidation to check uniqueness ", dataValidation)
            #print("current year ",current_year)
            print("yoa, ",yoaData)
            '''if int(yoaData) <= int(current_year):
                dataValidation = True
                if(dataValidation) :
                    dataValidation = True
                else :
                    dataValidation = False
                    CTkMessagebox(title="Error", message='SRN and YEAR of ADMISSION NOT Unique')
            else:
                dataValidation = False
                CTkMessagebox(title="Error", message='Year of Admission cannot be more than Current Year.')'''
        else:
            dataValidation = False
            CTkMessagebox(title="Error", message='Enter valid input for Year of Admission')
    else:
        dataValidation = False
        CTkMessagebox(title="Error", message='Enter valid input for Year Of Admission Data')
    print("dataValidation in checkYoaData : ", dataValidation)
    return dataValidation

def modified():
    global srndata , yeardata
    srndata = srnentry.get()
    yeardata = yearentry.get()

    #checkSRNData(srndata)
    if(checkSRNData(srndata)) :
        checkFlag = checkYoaDataModify(srndata, yeardata)
        if(checkFlag) :
            flag = DataValidator.checkIfSRNExists(srndata, yeardata)
            if(flag) :
                print("passing srndata and yeardata ",srndata, yeardata)
                ModifyStudentsMain.drawModifyStudentMainApp(srndata, yeardata)
            else :
                CTkMessagebox(title="Error", message='DATA VALIDATION FAILED', icon="cancel")
        else :
            CTkMessagebox(title="Error", message='Enter Proper Inputs', icon="cancel")
    else:
        CTkMessagebox(title="Error", message='Enter Proper Inputs2', icon="cancel")


def drawModifyStudentApp():
#    winadd()
    initializeModStudent()
    newwindow1()
    wind.mainloop()
    print("drawModifyStudentApp")

drawModifyStudentApp()
