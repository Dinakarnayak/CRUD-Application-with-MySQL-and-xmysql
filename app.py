import asyncio
from db import create_connection_pool
from models import create_record, read_records, update_record, delete_record

async def main():
    pool = await create_connection_pool()

    # Create records
    await create_record(pool, "Alice", 30)
    await create_record(pool, "Bob", 25)

    # Read all records
    records = await read_records(pool)
    print("All records:", records)

    # Update a record
    await update_record(pool, 1, "Alice Smith", 31)

    # Delete a record
    await delete_record(pool, 2)

    # Read again to confirm changes
    records = await read_records(pool)
    print("All records after changes:", records)

if __name__ == "__main__":
    asyncio.run(main())
