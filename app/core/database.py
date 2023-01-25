from typing import AsyncIterator
from urllib.parse import urlencode

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pydantic import MongoDsn

from app.core.log import logger


class MongoSrvDsn(MongoDsn):
    allowed_schemes = {"mongo", "mongodb+srv"}


def get_mongo_database(
    scheme: str, host: str, db_name: str, username: str, password: str, rs_name: str = None
) -> AsyncIterator[AsyncIOMotorDatabase]:
    """Create database connection."""

    logger.info(f"MongoDB[{db_name}] Initiation")

    query_dict = {}
    if scheme == "mongodb+srv":
        if rs_name:
            query_dict["replicaSet"] = rs_name
        query_dict["retryWrites"] = "true"
        query_dict["w"] = "majority"

    query = urlencode(query_dict)

    url = MongoSrvDsn(
        url=None,
        scheme=scheme,
        user=username,
        password=password,
        host=host,
        query=query,
    )
    logger.info(f"Mongo URI: {url}")

    motor_conf = {"serverSelectionTimeoutMS": 10000}
    mdb_client = AsyncIOMotorClient(url, **motor_conf)

    yield mdb_client[db_name]

    mdb_client.close()
    logger.info("MongoDB Closed")
