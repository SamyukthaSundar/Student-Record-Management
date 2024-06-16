from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import ImageTk,Image
import customtkinter
from connection import cur
import statistics
import matplotlib.pyplot as plt

#Sanika Imports
import os



def login():                            #getting username and password from user to login
    user=username.get()
    pswrd=password.get()
    database(user,pswrd)

#python-sql connectivity
def database(u,p):
    if p=='a' and u!='':
        global con
        global cur
        import connection
        connection
        from connection import cur
        messagebox.showinfo("Login successful","Logged in")
        cur.execute("CREATE TABLE IF NOT EXISTS Student_Details(SRN INT NOT NULL PRIMARY KEY,SNAME VARCHAR(30),COURSE VARCHAR(30),YEAR_OF_ADMISSION INT(4) NOT NULL,CONTACT INT(10) NOT NULL,EMAIL VARCHAR(30) NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS Mid_Sem(SRN INT NOT NULL REFERENCES Student_Details(SRN),YEAR INT(4) NOT NULL,SUB1 FLOAT(4,1),SUB2 FLOAT(4,1),SUB3 FLOAT(4,1),SUB4 FLOAT(4,1),SUB5 FLOAT(4,1),TOTAL INT,PERCENTAGE FLOAT(4,1),PRIMARY KEY(SRN,YEAR))")
        cur.execute("CREATE TABLE IF NOT EXISTS End_Sem(SRN INT NOT NULL REFERENCES Student_Details(SRN),YEAR INT(4) NOT NULL,SUB1 FLOAT(4,1),SUB2 FLOAT(4,1),SUB3 FLOAT(4,1),SUB4 FLOAT(4,1),SUB5 FLOAT(4,1),TOTAL INT,PERCENTAGE FLOAT(4,1),PRIMARY KEY(SRN,YEAR))")
        quitwindow()
        window2()

    elif p=='':
        messagebox.showerror("error","Password required")
    elif u=='':
        messagebox.showerror("error","Username required")
    else:
        messagebox.showerror("error","Incorrect password")

def quitwindow():
    window.withdraw()


def window2():
    global win2
    win2=customtkinter.CTkToplevel()
    win2.geometry("400x400+0+0")
    win2.resizable(False,False)
    win2.title("Menu")
    win2.config(bg='#001220')
    
    title=customtkinter.CTkLabel(win2,text='Student Records',text_color='#fff',bg_color='#001220',font=font1)
    title.place(x=70,y=5)

    button1=customtkinter.CTkButton(win2,text='Student Details',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=choice1)
    button1.place(x=120,y=70)
    
    button2=customtkinter.CTkButton(win2,text='Examinations',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=choice2)
    button2.place(x=120,y=170)

    button3=customtkinter.CTkButton(win2,text='LogOut',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=logout)
    button3.place(x=120,y=270)
def logout():
    win2.withdraw()
    window.deiconify()

def choice1():
    win2.withdraw()
    global student
    student=customtkinter.CTkToplevel()
    student.config(bg='#001220')
    student.geometry("700x630+0+0")
    student.title('Student Details')
    student.resizable(False,False)
    stu_menu()
def stu_menu():
        button1=customtkinter.CTkButton(student,text='Add Student',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=add)  #add()
        button1.place(x=100,y=50)
        button2=customtkinter.CTkButton(student,text='Modify Student',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=modify)  #modify()
        button2.place(x=100,y=150)
        button3=customtkinter.CTkButton(student,text='Delete Student',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=delete)  #delete()
        button3.place(x=100,y=250)
        button4=customtkinter.CTkButton(student,text='Search Student',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=search)  #search()
        button4.place(x=100,y=350)
        button5=customtkinter.CTkButton(student,text='View All',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=view)  #view()
        button5.place(x=100,y=450)
        back__home = customtkinter.CTkButton(student, text='Back to Home Page', text_color='#fff', fg_color='#00965d',
                                           hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,
                                           width=120, font=font1, command=b2stu_menu)
        back__home.place(x=400, y=550)
def b2stu_menu():
    student.withdraw()
    win2.deiconify()

#Removed by Sanika

def add():
    from AddStudents import drawAddStudentApp
def modify():
    from ModifyStudentsInt import drawModifyStudentApp

def delete():
    from DeleteStudents import drawDeleteStudentApp

def search():
    from SearchStudents import drawSearchStudentApp

def view():
    from ViewStudents import drawViewStudentApp

#--------------------------------------------------EXAMINATIONS----------------------------------------------
def choice2():
    global exam
    win2.withdraw()
    exam=customtkinter.CTkToplevel()
    exam.geometry("400x400+0+0")
    exam.title('Examinations')
    exam.resizable(False,False)
    exam.config(bg='#001220')
    backhome=customtkinter.CTkButton(exam,text='Back to Home Page',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=home)
    backhome.place(x=100,y=230)
    exam_menu()
    #put a back to homepage button here
def home():
    exam.withdraw()
    win2.deiconify()
def exam_menu():
    button1=customtkinter.CTkButton(exam,text='Mid Sem',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=midsem)
    button1.place(x=100,y=70)
    button2=customtkinter.CTkButton(exam,text='End Sem',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=endsem)
    button2.place(x=100,y=140)

#-------------------------------------------------MID SEM---------------------------------------------------------
def midsem():
    #exam.withdraw()
    global midsemw
    exam.withdraw()
    midsemw=customtkinter.CTkToplevel()
    midsemw.geometry("700x630+0+0")
    midsemw.title('Examinations')
    midsemw.config(bg='#001220')
    midsemw.resizable(False,False)
    button1=customtkinter.CTkButton(midsemw,text='Add Scores',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=midadd)
    button1.place(x=100,y=150)
    button2=customtkinter.CTkButton(midsemw,text='View Scores',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=midview)
    button2.place(x=100,y=250)
    button3=customtkinter.CTkButton(midsemw,text='Delete Scores',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=middel)
    button3.place(x=100,y=350)
    button4=customtkinter.CTkButton(midsemw,text='Modify Scores',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=midmodify)
    button4.place(x=100,y=450)
    button5=customtkinter.CTkButton(midsemw,text='Average',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=midaverage)
    button5.place(x=100,y=550)
    backhome=customtkinter.CTkButton(midsemw,text='Back to Home Page',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=homemid)
    backhome.place(x=450,y=550)
def homemid():
    midsemw.withdraw()
    win2.deiconify()


