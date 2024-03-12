import os

import mysql.connector
try:
    mydb = mysql.connector.connect(
      host=os.getenv("DATABASE_HOST"),
      user=os.getenv("DATABASE_USER"),
      password=os.getenv("DATABASE_PSWD")
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE polls")
    print("Done")
    mycursor.close()
except Exception:
    pass

mydb = mysql.connector.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PSWD"),
    db=os.getenv("DATABASE_NAME")
)

mycursor = mydb.cursor()
mycursor.execute(open("bincom_test.sql").read())
mycursor.close()



