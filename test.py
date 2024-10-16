from pymongo import MongoClient
import os


client = MongoClient(os.getenv('MONGO_URI'))

db = client["comet-db"]
users = db["users"]


