# add nationality of authors
# these informations are collected by survey
# and need to be added manually

from global_vars import *
from database import *

# create a databased accessor object
db = DatabaseAccessor()

def set_IR(id):
    "updates Nationality_id of an author to IR"
    db.update("Authors", id, "Nationality_id", "IR")

set_IR(1021261) # Hassan Firouzjahi

# export to csv
db.to_csv()
