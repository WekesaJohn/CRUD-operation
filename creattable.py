import sqlite3

jinn = sqlite3.connect("employee.db")
print("Connect successifully")

jinn.execute("""CREATE TABLE Staff(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL, 
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(50))""")

print("Successfully created staff table")

jinn.close()