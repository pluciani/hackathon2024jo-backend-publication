import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_connection():
    config = {
        'user': '360826_team12',
        'password': 'Ipssi12**',
        'host': 'mysql-hackathonmia12.alwaysdata.net',
        'database': 'hackathonmia12_olympicgames2024'
    }
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            logger.info('Connexion réussie à la base de données')
        return conn
    except Error as e:
        logger.error(f"Error: {e}")
        return None