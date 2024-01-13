import sqlite3
# SQlite: Are a database simple to the python you can use all comand from mySQL

# You need from a connect and one cursor

conn = sqlite3.connect('Banco_ei.db')

cursor = conn.cursor()
# cursor.execute("insert into Usuarios (id,nome) values ('1','Kaua')")
# cursor.execute("insert into Usuarios (id,nome) values ('2','Lucas')")
# cursor.execute("insert into Usuarios (id,nome) values ('3','Pedro')")
# cursor.execute("insert into Usuarios (id,nome) values ('4','Luiza')")
# You use the commit to save alter 
conn.commit()

Cunsuta = cursor.execute('Select * from Usuarios')
print(Cunsuta.fetchall())