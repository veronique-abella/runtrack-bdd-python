import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vllmcdpdu.13",
    database="LaPlateforme"
)

cursor = mydb.cursor()

query = "SELECT * FROM etudiant"
cursor.execute(query)

etudiant = cursor.fetchall()

for etudiants in etudiant:
    print(etudiants) 

cursor.close()
mydb.close()