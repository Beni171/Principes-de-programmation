import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def get_connection():
    """Crée et retourne une nouvelle connexion mysql, leve une exception si la connexion échoue.
    """
    
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Erreur connexion Mysql : {e}")
        raise
    
get_connection()