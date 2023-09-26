import sqlalchemy as db
from agro_config import config
import urllib.parse


def connection(database=''):
    key = config.config()
    database_password = urllib.parse.quote_plus(key['DB_PASSWORD'])
    engine = db.create_engine(f"mysql+mysqlconnector://{key['DB_usersNAME']}:{database_password}@{key['DB_HOST']}/{database}")

    conn = engine.connect()
    metadata = db.MetaData()  # extracting the metadata
    # _table = db.Table(table, metadata,
    #                   autoload_with=engine)  # Table object
    #
    # print(repr(metadata.tables[table]))
    return engine, metadata