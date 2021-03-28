import sqlite3


connection = sqlite3.connect('scheduler.db')

# create a cursor for working with DB
cursor = connection.cursor()


# commit changes to the DB
connection.commit()

# close connection with DB
connection.close()
