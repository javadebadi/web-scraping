# create databases
# import packages
from global_vars import *
import os
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import select, insert
from sqlalchemy import String, Integer, Boolean, Float, Date
from sqlalchemy_utils import create_database, database_exists

# create engine
engine = create_engine(DB_PATH)

# create databse if it does not exist
if not database_exists(engine.url):
    create_database(engine.url)

class DatabaseCreator:

    def __init__(self, db_path=DB_PATH):
        self.engine = create_engine(DB_PATH)  # create engien
        self.metadata = MetaData()

    def create_all_tables(self):
        self.create_AuthorsTable()
        self.metadata.create_all(engine)

    def create_AuthorsTable(self):
        # create table if it does not exists
        if not self.engine.dialect.has_table(self.engine, 'Authors'):
            # Create a table with the appropriate Columns
            Authors = Table('Authors', self.metadata,
                Column('Id', Integer(), primary_key=True, nullable=False),
                Column('Name', String(255))
                )


class DatabaseAccessor:

    def __init__(self, db_path=DB_PATH):
        self.engine = create_engine(DB_PATH)  # create engine
        self.metadata = MetaData()
        self.Authors = Table('Authors', self.metadata, autoload=True, autoload_with=engine)
        self.connection = self.engine.connect()

    def insert_Author(self, Id, Name):
        stmt = insert(self.Authors).values(Id=Id, Name=Name)
        results = self.connection.execute(stmt)
        print(results.rowcount)

    def close(self):
        self.connection.close()
        engine.dispose()

if __name__ == "__main__":
    os.remove("hep.sqlite")
    creator = DatabaseCreator()
    creator.create_all_tables()
