import mysql.connector

class Directeur:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def create_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def read_cage(self):
        query = "SELECT * FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result :
            for cage in result:
                print(cage)

    def update_cage(self, id, nouvelle_capacite):
        query = "UPDATE cage SET capacite_max = %s WHERE id = %s"
        values = (nouvelle_capacite, id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_cage(self, id):
        query = "DELETE FROM cage WHERE id_cage = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def create_animal(self, nom, race, id_cage, date_naissance, origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, origine)
        self.cursor.execute(query, values)
        self.mydb.commit()
    
    def read_animal(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        resultat = self.cursor.fetchall()
        if resultat:
            for animal in resultat :
                print(animal)

    def update_animal(self, animal_id, nouveau_id_cage):
        query = "UPDATE animal SET id_cage = %s WHERE id = %s"
        values = (nouveau_id_cage, animal_id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result :
            for superficie in result:
                print("La superficie totale des cages est de :",superficie)

    def animal_cage(self):
        query = " SELECT animal.nom, animal.race, cage.id AS cage FROM animal JOIN cage ON cage.id = animal.id_cage "
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            for animaux in result:
                print(animaux)

    def close_connection(self):
        self.cursor.close()

host="localhost"
user='root'
password='Vllmcdpdu.13'
database='Zoo'
mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
gerer_zoo = Directeur(host, user, password, database)
gerer_zoo.read_animal()

gerer_cage = Directeur(host, user, password, database)
gerer_cage.read_cage()
gerer_zoo.animal_cage()
