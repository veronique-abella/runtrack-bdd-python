import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vllmcdpdu.13",
    database="LaPlateforme"
)

cursor = mydb.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

for salle in cursor.fetchall():
    print(salle)

cursor.close()
mydb.close()
