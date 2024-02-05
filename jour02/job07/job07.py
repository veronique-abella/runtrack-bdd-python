import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vllmcdpdu.13",
    database="LaPlateforme"
)

cursor = mydb.cursor()
query = "SELECT employe.nom, employe.prenom, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id"
cursor.execute(query)
resultat = cursor.fetchall()

if resultat :
    for employe in resultat :
        print(employe)

class Employe :
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vllmcdpdu.13",
            database = "LaPlateforme"
        )
        self.cursor = self.mydb.cursor()

    def creation_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Employé créé")

    def read_employe(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        resultat = self.cursor.fetchall()
        if resultat:
            for employe in resultat :
                print(employe)
    
    def update_employe(self, nouveau_nom, nouveau_prenom, nouveau_salaire, id):
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s WHERE id = %s"
        values = (nouveau_nom, nouveau_prenom, nouveau_salaire, id)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Donnée employé modifiée")

    def delete_employe(self, id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Employé supprimé")

host = "localhost"
user = "root"
password = "Vllmcdpdu.13"
database = "LaPlateforme"
gerer_employe = Employe(host, user, password, database)
gerer_employe.creation_employe("Duwat", "Victor", 20, 11)
gerer_employe.read_employe()
cursor.close()
mydb.close()
