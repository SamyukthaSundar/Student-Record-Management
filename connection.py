import mysql.connector
global cur
con=mysql.connector.connect(host='localhost',user='root',password='123456',db='clg')
cur=con.cursor()
