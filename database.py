# create databases
# import packages
from global_vars import *
import os
import pandas as pd
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
        self.engine = create_engine(DB_PATH)  # create engine
        self.metadata = MetaData()

    def create_all_tables(self):
        self.create_AuthorsTable()
        self.metadata.create_all(engine)

    def create_AuthorsTable(self):
        # create table if it does not exists
        if not self.engine.dialect.has_table(self.engine, 'Authors'):
            # Create a table with the appropriate Columns
            Authors = Table('Authors', self.metadata,
                            Column('Id', Integer(),
                                   primary_key=True, nullable=False),
                            Column('Name', String(255)),
                            Column('BS_id', Integer(), default=None),
                            Column('BS_year', Integer(), default=None),
                            Column('MS_id', Integer(), default=None),
                            Column('MS_year', Integer(), default=None),
                            Column('PhD_id', Integer(), default=None),
                            Column('PhD_year', Integer(), default=None),
                            Column('PD1_id', Integer(), default=None),
                            Column('PD1_year', Integer(), default=None),
                            Column('PD2_id', Integer(), default=None),
                            Column('PD2_year', Integer(), default=None),
                            Column('PD3_id', Integer(), default=None),
                            Column('PD3_year', Integer(), default=None),
                            Column('PD4_id', Integer(), default=None),
                            Column('PD4_year', Integer(), default=None),
                            Column('Senior1_id', Integer(), default=None),
                            Column('Senior1_year', Integer(), default=None),
                            Column('Senior2_id', Integer(), default=None),
                            Column('Senior2_year', Integer(), default=None),
                            Column('Senior3_id', Integer(), default=None),
                            Column('Senior3_year', Integer(), default=None),
                            Column('Senior4_id', Integer(), default=None),
                            Column('Senior4_year', Integer(), default=None),
                            Column('Nationality_id', String(2), default=None)
                            )


class DatabaseAccessor:

    def __init__(self, db_path=DB_PATH):
        self.engine = create_engine(DB_PATH)  # create engine
        self.metadata = MetaData()
        self.Authors = Table('Authors', self.metadata,
                             autoload=True, autoload_with=engine)
        self.connection = self.engine.connect()

    def insert_Author(self, Id, Name,
                      BS_id=None, BS_year=None,
                      MS_id=None, MS_year=None,
                      PhD_id=None, PhD_year=None,
                      PD1_id=None, PD1_year=None,
                      PD2_id=None, PD2_year=None,
                      PD3_id=None, PD3_year=None,
                      PD4_id=None, PD4_year=None,
                      Senior1_id=None, Senior1_year=None,
                      Senior2_id=None, Senior2_year=None,
                      Senior3_id=None, Senior3_year=None,
                      Senior4_id=None, Senior4_year=None,
                      Nationality_id=None):
        stmt = insert(self.Authors).values(Id=Id, Name=Name,
                                           BS_id=BS_id,
                                           BS_year=BS_year,
                                           MS_id=MS_id,
                                           MS_year=MS_year,
                                           PhD_id=PhD_id,
                                           PhD_year=PhD_year,
                                           PD1_id=PD1_id,
                                           PD1_year=PD1_year,
                                           PD2_id=PD2_id,
                                           PD2_year=PD2_year,
                                           PD3_id=PD3_id,
                                           PD3_year=PD3_year,
                                           PD4_id=PD4_id,
                                           PD4_year=PD4_year,
                                           Senior1_id=Senior1_id,
                                           Senior1_year=Senior1_year,
                                           Senior2_id=Senior2_id,
                                           Senior2_year=Senior2_year,
                                           Senior3_id=Senior3_id,
                                           Senior3_year=Senior3_year,
                                           Senior4_id=Senior4_id,
                                           Senior4_year=Senior4_year,
                                           Nationality_id=Nationality_id)
        results = self.connection.execute(stmt)
        print(results.rowcount)

    def export_table_to_csv(self, table_name, path=WORKING_PATH):
        """exports a table with given name to csv file"""
        stmt = "SELECT * FROM {}".format(table_name)
        results = pd.read_sql_query(stmt,self.engine)
        results.to_csv(path+table_name+".csv",index=False,sep=",")

    def to_csv(self, path=WORKING_PATH):
        """exports all tables in database to csv files
        with name of each csv file to be same as the name of table"""
        for table in self.metadata.tables.values():
            self.export_table_to_csv(table.name, path=path)

    def update(self, table_name, Id, column_name, value):
        if type(value) == str:
            stmt = "UPDATE {} SET {} = '{}' WHERE Id = {}".format(table_name, column_name, value, Id)
        else:
            stmt = "UPDATE {} SET {} = {} WHERE Id = {}".format(table_name, column_name, value, Id)
        self.connection.execute(stmt)


    def close(self):
        self.connection.close()
        engine.dispose()


if __name__ == "__main__":
    os.remove("hep.sqlite")
    creator = DatabaseCreator()
    creator.create_all_tables()
