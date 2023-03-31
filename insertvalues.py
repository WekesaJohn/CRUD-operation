import sqlite3
jinn = sqlite3.connect("employee.db")
print("Connected")

jinn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(1,'John','Mbappe',21,45000.00,'Director')")
jinn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(2,'Hussein','Wekesa',23,45000.00,'Caretaker')")
jinn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(3,'Massud','THogan', 22 ,45000.00,'Plant operator')")
jinn.execute(" INSERT INTO Staff(ID , FIRSTNAME , LASTNAME , AGE , SALARY, TASK) \
VALUES(4,'KIngsly','Comman',25,45000.00,'Driver')")
jinn.execute(" INSERT INTO Staff (ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK) \
VALUES(5,'Mykhaylo','Mudryk',31,45000.00,'Manager')")

jinn.commit()
print("Inserted values successfully into staff table")
jinn.close()