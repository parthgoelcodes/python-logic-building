import sqlite3
conn = sqlite3.connect("std_details.db")
c = conn.cursor()

a = """CREATE TABLE std(
       Rollno INTEGER PRIMARY KEY, 
       Name TEXT, 
       Grade TEXT, 
       Email TEXT, 
       Phoneno TEXT 
       
 );
 """

c.execute(a)
conn.commit()
print("data added scussfully")
conn.close()