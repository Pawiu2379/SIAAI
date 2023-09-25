#TODO: database connection, import config file

import pymongo
import sys
import os

# Get the parent directory of the current script (myscript.py)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory (/main/) to the Python path
sys.path.append(parent_dir)
from .. import config
database =config.database

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient[database.name]

dblist = myclient.list_database_names()
if "SIAAI" in dblist:
  print("The database exists.")

mycol = mydb[database.collections.request]

collist = mydb.list_collection_names()
if "request" in collist:
  print("The collection exists.")