#======================================================ADD SCORES=====================================
def midadd():
    global srnentry
    global mid
    global ok1

    #                   SELECT SRNS FROM STUDENT_DETAILS TO SEE IF STUDENT EXISTS.SO IN VALIDATIONS ALSO YOU INCLUDE THIS
    unique=[]
    q="SELECT SRN,YEAR FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        unique.append(i)
    srns=[]
    q="SELECT SRN FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srns.append(j)

    existing=[]
    q="SELECT SRN FROM STUDENT_DETAILS"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            existing.append(j)

    data=[]
    def getsrn():
        global mid
        global srnentry
        global yearentry,entry1
        global ok1,ok2
        entry1=srnentry.get()
        try:
            if entry1!='':
                if entry1.isdigit():
                    if int(entry1) in existing:
                        data.append(entry1)
                        srnentry.configure(state='disabled')
                        ok1.configure(state=customtkinter.DISABLED)
                        ok1.destroy()
                        #ok1['state']=DISABLED
                        year=customtkinter.CTkLabel(mid,text='Year of Study',font=font2,text_color='#fff',bg_color='#001220')
                        year.place(x=100,y=50)
                        colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                        colon.place(x=220,y=50)
                        yearentry=customtkinter.CTkEntry(mid,width=120)
                        yearentry.place(x=250,y=50)
                        ok2=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getyear)
                        ok2.place(x=400,y=50)
                    else:
                        messagebox.showerror('error','SRN Does Not Exists')
                elif entry1.isalpha():
                    messagebox.showerror('Error','Enter Integer Value of length x')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Empty fields not allowed')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def getyear():
        global yearentry,sub1entry,entry2
        global mid
        global ok2,ok3
        entry2=yearentry.get()
        try:
            if entry2!='':
                if entry2.isdigit() and len(entry2)==4:
                    if (int(entry1),int(entry2)) not in unique:
                        data.append(entry2)
                        yearentry.configure(state='disabled')
                        ok2.configure(state=customtkinter.DISABLED)
                        ok2.destroy()
                        #ok2['state']=DISABLED
                        sub1=customtkinter.CTkLabel(mid,text='Subject 1',font=font2,text_color='#fff',bg_color='#001220')
                        sub1.place(x=100,y=90)
                        colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                        colon.place(x=220,y=90)
                        sub1entry=customtkinter.CTkEntry(mid,width=120)
                        sub1entry.place(x=250,y=90)
                        ok3=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=getsub1)
                        ok3.place(x=400,y=90)
                    else:
                        messagebox.showerror('Error','Record Exists')
                        mid.withdraw()
                        midadd()
                        #winadd()
                elif entry2.isalpha():
                    messagebox.showerror('Error','Enter Integer Value')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Empty fields not allowed')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def getsub1():
        global sub1entry,sub2entry
        global mid,ok3,ok4
        entry3=sub1entry.get()        #REMOVE TRY AND EXCEPT FROM HERE
    
        if entry3!='':
            if entry3.isdigit() and int(entry3)<=100:
                data.append(entry3)
                sub1entry.configure(state='disabled')
                ok3.configure(state=customtkinter.DISABLED)
                ok3.destroy()
                #ok3['state']=DISABLED
                sub2=customtkinter.CTkLabel(mid,text='Subject 2',font=font2,text_color='#fff',bg_color='#001220')
                sub2.place(x=100,y=130)
                colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=130)
                sub2entry=customtkinter.CTkEntry(mid,width=120)
                sub2entry.place(x=250,y=130)
                ok4=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub2)
                ok4.place(x=400,y=130)
            elif entry3.isalpha():
                messagebox.showerror('Error','Enter Integer Value within 100')
            else:
                messagebox.showerror('Error','Enter Integer Value within 100')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub2():
        global mid,sub2entry,sub3entry,ok4,ok5
        entry4=sub2entry.get()
        if entry4!='':
            if entry4.isdigit() and int(entry4)<=100:
                data.append(entry4)
                sub2entry.configure(state='disabled')
                ok4.configure(state=customtkinter.DISABLED)
                ok4.destroy()
                #ok4['state']=DISABLED
                sub3=customtkinter.CTkLabel(mid,text='Subject 3',font=font2,text_color='#fff',bg_color='#001220')
                sub3.place(x=100,y=170)
                colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=170)
                sub3entry=customtkinter.CTkEntry(mid,width=120)
                sub3entry.place(x=250,y=170)
                ok5=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub3)
                ok5.place(x=400,y=170)        
            elif entry4.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')


    def getsub3():
        global mid,sub3entry,sub4entry,ok5,ok6
        entry5=sub3entry.get()
        if entry5!='':
            if entry5.isdigit() and int(entry5)<=100:
                data.append(entry5)
                sub3entry.configure(state='disabled')
                ok5.configure(state=customtkinter.DISABLED)
                ok5.destroy()
                #ok5['state']=DISABLED
                sub4=customtkinter.CTkLabel(mid,text='Subject 4',font=font2,text_color='#fff',bg_color='#001220')
                sub4.place(x=100,y=210)
                colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=210)
                sub4entry=customtkinter.CTkEntry(mid,width=120)
                sub4entry.place(x=250,y=210)
                ok6=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub4)
                ok6.place(x=400,y=210)
            elif entry5.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub4():
        global mid,sub4entry,sub5entry,ok6,ok7
        entry6=sub4entry.get()
        if entry6!='':
            if entry6.isdigit() and int(entry6)<=100:
                data.append(entry6)
                sub4entry.configure(state='disabled')
                ok6.configure(state=customtkinter.DISABLED)
                ok6.destroy()
                #ok6['state']=DISABLED
                sub5=customtkinter.CTkLabel(mid,text='Subject 5',font=font2,text_color='#fff',bg_color='#001220')
                sub5.place(x=100,y=250)
                colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=250)
                sub5entry=customtkinter.CTkEntry(mid,width=120)
                sub5entry.place(x=250,y=250)
                ok7=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub5)
                ok7.place(x=400,y=250)
            elif entry6.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub5():
        global mid,sub5entry,ok7
        entry7=sub5entry.get()
        if entry7!='':
            if entry7.isdigit() and int(entry7)<=100:
                data.append(entry7)
                sub5entry.configure(state='disabled')
                ok7.configure(state=customtkinter.DISABLED)
                ok7.destroy()
                #ok7['state']=DISABLED
                button=customtkinter.CTkButton(mid,text='Enter Details',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=details)
                button.place(x=270,y=300)
            elif entry7.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def details():
        tlist=data[2:7]
        marks=[]
        for i in tlist:
            j=int(i)
            marks.append(j)
        #print(sum(marks))
        total=sum(marks)
        perc=total/5
        data.append(total)
        data.append(perc)
        print(data)
        q="INSERT INTO mid_sem VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        v=tuple(data)
        cur.execute(q,v)
        con.commit()
        messagebox.showinfo("Details","Details entered")
        continue1()

    def midremove():
        mid.withdraw()
        midadd()
        midsemw.deiconify()  #I CJUST CANGED TISSSSSSSSSSSSSSSSSSS

    def continue1():
        again=customtkinter.CTkButton(mid,text='Add another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=midremove)
        again.place(x=250,y=350)

    def resize1():
        mid.withdraw()
        midsemw.deiconify()
        
    midsemw.withdraw()
    mid=customtkinter.CTkToplevel()
    mid.geometry("500x450+0+0")
    mid.resizable(False,False)
    mid.config(bg='#121111')
    srn=customtkinter.CTkLabel(mid,text='SRN',font=font2,text_color='#fff',bg_color='#001220')
    srn.place(x=100,y=10)
    #info=customtkinter.CTkLabel(mid,text='(Student Registration Number)',font=font1,text_color='#fff',bg_color='#001220')
    #info.place(x=20,y=30)
    colon=customtkinter.CTkLabel(mid,text=':',font=font3,text_color='#fff',bg_color='#001220')
    colon.place(x=220,y=10)
    srnentry=customtkinter.CTkEntry(mid,width=120)
    srnentry.place(x=250,y=10)
    ok1=customtkinter.CTkButton(mid,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsrn)
    ok1.place(x=400,y=10)
    back=customtkinter.CTkButton(mid,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resize1)
    back.place(x=190,y=400)



#===============================MODIFY SCORES===========================================
#DISABLING BUTTONS AND ENTRY-TO DO
def midmodify():
    def modify():
        global mw,mb,comboboxm
        mw=customtkinter.CTkToplevel()
        mw.title('Modify')
        mw.geometry('500x500+0+0')
        mw.resizable(False,False)
        mw.configure(bg='#001220')
        mb=customtkinter.CTkLabel(mw,text='Modify Record',font=font2,text_color='#fff',bg_color='#001220')
        mb.place(x=100,y=10)
        comboboxm=ttk.Combobox(mw)
        comboboxm.config(values=['Subject1','Subject2','Subject3','Subject4','Subject5'])
        comboboxm.set("Select An Option")
        comboboxm.bind("<<ComboboxSelected>>",on_selectm)
        comboboxm.place(x=320,y=18)
        b2menu=customtkinter.CTkButton(mw,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=b2menuf)
        b2menu.place(x=380,y=400)
    def b2menuf():
        mw.withdraw()
        midsemw.deiconify()
        

    def on_selectm(event):
        global selected
        selected=event.widget.get()
        print(selected)
        mod1()

    modsrn=[]
    q='select srn from Mid_sem'
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            modsrn.append(j)
    modsrnstud=[]
    q='select srn from student_details'
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            modsrnstud.append(j)

    def mod1():
        global m1entry,modb
        comboboxm.destroy()
        mb.destroy()
        mb1=customtkinter.CTkLabel(mw,text='SRN',font=font2,text_color='#fff',bg_color='#001220')
        mb1.place(x=100,y=10)
        m1entry=customtkinter.CTkEntry(mw,width=120)
        m1entry.place(x=230,y=14)
        modb=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod)
        modb.place(x=380,y=12)
    #getting srn to modify
    def sub1mod():
        global modb2,m1entry2,sub1entry
        sub1entry=m1entry.get()
        if sub1entry!='' and int(sub1entry) in modsrn: #and int(sub1entry) in modsrnstud
            if sub1entry.isdigit():
                modb.destroy()
                mb2=customtkinter.CTkLabel(mw,text='Academic Year',font=font2,text_color='#fff',bg_color='#001220')
                mb2.place(x=100,y=70)
                m1entry2=customtkinter.CTkEntry(mw,width=120)
                m1entry2.place(x=230,y=64)
                modb2=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod2)
                modb2.place(x=380,y=62)
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Enter Integer Value')

    uniquemod=[]
    q="SELECT SRN,YEAR FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        uniquemod.append(i)

    def sub1mod2():
        global modb2,m1entry3,modyearentry
        modyearentry=m1entry2.get()
        if modyearentry!='':
            if modyearentry.isdigit() and len(modyearentry)==4:
                if (int(sub1entry),int(modyearentry)) in uniquemod:
                    modb2.destroy()
                    mb3=customtkinter.CTkLabel(mw,text='Enter New Score',font=font2,text_color='#fff',bg_color='#001220')
                    mb3.place(x=70,y=130)
                    m1entry3=customtkinter.CTkEntry(mw,width=120)
                    m1entry3.place(x=230,y=114)
                    modb2=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod3)
                    modb2.place(x=380,y=112)
                else:
                    messagebox.showerror('Error','Record does not exist')
                    modify()
            elif modyearentry.isalpha():
                messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','enter valid year of length 4')
        else:
            messagebox.showerror('error','no empty fields allowed')

    def sub1mod3():
        newsub1=m1entry3.get()
        if newsub1!='':
            if newsub1.isdigit() and int(newsub1)<=100:
                if selected=='Subject1':
                    q='UPDATE MID_SEM SET SUB1=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject2':
                    q='UPDATE MID_SEM SET SUB2=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject3':
                    q='UPDATE MID_SEM SET SUB3=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject4':
                    q='UPDATE MID_SEM SET SUB4=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject5':
                    q='UPDATE MID_SEM SET SUB5=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                cur.execute(q,v)
                con.commit()
                messagebox.showinfo('Done','Record Modified')
                newmodify()
            elif newsub1.isalpha():
                messagebox.showerror('error','integer value only')
        else:
            messagebox.showerrror('error','no empty fields')

    def newmodify():
        modifynew=customtkinter.CTkButton(mw,text='Modify Another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=modifyagain)
        modifynew.place(x=100,y=400)

    def modifyagain():
        mw.withdraw()
        modify()
    def exitmodify():
        
        mw.withdraw()
        midsemw.deiconify()
    #MADE CHANGES HERE FOR MIDSEM
    #deiconfiy the endsemw window

    modify()


#==============================VIEW/SEARCH SCORES====================================
def midview():
    global view
    def winview():
        global view,okbv,searchl,oksearch,backall
        midsemw.withdraw()        
        view=customtkinter.CTkToplevel()
        view.geometry("700x400+0+0")
        view.resizable(False,False)
        view.config(bg='#121111')
        allview=Label(view,text='View All',fg='black',bg='cyan3',font='Times 14')
        allview.place(x=100,y=10)
        searchl=Label(view,text='Search By',fg='black',bg='cyan3',font='Times 14')
        searchl.place(x=100,y=50)
        oksearch=Button(view,text='Search',bg='cornsilk',fg='black',command=searchscore)
        oksearch.place(x=200,y=50)
        okbv=Button(view,text='View',bg='cornsilk',fg='black',command=viewall)
        okbv.place(x=200,y=10)
        backall=customtkinter.CTkButton(view,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resizeviewwindow)
        backall.place(x=400,y=350)

    def resizeviewwindow():
        view.withdraw()
        midsemw.deiconify()
    def viewall():
        global view,okbv
        searchl.destroy()
        oksearch.destroy()
        q="SELECT * FROM MID_SEM"
        cur.execute(q)
        res=cur.fetchall()
        okbv['state']=DISABLED

        s=ttk.Style(view)
        s.theme_use('default')
        tree=ttk.Treeview(view)
        tree['show']='headings'
        tree['columns']=('1','2','3','4','5','6','7','8','9')
        tree.column('1',width=100,minwidth=0,anchor=CENTER)
        tree.column('2',width=100,minwidth=50,anchor=CENTER)
        tree.column('3',width=100,minwidth=50,anchor=CENTER)
        tree.column('4',width=100,minwidth=50,anchor=CENTER)
        tree.column('5',width=100,minwidth=50,anchor=CENTER)
        tree.column('6',width=100,minwidth=50,anchor=CENTER)
        tree.column('7',width=100,minwidth=50,anchor=CENTER)
        tree.column('8',width=100,minwidth=50,anchor=CENTER)
        tree.column('9',width=100,minwidth=50,anchor=CENTER)

        tree.heading('1',text='SRN',anchor=CENTER)
        tree.heading('2',text='Academic Year',anchor=CENTER)
        tree.heading('3',text='Subject1',anchor=CENTER)
        tree.heading('4',text='Subject2',anchor=CENTER)
        tree.heading('5',text='Subject3',anchor=CENTER)
        tree.heading('6',text='Subject4',anchor=CENTER)
        tree.heading('7',text='Subject5',anchor=CENTER)
        tree.heading('8',text='Total',anchor=CENTER)
        tree.heading('9',text='Percentage',anchor=CENTER)

        sb = ttk.Scrollbar(view, orient="vertical", command=tree.yview)
        sb.place(x=922,y=70, height=225)
        tree.configure(yscrollcommand=sb.set)
        for rec in res:
            tree.insert('','end',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
        tree.place(x=20,y=70)
        backall.destroy()
        back=customtkinter.CTkButton(view,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=midviewrem)
        back.place(x=400,y=350)
    def midviewrem():
        view.withdraw()

    def searchscore():
        global combobox1,searchw,sview
        view.withdraw()
        searchw=customtkinter.CTkToplevel()
        searchw.geometry("700x400+0+0")
        searchw.resizable(False,False)
        searchw.config(bg='#121111')
        sview=Label(searchw,text='Search By',fg='black',bg='cyan3',font='Times 14')
        sview.place(x=70,y=10)
        combobox1=ttk.Combobox(searchw)
        combobox1.config(values=['SRN','Academic Year','Year of Admission'])
        combobox1.set("Select An Option")
        combobox1.bind("<<ComboboxSelected>>",on_select)
        combobox1.place(x=170,y=15)
    def on_select(event):
        selected_item=event.widget.get()
        print(selected_item)
        if selected_item=="SRN":
            srnsearch()
        elif selected_item=='Academic Year':
            yearsearch()
        elif selected_item=='Year of Admission':
            batchsearch()
    def srnsearch():
        global ent,entb,srnmids   #WHATS THIS 
        combobox1.destroy()
        sview.destroy()
        srnmids=Label(searchw,text='SRN',fg='black',bg='cyan3',font='Times 14')
        srnmids.place(x=70,y=10)
        ent=Entry(searchw,width=20)
        ent.place(x=150,y=14)
        entb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbysrn)
        entb.place(x=300,y=12)
        
        q="SELECT * FROM MID_SEM WHERE SRN==%s"

    numbers=[]
    q="SELECT SRN FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            numbers.append(j)

    def searchbysrn():
        number=ent.get()
        try:
            if number!='' and int(number) in numbers:
                if number.isdigit():
                    ts=int(number)
                    entb.destroy()   #Ent bt midttttttttttttttttttttttttttttt
                    ent.destroy()
                    srnmids.destroy()
                    q="SELECT * FROM MID_SEM WHERE SRN=%s"
                    v=(ts,)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9')
                    tree.column('1',width=100,minwidth=0,anchor=CENTER)
                    tree.column('2',width=100,minwidth=50,anchor=CENTER)
                    tree.column('3',width=100,minwidth=50,anchor=CENTER)
                    tree.column('4',width=100,minwidth=50,anchor=CENTER)
                    tree.column('5',width=100,minwidth=50,anchor=CENTER)
                    tree.column('6',width=100,minwidth=50,anchor=CENTER)
                    tree.column('7',width=100,minwidth=50,anchor=CENTER)
                    tree.column('8',width=100,minwidth=50,anchor=CENTER)
                    tree.column('9',width=100,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=922,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','mid',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=midviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showinfo('Delete','Enter Valid SRN')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def midviewrem2():
        searchw.withdraw()
        
        
    def yearsearch():
        global yearmids,yearsearche,viewyearb
        combobox1.destroy()
        sview.destroy()
        yearmids=Label(searchw,text='Academic Year',fg='black',bg='cyan3',font='Times 14')
        yearmids.place(x=70,y=10)
        yearsearche=Entry(searchw,width=20)
        yearsearche.place(x=150,y=14)
        viewyearb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbyyear)
        viewyearb.place(x=300,y=12)
    def searchbyyear():
        yeare=yearsearche.get()
        try:
            if yeare!='':
                if yeare.isdigit():
                    yearmids.destroy()
                    yearsearche.destroy()
                    viewyearb.destroy()
                    q="SELECT * FROM MIDSEM WHERE YEAR=%s"
                    v=(int(yeare),)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9')
                    tree.column('1',width=100,minwidth=0,anchor=CENTER)
                    tree.column('2',width=100,minwidth=50,anchor=CENTER)
                    tree.column('3',width=100,minwidth=50,anchor=CENTER)
                    tree.column('4',width=100,minwidth=50,anchor=CENTER)
                    tree.column('5',width=100,minwidth=50,anchor=CENTER)
                    tree.column('6',width=100,minwidth=50,anchor=CENTER)
                    tree.column('7',width=100,minwidth=50,anchor=CENTER)
                    tree.column('8',width=100,minwidth=50,anchor=CENTER)
                    tree.column('9',width=100,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=922,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','mid',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=midviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','no empty fields')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')


    def batchsearch():
        global batchmids,batchsearche,viewbatchb
        combobox1.destroy()
        sview.destroy()
        batchmids=Label(searchw,text='Academic Year',fg='black',bg='cyan3',font='Times 14')
        batchmids.place(x=70,y=10)
        batchsearche=Entry(searchw,width=20)
        batchsearche.place(x=150,y=14)
        viewbatchb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbybatch)
        viewbatchb.place(x=300,y=12) 
    def searchbybatch():
        batche=batchsearche.get()
        try:
            if batche!='':
                if batche.isdigit():
                    batchmids.destroy()
                    batchsearche.destroy() #here e.rn to m.srn
                    viewbatchb.destroy()
                    q="SELECT M.SRN,YEAR,SUB1,SUB2,SUB3,SUB4,SUB5,TOTAL,PERCENTAGE,YEAR_OF_ADMISSION FROM MID_SEM E,STUDENT_DETAILS S WHERE E.SRN=S.SRN AND S.YEAR_OF_ADMISSION=%s"
                    v=(int(batche),)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9','10')
                    tree.column('1',width=70,minwidth=0,anchor=CENTER)
                    tree.column('2',width=70,minwidth=50,anchor=CENTER)
                    tree.column('3',width=70,minwidth=50,anchor=CENTER)
                    tree.column('4',width=70,minwidth=50,anchor=CENTER)
                    tree.column('5',width=70,minwidth=50,anchor=CENTER)
                    tree.column('6',width=70,minwidth=50,anchor=CENTER)
                    tree.column('7',width=70,minwidth=50,anchor=CENTER)
                    tree.column('8',width=70,minwidth=50,anchor=CENTER)
                    tree.column('9',width=70,minwidth=50,anchor=CENTER)
                    tree.column('10',width=70,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)
                    tree.heading('10',text='YOA',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=720,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','mid',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],rec[9]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=midviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','no empty fields')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
     

        
    winview()
        
