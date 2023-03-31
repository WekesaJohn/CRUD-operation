import sqlite3
jinn = sqlite3.connect("employee.db")
print("connect successfull")

jinn.execute("UPDATE Staff set SALARY=50000 WHERE ID=1")
jinn.commit()

data = jinn.execute("SELECT * FROM Staff")

for rows in data:
    print("ID:",rows[0])
    print("FIRSTNAME:",rows[1])
    print("LASTNAME:",rows[2])
    print("AGE:",rows[3])
    print("SALARY:",rows[4])
    print("TASK:",rows[5])

print("successfully updated salary")
jinn.close()