from CTkMessagebox import CTkMessagebox
import customtkinter
import mysql.connector as mysql
import DataValidator



#srndata, yeardata = 100, 100
def modified_wind(srndata, yeardata):
    print("modified_wind")
    global srnentry , yearentry, app
    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("600x600")
    app.resizable(True, True)
    app.title('Modified student details')
    global srnentry
    global nameentry
    global courseentry
    global yearentry
    global contactentry
    global yearentry
    global emailentry

    # SRN details
    srn = customtkinter.CTkLabel(app, text='Student Registration Number', font=("Helvetica", 20), text_color='Black',
                                 fg_color='#80FF80')
    srn.place(x=10, y=10)
    info = customtkinter.CTkLabel(app, text='(SRN)', font=("Helvetica", 20), text_color='Black', fg_color='#80FF80')
    info.place(x=10, y=45)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=45)
    srnentry = customtkinter.CTkEntry(app)  # entry = function
    srnentry.place(x=350, y=45)

    # Name Details
    name = customtkinter.CTkLabel(app, text='Student Name', font=("Helvetica", 20), text_color='Black',
                                  fg_color='#80FF80')
    name.place(x=10, y=90)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=90)
    nameentry = customtkinter.CTkEntry(app)
    nameentry.place(x=350, y=90)
    #srnentry . insert (row 1 ,,,,,)
    # Course Details
    course = customtkinter.CTkLabel(app, text='Course Name', font=("Helvetica", 20), text_color='Black',
                                    fg_color='#80FF80')
    course.place(x=10, y=135)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=135)
    courseentry = customtkinter.CTkEntry(app)
    courseentry.place(x=350, y=135)

    # YOA Details
    year = customtkinter.CTkLabel(app, text='Year of Admission', font=("Helvetica", 20), text_color='Black',
                                  fg_color='#80FF80')
    year.place(x=10, y=175)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=175)
    yearentry = customtkinter.CTkEntry(app)
    yearentry.place(x=350, y=175)

    # Contact Details
    ContactLabel = customtkinter.CTkLabel(app, text='Contact', font=("Helvetica", 20), text_color='Black',
                                          fg_color='#80FF80')
    ContactLabel.place(x=10, y=215)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=215)
    contactentry = customtkinter.CTkEntry(app)
    contactentry.place(x=350, y=215)

    # Email Details
    email = customtkinter.CTkLabel(app, text='Email', font=("Helvetica", 20), text_color='Black', fg_color='#80FF80')
    email.place(x=10, y=250)
    colon = customtkinter.CTkLabel(app, font=("Helvetica", 20), text=':', text_color='White')
    colon.place(x=325, y=250)
    emailentry = customtkinter.CTkEntry(app)
    emailentry.place(x=350, y=250)
    b2menu = customtkinter.CTkButton(app, text='Back', font=("Helvetica", 20), text_color='Black', fg_color='#80FF80',
                                     command=closemain)
    b2menu.place(x=200, y=520)

    #submit the data array to modify record
    modified_button = customtkinter.CTkButton(app, text='Submit Modified Details', text_color='Black',
                                              fg_color='#80FF80',width = 150, command=submitDetails)
    modified_button.place(x=200, y=450)
    #fill the page with data
    #print("before Select Data")
    Select(srndata, yeardata)

def createDataSet():
    #create an data array
    global dataSet
    dataSet = []
    dataSet.clear()

    dataSet.append(nameentry.get())
    dataSet.append(courseentry.get())
    dataSet.append(contactentry.get())
    dataSet.append(emailentry.get())
    dataSet.append(srnentry.get())
    dataSet.append(yearentry.get())

    #print("data array ",dataSet)


    validationFlag = DataValidator.validateAllData(dataSet)

    # recreate the data for submission, note the conversion to int

    if(validationFlag) :
        dataSet.clear()
        dataSet.append(nameentry.get())
        dataSet.append(courseentry.get())
        dataSet.append(int(contactentry.get()))
        dataSet.append(emailentry.get())
        dataSet.append(int(srnentry.get()))
        dataSet.append(int(yearentry.get()))

    return validationFlag

def serverModify():
    flag = createDataSet()
    if(flag) :
        global con, cur
        con = mysql.connect(host='localhost', user='root', password='123456', db='clg')
        cur = con.cursor()
        q = "update student_details set SNAME = %s,COURSE = %s,contact = %s, EMAIL = %s WHERE (SRN = %s  AND YEAR_OF_ADMISSION = %s)"
        #v = tuple(data)
        value = (dataSet[0], dataSet[1], dataSet[2], dataSet[3], dataSet[4], dataSet[5])
        #print("value",value)
        cur.execute(q, value)
        #cur.execute(q)
        #print("executed cursor")
        con.commit()
        con.close()
        dataSet.clear()
        if (cur.rowcount == 1) :
            #print("updated records :", cur.rowcount)
            CTkMessagebox(title="Success", message='Data Modified Successfully',icon="check", option_1="Done")
        else :
            CTkMessagebox(title="Error", message='Data Modification Failed', icon="cancel")
    else :
        dataSet.clear()
        CTkMessagebox(title="Error", message='Data Validation Error', icon="cancel")

def submitDetails():
    serverModify()

def closemain():
    app.withdraw()


def Select(srndata, yeardata):
    #print("Inside Select Data")
    if (srndata == ""):
        CTkMessagebox(title="ALERT",message= "Empty Fields not Allowed!",icon="cancel")
    else:
        con = mysql.connect(host='localhost',user='root',password='123456',db='clg')
        cursor = con.cursor()
        query = ("select * from student_details where SRN = %s AND YEAR_OF_ADMISSION = %s")
        value = (srndata, yeardata,)
        #print("printing after query : ", srndata, yeardata)
        cursor.execute(query, value)
        #cursor.execute("select * from student_details where SRN = 122 AND YEAR_OF_ADMISSION = 2022")
        rows = cursor.fetchall()
        print("fetched rows : ", cursor.rowcount)
        for row in rows:
            print("row ", row)
            srnentry.insert(0, row[0])
            srnentry.configure(state='disabled')
            nameentry.insert(0,row[1])
            courseentry.insert(0,row[2])
            yearentry.insert(0, row[3])
            yearentry.configure(state='disabled')
            contactentry.insert(0,row[4])
            emailentry.insert(0,row[5])

        con.close()


def drawModifyStudentMainApp(srndata, yeardata):
    print("drawModifyStudentMainApp")
    modified_wind(srndata, yeardata)
    app.mainloop()

#drawModifyStudent1App(srndata, yeardata)
