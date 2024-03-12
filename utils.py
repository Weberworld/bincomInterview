import mysql.connector
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="Weber",
      password="manuels2385."
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE polls")
    print("Done")
    mycursor.close()
except Exception:
    pass

mydb = mysql.connector.connect(
  host="localhost",
  user="Weber",
  password="manuels2385.",
db="polls"
)

mycursor = mydb.cursor()
mycursor.execute(open("bincom_test.sql").read())
mycursor.close()


# mycursor.execute("SELECT * FROM `agentname`")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