#========================================DELETE MARKS====================================================
def middel():
    global delwin
    def delete():
        global delwin,ds,db
        midsemw.withdraw() #3333333333333
        delwin=customtkinter.CTkToplevel()
        delwin.geometry("400x400+0+0")
        delwin.resizable(False,False)
        delwin.config(bg='#121111')
        dlabel=customtkinter.CTkLabel(delwin,text="SRN",font=font2,text_color='#fff',bg_color='#001220')
        dlabel.place(x=180,y=30)
        ds=customtkinter.CTkEntry(delwin,width=120)
        ds.place(x=150,y=60)
        db=customtkinter.CTkButton(delwin,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=press)
        db.place(x=180,y=90)
        backdel=customtkinter.CTkButton(delwin,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=withdraw)
        backdel.place(x=140,y=340)
    def withdraw():
        delwin.withdraw()
        midsemw.deiconify()
        
    srns=[]
    q="SELECT SRN FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srns.append(j)

    dlist=[]
    def press():
        global ds,delwin,db,yeardel,deleteb
        dentry=ds.get()
        if dentry!='':
            if int(dentry) in srns:
                if dentry.isdigit():
                    ds.configure(state='disabled')
                    db.configure(state=customtkinter.DISABLED)
                    db.destroy()
                    #db['state']=DISABLED
                    dlist.append(int(dentry))
                    year=customtkinter.CTkLabel(delwin,text='Year of Study',font=font2,text_color='#fff',bg_color='#001220')
                    year.place(x=150,y=120)
                    yeardel=customtkinter.CTkEntry(delwin,width=120)
                    yeardel.place(x=140,y=150)
                    deleteb=customtkinter.CTkButton(delwin,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=delrecord)
                    deleteb.place(x=180,y=180)
                elif entry1.isalpha():
                    messagebox.showerror('Error','Enter Integer Value of length x')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showinfo('Delete','Enter Valid SRN')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    result=[]
    q="SELECT SRN,YEAR FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        result.append(i)
        
    print(result)

    def delrecord():
        global delwin,yeardel,deleteb,dtuple
        getyear=yeardel.get()
        if getyear!='':
            if getyear.isdigit():
                dlist.append(int(getyear))
                dtuple=tuple(dlist)
                yeardel.configure(state='disabled')
                deleteb.configure(state=customtkinter.DISABLED)
                deleteb.destroy()
                #deleteb['state']=DISABLED
                final=customtkinter.CTkButton(delwin,text='Delete',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=deleterecord)
                final.place(x=130,y=220)
                        
                    
            elif entry1.isalpha():
                messagebox.showerror('Error','Enter Integer Value of length x')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def deleterecord():
        if dtuple in result:
            q="DELETE FROM MID_SEM WHERE SRN=%s and YEAR=%s"        
            cur.execute(q,list(dtuple))
            con.commit()
            messagebox.showinfo("Deletion Status","Record Deleted")
            continuedel()
        else:
            messagebox.showinfo("Deletion Status","Record Not Found")
            continuedel()
            
    def continuedel():
        again=customtkinter.CTkButton(delwin,text='Delete another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resizedel)
        again.place(x=140,y=260)

    def resizedel():
        delwin.withdraw()
        delete()

    delete()

#======================================AVERAGE OF A STUDENT===========================================
from tkinter import *
from tkinter import messagebox
import mysql.connector
import customtkinter
import matplotlib.pyplot as plt
import statistics

con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
cur=con.cursor()

def midaverage():
    def avgwindow():
        global avg,avgentry,ab
        avg=customtkinter.CTkToplevel()
        avg.geometry('300x300+0+0')
        avg.resizable(False,False)
        avg.config(bg='#121111')
        alabel=customtkinter.CTkLabel(avg,text="SRN",font=font2,text_color='#fff',bg_color='#001220')
        alabel.place(x=130,y=30)
        avgentry=customtkinter.CTkEntry(avg,width=120)
        avgentry.place(x=85,y=60)
        ab=customtkinter.CTkButton(avg,text='Next',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=pressavg)
        ab.place(x=115,y=90)
        backavg=customtkinter.CTkButton(avg,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=withdrawavg)
        backavg.place(x=75,y=260)
    def withdrawavg():
        avg.withdraw()
        #avg.deiconify()
    srnavg=[]
    q="SELECT SRN FROM MID_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srnavg.append(j)
    alist=[]
    def pressavg():
        global yearavg,yrb
        srnaverage=avgentry.get()
        if srnaverage!='':
            if srnaverage.isdigit():
                if int(srnaverage) in srnavg:
                    avgentry.configure(state='disabled')
                    ab.destroy()
                    alist.append(int(srnaverage))
                    yrb=customtkinter.CTkButton(avg,text='Search',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=avgrecord)
                    yrb.place(x=100,y=180)
                else:
                    messagebox.showerror('error','srn does not exist')
            else:
                messagebox.showerror('error','integer values only')
        else:
            messagebox.showerror('error','no empty fields allowed')


    def avgrecord():
        q='SELECT YEAR,PERCENTAGE FROM MID_SEM WHERE SRN=%s'
        v=tuple(alist)
        cur.execute(q,v)
        res=cur.fetchall()
        percentages=[]
        labelsl=[]
        for i in range(len(res)):
            percentages.append(res[i][1])
            labelsl.append(res[i][0])
        print(percentages)
        print(labelsl)
        average_percentage=statistics.mean(percentages)
        print(average_percentage)

        plt.bar(range(1,l + 1), percentages)
        plt.xlabel('Year')
        plt.ylabel('Percentage')
        plt.title('Bar Graph of Subject Marks')
        plt.grid(False)
        plt.xticks(range(1,l+1), labelsl)
        plt.show()

   
                
    font2=('Helvetica',14,'bold')
    font3=('Helvetica',13,'bold')
    avgwindow()



    

#----------------------LOGIN WINDOW-----------------------------
window=customtkinter.CTk()
window.title('Login')
window.geometry('450x360')
window.config(bg='#001220')
window.resizable(False,False)


font1=('Helvetica',25,'bold')
font2=('Helvetica',14,'bold')
font3=('Helvetica',15,'bold')
login_label=customtkinter.CTkLabel(window,text='Login',font=font1,text_color='#fff',bg_color='#001220')
login_label.place(x=280,y=20)

username=customtkinter.CTkEntry(window,font=font1,text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Username',placeholder_text_color='#a3a3a3',width=200,height=50)
username.place(x=230,y=80)

password=customtkinter.CTkEntry(window,show='*',font=font1,text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=200,height=50)
password.place(x=230,y=150)

submit=customtkinter.CTkButton(window,text='Login',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=login)
submit.place(x=230,y=220)




window.mainloop()

#----------------------------------------------------ENDSEM---------------------------------------
def endsem():
    #exam.withdraw()
    global endsemw
    exam.withdraw()
    endsemw=customtkinter.CTkToplevel()
    endsemw.geometry("700x630+0+0")
    endsemw.title('Examinations')
    endsemw.config(bg='#001220')
    endsemw.resizable(False,False)
    button1=customtkinter.CTkButton(endsemw,text='Add Scores',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=endadd)
    button1.place(x=100,y=150)
    button2=customtkinter.CTkButton(endsemw,text='View Scores',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=endview)
    button2.place(x=100,y=250)
    button3=customtkinter.CTkButton(endsemw,text='Delete Scores',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=enddel)
    button3.place(x=100,y=350)
    button4=customtkinter.CTkButton(endsemw,text='Modify Scores',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=endmodify)
    button4.place(x=100,y=450)
    button5=customtkinter.CTkButton(endsemw,text='Percentage',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=endperc)
    button5.place(x=100,y=550)
    backhome=customtkinter.CTkButton(endsemw,text='Back to Home Page',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=homeend)
    backhome.place(x=450,y=550)
def homeend():
    endsemw.withdraw()
    win2.deiconify()

#======================================================ADD SCORES=====================================
def endadd():
    global srnentry
    global end
    global ok1

    #                                  SELECT SRNS FROM STUDENT_DETAILS TO SEE IF STUDENT EXISTS.SO IN VALIDATIONS ALSO YOU INCLUDE THIS
    unique=[]
    q="SELECT SRN,YEAR FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        unique.append(i)
    srns=[]
    q="SELECT SRN FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srns.append(j)

    existing=[]
    q="SELECT SRN FROM STUDENT_DETAILS"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            existing.append(j)

    data=[]
    def getsrn():
        global end
        global srnentry
        global yearentry,entry1
        global ok1,ok2
        entry1=srnentry.get()
        try:
            if entry1!='':
                if entry1.isdigit():
                    if int(entry1) in existing:
                        data.append(entry1)
                        srnentry.configure(state='disabled')
                        ok1.configure(state=customtkinter.DISABLED)
                        ok1.destroy()
                        year=customtkinter.CTkLabel(end,text='Year of Study',font=font2,text_color='#fff',bg_color='#001220')
                        year.place(x=100,y=50)
                        colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                        colon.place(x=220,y=50)
                        yearentry=customtkinter.CTkEntry(end,width=120)
                        yearentry.place(x=250,y=50)
                        ok2=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getyear)
                        ok2.place(x=400,y=50)
                    else:
                        messagebox.showerror('error','SRN Does Not Exists')
                elif entry1.isalpha():
                    messagebox.showerror('Error','Enter Integer Value of length x')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Empty fields not allowed')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def getyear():
        global yearentry,sub1entry,entry2
        global end
        global ok2,ok3
        entry2=yearentry.get()
        try:
            if entry2!='':
                if entry2.isdigit() and len(entry2)==4:
                    if (int(entry1),int(entry2)) not in unique:
                        data.append(entry2)
                        yearentry.configure(state='disabled')
                        ok2.configure(state=customtkinter.DISABLED)
                        ok2.destroy()
                        #ok2['state']=DISABLED
                        sub1=customtkinter.CTkLabel(end,text='Subject 1',font=font2,text_color='#fff',bg_color='#001220')
                        sub1.place(x=100,y=90)
                        colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                        colon.place(x=220,y=90)
                        sub1entry=customtkinter.CTkEntry(end,width=120)
                        sub1entry.place(x=250,y=90)
                        ok3=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=getsub1)
                        ok3.place(x=400,y=90)
                    else:
                        messagebox.showerror('Error','Record Exists')
                        end.withdraw()
                        endadd()
                        #winadd()
                elif entry2.isalpha():
                    messagebox.showerror('Error','Enter Integer Value')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Empty fields not allowed')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def getsub1():
        global sub1entry,sub2entry
        global end,ok3,ok4
        entry3=sub1entry.get()
        if entry3!='':
            if entry3.isdigit() and int(entry3)<=100:
                data.append(entry3)
                sub1entry.configure(state='disabled')
                ok3.configure(state=customtkinter.DISABLED)
                ok3.destroy()
                #ok3['state']=DISABLED
                sub2=customtkinter.CTkLabel(end,text='Subject 2',font=font2,text_color='#fff',bg_color='#001220')
                sub2.place(x=100,y=130)
                colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=130)
                sub2entry=customtkinter.CTkEntry(end,width=120)
                sub2entry.place(x=250,y=130)
                ok4=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub2)
                ok4.place(x=400,y=130)
            elif entry3.isalpha():
                messagebox.showerror('Error','Enter Integer Value within 100')
            else:
                messagebox.showerror('Error','Enter Integer Value within 100')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub2():
        global end,sub2entry,sub3entry,ok4,ok5
        entry4=sub2entry.get()
        if entry4!='':
            if entry4.isdigit() and int(entry4)<=100:
                data.append(entry4)
                sub2entry.configure(state='disabled')
                ok4.configure(state=customtkinter.DISABLED)
                ok4.destroy()
                #ok4['state']=DISABLED
                sub3=customtkinter.CTkLabel(end,text='Subject 3',font=font2,text_color='#fff',bg_color='#001220')
                sub3.place(x=100,y=170)
                colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=170)
                sub3entry=customtkinter.CTkEntry(end,width=120)
                sub3entry.place(x=250,y=170)
                ok5=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub3)
                ok5.place(x=400,y=170)        
            elif entry4.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')


    def getsub3():
        global end,sub3entry,sub4entry,ok5,ok6
        entry5=sub3entry.get()
        if entry5!='':
            if entry5.isdigit() and int(entry5)<=100:
                data.append(entry5)
                sub3entry.configure(state='disabled')
                ok5.configure(state=customtkinter.DISABLED)
                ok5.destroy()
                #ok5['state']=DISABLED
                sub4=customtkinter.CTkLabel(end,text='Subject 4',font=font2,text_color='#fff',bg_color='#001220')
                sub4.place(x=100,y=210)
                colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=210)
                sub4entry=customtkinter.CTkEntry(end,width=120)
                sub4entry.place(x=250,y=210)
                ok6=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub4)
                ok6.place(x=400,y=210)
            elif entry5.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub4():
        global end,sub4entry,sub5entry,ok6,ok7
        entry6=sub4entry.get()
        if entry6!='':
            if entry6.isdigit() and int(entry6)<=100:
                data.append(entry6)
                sub4entry.configure(state='disabled')
                ok6.configure(state=customtkinter.DISABLED)
                ok6.destroy()
                #ok6['state']=DISABLED
                sub5=customtkinter.CTkLabel(end,text='Subject 5',font=font2,text_color='#fff',bg_color='#001220')
                sub5.place(x=100,y=250)
                colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
                colon.place(x=220,y=250)
                sub5entry=customtkinter.CTkEntry(end,width=120)
                sub5entry.place(x=250,y=250)
                ok7=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsub5)
                ok7.place(x=400,y=250)
            elif entry6.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def getsub5():
        global end,sub5entry,ok7
        entry7=sub5entry.get()
        if entry7!='':
            if entry7.isdigit() and int(entry7)<=100:
                data.append(entry7)
                sub5entry.configure(state='disabled')
                ok7.configure(state=customtkinter.DISABLED)
                ok7.destroy()
                #ok7['state']=DISABLED
                button=customtkinter.CTkButton(end,text='Enter Details',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=details)
                button.place(x=270,y=300)
            elif entry7.isalpha():
                messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def details():
        tlist=data[2:7]
        marks=[]
        for i in tlist:
            j=int(i)
            marks.append(j)
        #print(sum(marks))
        total=sum(marks)
        perc=total/5
        data.append(total)
        data.append(perc)
        print(data)
        q="INSERT INTO end_sem VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        v=tuple(data)
        cur.execute(q,v)
        con.commit()
        messagebox.showinfo("Details","Details entered")
        continue1()

    def endremove():
        end.withdraw()
        endadd()
        #end.deiconify()

    def continue1():
        again=customtkinter.CTkButton(end,text='Add another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=endremove)
        again.place(x=250,y=350)

    def resize1():
        end.withdraw()
        endsemw.deiconify()
        
    endsemw.withdraw()
    end=customtkinter.CTkToplevel()
    end.geometry("500x450+0+0")
    end.resizable(False,False)
    end.config(bg='#121111')
    srn=customtkinter.CTkLabel(end,text='SRN',font=font2,text_color='#fff',bg_color='#001220')
    srn.place(x=100,y=10)
    #info=customtkinter.CTkLabel(end,text='(Student Registration Number)',font=font1,text_color='#fff',bg_color='#001220')
    #info.place(x=20,y=30)
    colon=customtkinter.CTkLabel(end,text=':',font=font3,text_color='#fff',bg_color='#001220')
    colon.place(x=220,y=10)
    srnentry=customtkinter.CTkEntry(end,width=120)
    srnentry.place(x=250,y=10)
    ok1=customtkinter.CTkButton(end,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=getsrn)
    ok1.place(x=400,y=10)
    back=customtkinter.CTkButton(end,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resize1)
    back.place(x=190,y=400)



#===============================MODIFY SCORES===========================================
#DISABLING BUTTONS AND ENTRY-TO DO
def endmodify():
    def modify():
        global mw,mb,comboboxm
        mw=customtkinter.CTkToplevel()
        mw.title('Modify')
        mw.geometry('500x500+0+0')
        mw.resizable(False,False)
        mw.configure(bg='#001220')
        mb=customtkinter.CTkLabel(mw,text='Modify Record',font=font2,text_color='#fff',bg_color='#001220')
        mb.place(x=100,y=10)
        comboboxm=ttk.Combobox(mw)
        comboboxm.config(values=['Subject1','Subject2','Subject3','Subject4','Subject5'])
        comboboxm.set("Select An Option")
        comboboxm.bind("<<ComboboxSelected>>",on_selectm)
        comboboxm.place(x=320,y=18)
        b2menu=customtkinter.CTkButton(mw,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=b2menuf)
        b2menu.place(x=380,y=400)
    def b2menuf():
        mw.withdraw()
        endsemw.deiconify()
        

    def on_selectm(event):
        global selected
        selected=event.widget.get()
        print(selected)
        mod1()

    modsrn=[]
    q='select srn from end_sem'
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            modsrn.append(j)
    modsrnstud=[]
    q='select srn from student_details'
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            modsrnstud.append(j)

    def mod1():
        global m1entry,modb
        comboboxm.destroy()
        mb.destroy()
        mb1=customtkinter.CTkLabel(mw,text='SRN',font=font2,text_color='#fff',bg_color='#001220')
        mb1.place(x=100,y=10)
        m1entry=customtkinter.CTkEntry(mw,width=120)
        m1entry.place(x=230,y=14)
        modb=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod)
        modb.place(x=380,y=12)
    #getting srn to modify
    def sub1mod():
        global modb2,m1entry2,sub1entry
        sub1entry=m1entry.get()
        if sub1entry!='' and int(sub1entry) in modsrn: #and int(sub1entry) in modsrnstud
            if sub1entry.isdigit():
                modb.destroy()
                mb2=customtkinter.CTkLabel(mw,text='Academic Year',font=font2,text_color='#fff',bg_color='#001220')
                mb2.place(x=100,y=70)
                m1entry2=customtkinter.CTkEntry(mw,width=120)
                m1entry2.place(x=230,y=64)
                modb2=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod2)
                modb2.place(x=380,y=62)
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Enter Integer Value')

    uniquemod=[]
    q="SELECT SRN,YEAR FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        uniquemod.append(i)

    def sub1mod2():
        global modb2,m1entry3,modyearentry
        modyearentry=m1entry2.get()
        if modyearentry!='':
            if modyearentry.isdigit() and len(modyearentry)==4:
                if (int(sub1entry),int(modyearentry)) in uniquemod:
                    modb2.destroy()
                    mb3=customtkinter.CTkLabel(mw,text='Enter New Score',font=font2,text_color='#fff',bg_color='#001220')
                    mb3.place(x=70,y=130)
                    m1entry3=customtkinter.CTkEntry(mw,width=120)
                    m1entry3.place(x=230,y=114)
                    modb2=customtkinter.CTkButton(mw,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=sub1mod3)
                    modb2.place(x=380,y=112)
                else:
                    messagebox.showerror('Error','Record does not exist')
                    modify()
            elif modyearentry.isalpha():
                messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','enter valid year of length 4')
        else:
            messagebox.showerror('error','no empty fields allowed')

    def sub1mod3():
        newsub1=m1entry3.get()
        if newsub1!='':
            if newsub1.isdigit() and int(newsub1)<=100:
                if selected=='Subject1':
                    q='UPDATE END_SEM SET SUB1=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject2':
                    q='UPDATE END_SEM SET SUB2=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject3':
                    q='UPDATE END_SEM SET SUB3=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject4':
                    q='UPDATE END_SEM SET SUB4=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                elif selected=='Subject5':
                    q='UPDATE END_SEM SET SUB5=%s WHERE SRN=%s AND YEAR=%s'
                    v=(int(newsub1),int(sub1entry),int(modyearentry))
                cur.execute(q,v)
                con.commit()
                messagebox.showinfo('Done','Record Modified')
                newmodify()
            elif newsub1.isalpha():
                messagebox.showerror('error','integer value only')
        else:
            messagebox.showerrror('error','no empty fields')

    def newmodify():
        modifynew=customtkinter.CTkButton(mw,text='Modify Another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=modifyagain)
        modifynew.place(x=100,y=400)

    def modifyagain():
        mw.withdraw()
        modify()

    modify()


#==============================VIEW/SEARCH SCORES====================================
def endview():
    global view
    def winview():
        global view,okbv,searchl,oksearch,backall
        endsemw.withdraw()        
        view=customtkinter.CTkToplevel()
        view.geometry("700x400+0+0")
        view.resizable(False,False)
        view.config(bg='#121111')
        allview=Label(view,text='View All',fg='black',bg='cyan3',font='Times 14')
        allview.place(x=100,y=10)
        searchl=Label(view,text='Search By',fg='black',bg='cyan3',font='Times 14')
        searchl.place(x=100,y=50)
        oksearch=Button(view,text='Search',bg='cornsilk',fg='black',command=searchscore)
        oksearch.place(x=200,y=50)
        okbv=Button(view,text='View',bg='cornsilk',fg='black',command=viewall)
        okbv.place(x=200,y=10)
        backall=customtkinter.CTkButton(view,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resizeviewwindow)
        backall.place(x=400,y=350)

    def resizeviewwindow():
        view.withdraw()
        endsemw.deiconify()
    def viewall():
        global view,okbv
        searchl.destroy()
        oksearch.destroy()
        q="SELECT * FROM END_SEM"
        cur.execute(q)
        res=cur.fetchall()
        okbv['state']=DISABLED

        s=ttk.Style(view)
        s.theme_use('default')
        tree=ttk.Treeview(view)
        tree['show']='headings'
        tree['columns']=('1','2','3','4','5','6','7','8','9')
        tree.column('1',width=100,minwidth=0,anchor=CENTER)
        tree.column('2',width=100,minwidth=50,anchor=CENTER)
        tree.column('3',width=100,minwidth=50,anchor=CENTER)
        tree.column('4',width=100,minwidth=50,anchor=CENTER)
        tree.column('5',width=100,minwidth=50,anchor=CENTER)
        tree.column('6',width=100,minwidth=50,anchor=CENTER)
        tree.column('7',width=100,minwidth=50,anchor=CENTER)
        tree.column('8',width=100,minwidth=50,anchor=CENTER)
        tree.column('9',width=100,minwidth=50,anchor=CENTER)

        tree.heading('1',text='SRN',anchor=CENTER)
        tree.heading('2',text='Academic Year',anchor=CENTER)
        tree.heading('3',text='Subject1',anchor=CENTER)
        tree.heading('4',text='Subject2',anchor=CENTER)
        tree.heading('5',text='Subject3',anchor=CENTER)
        tree.heading('6',text='Subject4',anchor=CENTER)
        tree.heading('7',text='Subject5',anchor=CENTER)
        tree.heading('8',text='Total',anchor=CENTER)
        tree.heading('9',text='Percentage',anchor=CENTER)

        sb = ttk.Scrollbar(view, orient="vertical", command=tree.yview)
        sb.place(x=922,y=70, height=225)
        tree.configure(yscrollcommand=sb.set)
        for rec in res:
            tree.insert('','end',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
        tree.place(x=20,y=70)
        backall.destroy()
        back=customtkinter.CTkButton(view,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=endviewrem)
        back.place(x=400,y=350)
    def endviewrem():
        view.withdraw()

    def searchscore():
        global combobox1,searchw,sview
        view.withdraw()
        searchw=customtkinter.CTkToplevel()
        searchw.geometry("700x400+0+0")
        searchw.resizable(False,False)
        searchw.config(bg='#121111')
        sview=Label(searchw,text='Search By',fg='black',bg='cyan3',font='Times 14')
        sview.place(x=70,y=10)
        combobox1=ttk.Combobox(searchw)
        combobox1.config(values=['SRN','Academic Year','Year of Admission'])
        combobox1.set("Select An Option")
        combobox1.bind("<<ComboboxSelected>>",on_select)
        combobox1.place(x=170,y=15)
    def on_select(event):
        selected_item=event.widget.get()
        print(selected_item)
        if selected_item=="SRN":
            srnsearch()
        elif selected_item=='Academic Year':
            yearsearch()
        elif selected_item=='Year of Admission':
            batchsearch()
    def srnsearch():
        global ent,entb,srnends
        combobox1.destroy()
        sview.destroy()
        srnends=Label(searchw,text='SRN',fg='black',bg='cyan3',font='Times 14')
        srnends.place(x=70,y=10)
        ent=Entry(searchw,width=20)
        ent.place(x=150,y=14)
        entb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbysrn)
        entb.place(x=300,y=12)
        
        q="SELECT * FROM END_SEM WHERE SRN==%s"

    numbers=[]
    q="SELECT SRN FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            numbers.append(j)

    def searchbysrn():
        number=ent.get()
        try:
            if number!='' and int(number) in numbers:
                if number.isdigit():
                    ts=int(number)
                    entb.destroy()
                    ent.destroy()
                    srnends.destroy()
                    q="SELECT * FROM END_SEM WHERE SRN=%s"
                    v=(ts,)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9')
                    tree.column('1',width=100,minwidth=0,anchor=CENTER)
                    tree.column('2',width=100,minwidth=50,anchor=CENTER)
                    tree.column('3',width=100,minwidth=50,anchor=CENTER)
                    tree.column('4',width=100,minwidth=50,anchor=CENTER)
                    tree.column('5',width=100,minwidth=50,anchor=CENTER)
                    tree.column('6',width=100,minwidth=50,anchor=CENTER)
                    tree.column('7',width=100,minwidth=50,anchor=CENTER)
                    tree.column('8',width=100,minwidth=50,anchor=CENTER)
                    tree.column('9',width=100,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=922,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','end',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=endviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showinfo('Delete','Enter Valid SRN')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
    def endviewrem2():
        searchw.withdraw()
        
        
    def yearsearch():
        global yearends,yearsearche,viewyearb
        combobox1.destroy()
        sview.destroy()
        yearends=Label(searchw,text='Academic Year',fg='black',bg='cyan3',font='Times 14')
        yearends.place(x=70,y=10)
        yearsearche=Entry(searchw,width=20)
        yearsearche.place(x=150,y=14)
        viewyearb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbyyear)
        viewyearb.place(x=300,y=12)
    def searchbyyear():
        yeare=yearsearche.get()
        try:
            if yeare!='':
                if yeare.isdigit():
                    yearends.destroy()
                    yearsearche.destroy()
                    viewyearb.destroy()
                    q="SELECT * FROM END_SEM WHERE YEAR=%s"
                    v=(int(yeare),)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9')
                    tree.column('1',width=100,minwidth=0,anchor=CENTER)
                    tree.column('2',width=100,minwidth=50,anchor=CENTER)
                    tree.column('3',width=100,minwidth=50,anchor=CENTER)
                    tree.column('4',width=100,minwidth=50,anchor=CENTER)
                    tree.column('5',width=100,minwidth=50,anchor=CENTER)
                    tree.column('6',width=100,minwidth=50,anchor=CENTER)
                    tree.column('7',width=100,minwidth=50,anchor=CENTER)
                    tree.column('8',width=100,minwidth=50,anchor=CENTER)
                    tree.column('9',width=100,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=922,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','end',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=endviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','no empty fields')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')


    def batchsearch():
        global batchends,batchsearche,viewbatchb
        combobox1.destroy()
        sview.destroy()
        batchends=Label(searchw,text='Academic Year',fg='black',bg='cyan3',font='Times 14')
        batchends.place(x=70,y=10)
        batchsearche=Entry(searchw,width=20)
        batchsearche.place(x=150,y=14)
        viewbatchb=Button(searchw,text='View',bg='cornsilk',fg='black',command=searchbybatch)
        viewbatchb.place(x=300,y=12) 
    def searchbybatch():
        batche=batchsearche.get()
        try:
            if batche!='':
                if batche.isdigit():
                    batchends.destroy()
                    batchsearche.destroy()
                    viewbatchb.destroy()
                    q="SELECT E.SRN,YEAR,SUB1,SUB2,SUB3,SUB4,SUB5,TOTAL,PERCENTAGE,YEAR_OF_ADMISSION FROM END_SEM E,STUDENT_DETAILS S WHERE E.SRN=S.SRN AND S.YEAR_OF_ADMISSION=%s"
                    v=(int(batche),)
                    cur.execute(q,v)
                    res=cur.fetchall()
                    s=ttk.Style(searchw)
                    s.theme_use('default')
                    tree=ttk.Treeview(searchw)
                    tree['show']='headings'
                    tree['columns']=('1','2','3','4','5','6','7','8','9','10')
                    tree.column('1',width=70,minwidth=0,anchor=CENTER)
                    tree.column('2',width=70,minwidth=50,anchor=CENTER)
                    tree.column('3',width=70,minwidth=50,anchor=CENTER)
                    tree.column('4',width=70,minwidth=50,anchor=CENTER)
                    tree.column('5',width=70,minwidth=50,anchor=CENTER)
                    tree.column('6',width=70,minwidth=50,anchor=CENTER)
                    tree.column('7',width=70,minwidth=50,anchor=CENTER)
                    tree.column('8',width=70,minwidth=50,anchor=CENTER)
                    tree.column('9',width=70,minwidth=50,anchor=CENTER)
                    tree.column('10',width=70,minwidth=50,anchor=CENTER)

                    tree.heading('1',text='SRN',anchor=CENTER)
                    tree.heading('2',text='Academic Year',anchor=CENTER)
                    tree.heading('3',text='Subject1',anchor=CENTER)
                    tree.heading('4',text='Subject2',anchor=CENTER)
                    tree.heading('5',text='Subject3',anchor=CENTER)
                    tree.heading('6',text='Subject4',anchor=CENTER)
                    tree.heading('7',text='Subject5',anchor=CENTER)
                    tree.heading('8',text='Total',anchor=CENTER)
                    tree.heading('9',text='Percentage',anchor=CENTER)
                    tree.heading('10',text='YOA',anchor=CENTER)

                    sb = ttk.Scrollbar(searchw, orient="vertical", command=tree.yview)
                    sb.place(x=720,y=70, height=225)
                    tree.configure(yscrollcommand=sb.set)
                    for rec in res:
                        tree.insert('','end',text='',values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],rec[9]))
                    tree.place(x=20,y=70)
                    back=Button(searchw,text='Back to Menu',fg='black',bg='yellow',font=('Times New Roman',14),command=endviewrem2)
                    back.place(x=400,y=350)
                else:
                    messagebox.showerror('error','enter integer value')
            else:
                messagebox.showerror('error','no empty fields')
        except ValueError:
            messagebox.showerror('Error','Enter Integer Value')
     

        
    winview()
        
