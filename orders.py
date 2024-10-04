#!C:\Python\python.exe
import cgi
import mysql.connector
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>","Welcome","</h1>")
form=cgi.FieldStorage()
fname=form.getvalue("name")
fpass=form.getvalue("pass")
fflavour=form.getvalue("flavour")
fquantity=form.getvalue("quantity")
femail=form.getvalue("email")
fmobile=form.getvalue("mobileno")
faddress=form.getvalue("address")
print("<h1>",fname,fpass,fflavour,fquantity,femail,fmobile,faddress,"</h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scoopsafari")
mycursor=mydb.cursor()
sql="INSERT INTO orders(Name,Password,Flavour,Quantity,Email,MobileNumber,Address) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=(fname,fpass,fflavour,fquantity,femail,fmobile,faddress)
mycursor.execute(sql,val)
mydb.commit()
print("</body>")
print("</html>")
