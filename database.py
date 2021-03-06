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
        self.create_PapersTable()
        self.create_AuthorsTable()
        self.create_InstitutionsTable()
        self.metadata.create_all(engine)

    def create_PapersTable(self):
        # create table if it does not exists
        if not self.engine.dialect.has_table(self.engine, 'Papers'):
            # Create a table with the appropriate Columns
            Papers = Table('Papers', self.metadata,
                            Column('Id', Integer(),
                                   primary_key=True, nullable=False),
                            Column('Title', String(255), default=None),
                            Column('Authors_Institutes_id', String(2**15-1), default=None),
                            Column('Published', Boolean(), default=None),
                            Column('Collaborations_id', String(127), default=None),
                            Column('DOI', String(255), default=None),
                            Column('References', Integer(), default=None),
                            Column('References_id', String(2**10-1)),
                            Column('Citations', Integer(), default=None),
                            Column('Citations_id', Integer(), default=None),
                            Column('arXiv', String(255), default=None),
                            Column('reseach_areas', String(127), default=None),
                            Column('Publish_year', Integer(), default=None),
                            Column('Date', String(31), default=None)
                            )


    def create_InstitutionsTable(self):
        # create table if it does not exists
        if not self.engine.dialect.has_table(self.engine, 'Institutions'):
            # Create a table with the appropriate Columns
            Institutions = Table('Institutions', self.metadata,
                            Column('Id', Integer(),
                                   primary_key=True, nullable=False),
                            Column('Name', String(255)),
                            Column('Address', String(512), default=None),
                            Column('Country_id', String(2), default=None),
                            Column('Website', String(255), default=None),
                            Column('Papers_citeable', Integer(), default=None),
                            Column('Papers_published', Integer(), default=None),
                            Column('Citations_citeable', Integer(), default=None),
                            Column('Citations_published', Integer(), default=None),
                            Column('Papers_id', String(2**15-1), default=None),
                            Column('Authors_id', String(2**10-1), default=None)
                            )

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
                            Column('Nationality_id', String(2), default=None),
                            Column('Papers_citeable', Integer(), default=None),
                            Column('Citations_citeable', Integer(), default=None),
                            Column('Papers_published', Integer(), default=None),
                            Column('Citations_published', Integer(), default=None),
                            Column('Citations_L0', Integer(), default=None),
                            Column('Citations_L1', Integer(), default=None),
                            Column('Citations_L2', Integer(), default=None),
                            Column('Citations_L3', Integer(), default=None),
                            Column('Citations_L4', Integer(), default=None),
                            Column('Citations_L5', Integer(), default=None),
                            Column('Citations_L6', Integer(), default=None),
                            Column('Citations_Linf', Integer(), default=None),
                            Column('Experiments', String(255), default=None),
                            Column('PhD_Advisor', String(255), default=None),
                            Column('Papers_id', String(2**14-1), default=None),
                            Column('Email', String(255), default=None),
                            Column('LinkedIn', String(127), default=None),
                            Column('Telegram', String(127), default=None),
                            Column('Phone', String(31), default=None),
                            Column('GoogleScholar', String(127), default=None),
                            Column('Inspirehep',String(127), default=None),
                            Column('Scrape_depth', String(15), default=None),
                            Column('Research_areas', String(127), default=None)
                            )


class DatabaseAccessor:

    def __init__(self, db_path=DB_PATH):
        self.engine = create_engine(DB_PATH)  # create engine
        self.metadata = MetaData()
        self.tables_names = ["Papers", "Authors", "Institutions"]
        self.Papers = Table('Papers', self.metadata,
                             autoload=True, autoload_with=engine)
        self.Authors = Table('Authors', self.metadata,
                             autoload=True, autoload_with=engine)
        self.Institutions = Table('Institutions', self.metadata,
                             autoload=True, autoload_with=engine)
        self.connection = self.engine.connect()

    def insert_Author(self, Id, Name, Research_areas, Experiments):
        stmt = insert(self.Authors).values(Id=Id,
                                           Name=Name,
                                           Research_areas=Research_areas,
                                           Experiments=Experiments)
        results = self.connection.execute(stmt)

    def insert_Paper(self, Id):
        stmt = insert(self.Papers).values(Id=Id)
        result = self.connection.execute(stmt)

    def insert_Institution(self, Id, Name, Address, Website, Country_id, Papers_citeable):
        stmt = insert(self.Institutions).values(Id=Id,
                                                Name=Name,
                                                Address=Address,
                                                Website=Website,
                                                Country_id=Country_id,
                                                Papers_citeable=Papers_citeable)
        result = self.connection.execute(stmt)

    def update_Author(self, Id, column_name, value):
        self.update("Authors", Id, column_name, value)

    def update_Institution(self, Id, column_name, value):
        self.update("Institutions", Id, column_name, value)

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

    def _check_table_existence(self, table_name):
        if not table_name in self.tables_names:
            raise ValueError("No table with name {} in the database".format(table_name))

    def update(self, table_name, Id, column_name, value):
        self._check_table_existence(table_name)
        if type(value) == str:
            stmt = "UPDATE {} SET {} = '{}' WHERE Id = {}".format(table_name, column_name, value, Id)
        else:
            stmt = "UPDATE {} SET {} = {} WHERE Id = {}".format(table_name, column_name, value, Id)
        self.connection.execute(stmt)


    def close(self):
        self.connection.close()
        engine.dispose()


class DatabaseOrganizer():
    def __init__(self, db_path=DB_PATH):
        self.db = DatabaseAccessor(db_path=db_path)

    def add_id_from_Authors_to_Papers(self):
        stmt = "SELECT Papers_id FROM Authors"
        results = self.db.connection.execute(stmt).fetchall()
        for result in results:
            papers_id_list = [int(elem) for elem in result[0].split()]
            for id in papers_id_list:
                try:
                    self.db.insert_Paper(Id=id)
                    print(str(id) + " added to Papers table ...")
                except:
                    print(str(id) + " is already in Papers table ...")


    def organize(self):
        self.add_id_from_Authors_to_Papers()

    def close(self):
        self.db.close()

if __name__ == "__main__":
    os.remove("hep.sqlite")
    creator = DatabaseCreator()
    creator.create_all_tables()