#========================================DELETE MARKS====================================================
def enddel():
    global delwin
    def delete():
        global delwin,ds,db
        endsemw.withdraw() #3333333333333
        delwin=customtkinter.CTkToplevel()
        delwin.geometry("400x400+0+0")
        delwin.resizable(False,False)
        delwin.config(bg='#121111')
        dlabel=customtkinter.CTkLabel(delwin,text="SRN",font=font2,text_color='#fff',bg_color='#001220')
        dlabel.place(x=180,y=30)
        ds=customtkinter.CTkEntry(delwin,width=120)
        ds.place(x=150,y=60)
        db=customtkinter.CTkButton(delwin,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=press)
        db.place(x=180,y=90)
        backdel=customtkinter.CTkButton(delwin,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=withdraw)
        backdel.place(x=140,y=340)
    def withdraw():
        delwin.withdraw()
        endsemw.deiconify()
        
    srns=[]
    q="SELECT SRN FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srns.append(j)

    dlist=[]
    def press():
        global ds,delwin,db,yeardel,deleteb
        dentry=ds.get()
        if dentry!='':
            if int(dentry) in srns:
                if dentry.isdigit():
                    ds.configure(state='disabled')
                    db.configure(state=customtkinter.DISABLED)
                    db.destroy()
                    #db['state']=DISABLED
                    dlist.append(int(dentry))
                    year=customtkinter.CTkLabel(delwin,text='Year of Study',font=font2,text_color='#fff',bg_color='#001220')
                    year.place(x=150,y=120)
                    yeardel=customtkinter.CTkEntry(delwin,width=120)
                    yeardel.place(x=140,y=150)
                    deleteb=customtkinter.CTkButton(delwin,text='Next',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=delrecord)
                    deleteb.place(x=180,y=180)
                elif entry1.isalpha():
                    messagebox.showerror('Error','Enter Integer Value of length x')
                else:
                    messagebox.showerror('Error','Enter Integer Value')
            else:
                messagebox.showinfo('Delete','Enter Valid SRN')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    result=[]
    q="SELECT SRN,YEAR FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        result.append(i)
        
    print(result)

    def delrecord():
        global delwin,yeardel,deleteb,dtuple
        getyear=yeardel.get()
        if getyear!='':
            if getyear.isdigit():
                dlist.append(int(getyear))
                dtuple=tuple(dlist)
                yeardel.configure(state='disabled')
                deleteb.configure(state=customtkinter.DISABLED)
                deleteb.destroy()
                #deleteb['state']=DISABLED
                final=customtkinter.CTkButton(delwin,text='Delete',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=deleterecord)
                final.place(x=130,y=220)
                    
            elif entry1.isalpha():
                messagebox.showerror('Error','Enter Integer Value of length x')
            else:
                messagebox.showerror('Error','Enter Integer Value')
        else:
            messagebox.showerror('Error','Empty fields not allowed')

    def deleterecord():
        if dtuple in result:
            q="DELETE FROM END_SEM WHERE SRN=%s and YEAR=%s"        
            cur.execute(q,list(dtuple))
            con.commit()
            messagebox.showinfo("Deletion Status","Record Deleted")
            continuedel()
        else:
            messagebox.showinfo("Deletion Status","Record Not Found")
            continuedel()
            
    def continuedel():
        again=customtkinter.CTkButton(delwin,text='Delete another Record',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=resizedel)
        again.place(x=140,y=260)

    def resizedel():
        delwin.withdraw()
        delete()

    delete()

