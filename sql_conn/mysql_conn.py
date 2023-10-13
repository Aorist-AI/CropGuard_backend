from mysql import connector
from agro_config.config import config


def create(database="tamu"):
    dbconfig = config()
    conn = connector.connect(users=dbconfig["users"], password=dbconfig["password"],
                                   host=dbconfig["host"], database=database, autocommit=True)
    return conn