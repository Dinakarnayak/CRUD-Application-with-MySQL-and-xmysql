# models.py

# Create function
async def create_record(pool, name, age):
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    await pool.execute(query, (name, age))
    print("Record created successfully.")

# Read function
async def read_records(pool):
    query = "SELECT * FROM users"
    result = await pool.fetch(query)
    return result

# Update function
async def update_record(pool, user_id, name, age):
    query = "UPDATE users SET name = %s, age = %s WHERE id = %s"
    await pool.execute(query, (name, age, user_id))
    print("Record updated successfully.")

# Delete function
async def delete_record(pool, user_id):
    query = "DELETE FROM users WHERE id = %s"
    await pool.execute(query, (user_id,))
    print("Record deleted successfully.")