#======================================PERCENTAGE OF A STUDENT===========================================
def endperc():
    def avgwindow():
        endsemw.withdraw()
        global avg,avgentry,ab
        avg=customtkinter.CTkToplevel()
        avg.geometry('300x300+0+0')
        avg.resizable(False,False)
        avg.config(bg='#121111')
        alabel=customtkinter.CTkLabel(avg,text="SRN",font=font2,text_color='#fff',bg_color='#001220')
        alabel.place(x=130,y=30)
        avgentry=customtkinter.CTkEntry(avg,width=120)
        avgentry.place(x=85,y=60)
        ab=customtkinter.CTkButton(avg,text='Next',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=pressavg)
        ab.place(x=115,y=90)
        backavg=customtkinter.CTkButton(avg,text='Back to Menu',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font3,command=withdrawavg)
        backavg.place(x=75,y=260)
    def withdrawavg():
        avg.withdraw()
        endsemw.deiconify()
        #deiconify endsem
    srnavg=[]
    q="SELECT SRN FROM END_SEM"
    cur.execute(q)
    res=cur.fetchall()
    for i in res:
        for j in i:
            srnavg.append(j)
    alist=[]
    def pressavg():
        global yearavg,yrb
        srnaverage=avgentry.get()
        if srnaverage!='':
            if srnaverage.isdigit():
                if int(srnaverage) in srnavg:
                    avgentry.configure(state='disabled')
                    ab.destroy()
                    alist.append(int(srnaverage))
                    yrb=customtkinter.CTkButton(avg,text='Search',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font3,command=avgrecord)
                    yrb.place(x=100,y=180)
                else:
                    messagebox.showerror('error','srn does not exist')
            else:
                messagebox.showerror('error','integer values only')
        else:
            messagebox.showerror('error','no empty fields allowed')


    def avgrecord():
        q='SELECT YEAR,PERCENTAGE FROM END_SEM WHERE SRN=%s'
        v=tuple(alist)
        cur.execute(q,v)
        res=cur.fetchall()
        percentages=[]
        labelsl=[]
        for i in range(len(res)):
            percentages.append(res[i][1])
            labelsl.append(res[i][0])
        print(percentages)
        l=len(percentages)
        print(labelsl)
        average_percentage=statistics.mean(percentages)
        print(average_percentage)

        plt.bar(range(1,l+1),percentages)
        plt.xlabel('Year')
        plt.ylabel('Percentage')
        plt.title('Bar Graph of Subject Marks')
        plt.grid(False)
        plt.xticks(range(1,l+1),labelsl)
        plt.show()
            
            
            
    font2=('Helvetica',14,'bold')
    font3=('Helvetica',13,'bold')
    avgwindow()
    

