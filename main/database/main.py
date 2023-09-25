#TODO: database connection, import config file
import pymongo
import json
database = {
  "name":"SIAAI",
  "collection":"request",
  "client":"mongodb://localhost:27017/"
}

myclient = pymongo.MongoClient(database["client"])

mydb = myclient[database["name"]]

dblist = myclient.list_database_names()
if database["name"] in dblist:
  print("The database exists.")

mycol = mydb[database["collection"]]

collist = mydb.list_collection_names()
if database["collection"] in collist:
  print("The collection exists.")

def insertin(mydict):
  mydict.dumps(mydict)
  x = mycol.insert_one(mydict)
  print("succesfully inserted in database id =" + x.inserted_id)