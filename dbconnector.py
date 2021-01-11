from mysql.connector import connect, Error
import os
from datetime import datetime

try:
  with connect(host="localhost",user=os.environ.get("DB_USER"),password=os.environ.get("DB_PASS")) as connection:
    print(connection)
except Error as e:
  print(e)

now = datetime.now()

FirstName = "test" 
LastName =  "test"
VoteOn =    "test"
date = now.strftime("%Y-%m-%d %H:%M:%S")


dataAddQuery="""
UPDATE
      voted
SET
      FirstName = "%s"
      LastName = "%s"
      VoteOn = "%s"
      Date = "%s"
""" % (
  FirstName,
  LastName,
  VoteOn,
  date
)

print(dataAddQuery)

#with connection.cursor() as cursor:
 # cursor.execute()
  #connection.commit()