#-----------------------------------------------------login window----------------------------------------------------------------------

window=customtkinter.CTk()
window.title('Login')
window.geometry('450x360')
window.config(bg='#001220')
window.resizable(False,False)

def binaryfileabout():
    import binaryfile
'''    
bgimage = ImageTk.PhotoImage(file='bgimg.jpg')
bglabel = Label(window, image=bgimage)
bglabel.place(x=0, y=0)'''    
img=Image.open("loginwindow.jpg")
r=img.resize((340,550))
im=ImageTk.PhotoImage(r)
label2=Label(window,image=im,bd=0)
label2.pack(side=LEFT)

font1=('Helvetica',25,'bold')
font2=('Helvetica',14,'bold')
font3=('Helvetica',15,'bold')
login_label=customtkinter.CTkLabel(window,text='Login',font=font1,text_color='#fff',bg_color='#001220')
login_label.place(x=280,y=20)

username=customtkinter.CTkEntry(window,font=font1,text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Username',placeholder_text_color='#a3a3a3',width=200,height=50)
username.place(x=230,y=80)

password=customtkinter.CTkEntry(window,show='*',font=font1,text_color='#fff',fg_color='#001a2e',bg_color='#121111',border_color='#004780',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=200,height=50)
password.place(x=230,y=150)

submit=customtkinter.CTkButton(window,text='Login',text_color='#fff',fg_color='#00965d',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=120,font=font1,command=login)
submit.place(x=230,y=220)

about=customtkinter.CTkButton(window,text='About',text_color='#fff',fg_color='pink',hover_color='#006e44',bg_color='#121111',cursor='hand2',corner_radius=5,width=70,font=font2,command=binaryfileabout)
about.place(x=340,y=320)

window.mainloop()
