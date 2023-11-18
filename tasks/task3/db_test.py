import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

import configurations as config


async def ping_server():
    uri = f"mongodb+srv://{config.user_name}:{config.password}@cluster0.z7ht9nr.mongodb.net/"

    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    # Replace the placeholder with your Atlas connection string

    # without stable version
    # client = AsyncIOMotorClient(uri)

    # Send a ping to confirm a successful connection
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    asyncio.run(ping_server())
