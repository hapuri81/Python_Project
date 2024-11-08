import pyodbc as odbc
import csv

conn_str = (
    r'Driver=SQL Server;' +
    r'Server=HARIKA-THINKPAD\SQLEXPRESS;' +
    r'Database=NYCTaxi;' +
    r'Trusted_Connection=yes;'
)




def sql_statement(sql_st, file_name):
    conn = odbc.connect(conn_str)
    with conn.cursor() as cursor:
    # Read data from database
       cursor.execute(sql_st)
    # Fetch all rows
       columns = [desc[0] for desc in cursor.description]
       rows = cursor.fetchall()
       for row in rows:
            print(row)

    c = csv.writer(open(file_name,"w"))
    c.writerows(rows)
    conn.close()
emp = "select * from nyctaxi_sample where total_amount < 0"
emp2 = "select * from nyctaxi_sample where total_amount > 200"
sql_statement(emp, "temp3.csv")
sql_statement(emp2,"temp2.csv")