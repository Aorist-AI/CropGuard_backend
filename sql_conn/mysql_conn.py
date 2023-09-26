import mysql.connector
from agro_config.config import config


def create(database="tamu"):
    dbconfig = config()
    conn = mysql.connector.connect(user=dbconfig["user"], password=dbconfig["password"],
                                   host=dbconfig["host"], database=database, autocommit=True)
    return conn