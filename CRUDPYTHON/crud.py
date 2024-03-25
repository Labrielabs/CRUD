import mysql.connector

connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MariaDB",
    database = "crud_python"
    )


def create_user(nom, email):
    cursor = connexion.cursor()
    cursor.execute("""
                   INSERT INTO utilisateurs (nom, email) VALUES(%s, %s);
                """, (nom, email))
    connexion.commit()
    print("Utilisateur crée")



def read_users():
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM utilisateurs;")
    for (id , nom, email) in cursor:
        print(f"ID: {id}, Nom :{nom}, Email:{email}")
    


def update_user(id, email):  
    cursor = connexion.cursor()
    cursor.execute("""
        UPDATE utilisateurs
        SET email = %s
        WHERE id = %s
    """,  (email, id))
    connexion.commit()

def delete_user(id):
    cursor = connexion.cursor()
    cursor.execute("""
        DELETE FROM utilisateurs
        WHERE id = %s
    """, (id,))
    connexion.commit()
   
#create_user("John Doe", "johndoe@example.com")
#read_users
#update_user(2, "emicheldev@gmail.com")
#delete_user(2)