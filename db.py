import asyncio
from xmysql import XMySQL

# Function to create connection pool
async def create_connection_pool():
    return await XMySQL.connect(
        host="localhost",  # MySQL host
        port=3306,         # MySQL port
        user="root",       # MySQL username
        password="password",  # MySQL password
        database="crud_db"  # Your database name
    )
