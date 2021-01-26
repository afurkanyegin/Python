import sqlite3

conn=sqlite3.connect('customer.db')

c= conn.cursor()

many_customers=[
	('Yusuf','YAZICI','yusuf@yazici.com'),
	('Arif','SOYLU','arif@soylu.com'),
	('Süleyman','MUTLU','süleyman@mutlu.com')
]

c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)

conn.commit()

conn.close()