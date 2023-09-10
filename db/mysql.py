import mysql.connector
from config import configData

mydb = mysql.connector.connect(
  host=configData['mysql']['host'],
  user=configData['mysql']['user'],
  password=configData['mysql']['password'],
  database=configData['mysql']['database']
)

cursor = mydb.cursor(dictionary = True)

def insertdbMYSQL(id):

  sql = 'INSERT INTO users (ID) VALUES ({0})'.format(id)

  cursor.execute(sql)

def verifyidMYSQL(id):

  query = 'SELECT * FROM users WHERE ID = {0}'.format(id)
  
  cursor.execute(query)

  myresult = cursor.fetchone()

  if myresult != None:

    return 1