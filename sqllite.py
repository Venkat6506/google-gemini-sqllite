import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table="""
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table)

cursor.execute("""INSERT INTO STUDENT VALUES('Satya','Data Science','A',80)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Amit','Data Science','B',80)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Bibhu','DevOps','A',96)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Bisu','Prompt Engineer','A',98)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Sarada','DevOps','A',85)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Gudu','Data Science','A',87)""")
cursor.execute("""INSERT INTO STUDENT VALUES('Prima','Prompt Engineer','B',93)""")

print()
data=cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)


cursor.close()
connection.commit()
connection.close()

