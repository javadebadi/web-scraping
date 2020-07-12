import os
#os.system("python database.py")
os.system("python Author.py")

from global_vars import *
from database import *
from Author import *

def create_database():
    # create databases
    creator = DatabaseCreator()
    creator.create_all_tables()

def process_database():
    # organize database and process
    dbo = DatabaseOrganizer()
    dbo.organize()
    dbo.close()

def create_csv():
    db = DatabaseAccessor()
    db.to_csv()
    db.close()

def main():
    create_database()
    os.system("python db_nationality.py") # add natinality for authors we know
    process_database() # organize database and process
    create_csv()  #  create csv data of database


if __name__ == "__main__":
    main()
