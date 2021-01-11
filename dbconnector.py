from mysql.connector import connect, Error
import os


try:
  with connect(host="localhost",user=os.environ.get("DB_USER"),password=os.environ.get("DB_PASS")) as connection:
    print(connection)
except Error as e:
  print(e)

