from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

import configurations as config

uri = f"mongodb+srv://{config.user_name}:{config.password}@cluster0.z7ht9nr.mongodb.net/"
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
