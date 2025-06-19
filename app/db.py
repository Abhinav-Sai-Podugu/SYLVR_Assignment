from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

def connect_to_mongo():
    try:
        client = MongoClient(MONGO_URI)
        db = client["sample_analytics"]
        print("MongoDB connection successful")
        return db
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("MongoDB connection failed:", e)
        return None


def load_collections(db):
    return db.list_collection_names() if db else []
