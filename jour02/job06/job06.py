import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vllmcdpdu.13",
    database="LaPlateforme"
)

cursor = mydb.cursor()

query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
cursor.execute(query)

result = cursor.fetchone()

superficie_totale = result[0]
print("La capacité de toutes les salles est de :", superficie_totale)

cursor.close()
mydb.close()
