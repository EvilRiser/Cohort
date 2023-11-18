from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

import configurations as config

uri = f"mongodb+srv://{config.user_name}:{config.password}@cluster0.z7ht9nr.mongodb.net/"
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

students_db = client.students
# students_db = client["students"]

students_data = students_db.student_collection
# collection_data = students_db["student_collection"]

if __name__ == '__main__':
    import asyncio

    async def ping_server():
        """
        test db connection
        :return:
        """
        try:
            await client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

        except Exception as e:
            print(e)

    asyncio.run(ping_server())
