import os
from typing import Optional

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database


load_dotenv()

_MONGO_URI = os.getenv("MONGODB_URI", "mongodb+srv://vanshika1310sharma_db_user:myetcFSTQzOzBLmq@cluster0.4r2c82p.mongodb.net/trendevo")
_DB_NAME = _MONGO_URI.rsplit("/", 1)[-1] or "trendevo"

_client: Optional[MongoClient] = None


def get_mongo_client() -> MongoClient:
    """
    Return a singleton MongoClient for the agent.
    Reuses the same trendevo database as the Flask app.
    """
    global _client
    if _client is None:
        _client = MongoClient(_MONGO_URI)
    return _client


def get_db() -> Database:
    """
    Convenience accessor for the trendevo database.
    """
    client = get_mongo_client()
    return client[_DB_NAME]
