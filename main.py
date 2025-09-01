import databases
import sqlalchemy

DATABASE_URL = "mysql+aiomysql://<username>:<password>@<host>/<database_name>"
database = databases.Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()
    query = "CREATE DATABASE IF NOT EXISTS <database_name>;"
    await database.execute(query)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()