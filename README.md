
# CRUD Application with xmysql

This repository contains a simple Python-based CRUD (Create, Read, Update, Delete) application using `xmysql` for MySQL database interactions. The application demonstrates how to perform asynchronous database operations with Python, using the `xmysql` library.

## Features

- Create, read, update, and delete records in a MySQL database.
- Asynchronous operations to enhance performance and scalability.
- Built using Python 3.x and `xmysql` library for MySQL handling.

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.6 or higher**
- **MySQL Server**
- **Required Python libraries** (listed in `requirements.txt`)

### Install Python and MySQL:

1. **Python**: 
   - Download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Ensure that `pip` is also installed (it should come with Python).

2. **MySQL**:
   - Download and install MySQL from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/).
   - After installing MySQL, ensure the MySQL service is running and that you can access the MySQL CLI or Workbench.

## Installation Steps

### Step 1: Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/crud-app.git
cd crud-app
```

### Step 2: Install Dependencies

Install the required Python dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install the following libraries:
- `xmysql`: A Python library for asynchronous MySQL operations.
- `aiohttp`: For asynchronous HTTP requests (optional, for future API integration).

### Step 3: Set Up MySQL Database

1. **Log in to MySQL**:

   Open your MySQL terminal or MySQL Workbench and log in using your MySQL credentials:

   ```bash
   mysql -u root -p
   ```

   Enter your MySQL password when prompted.

2. **Create the Database**:

   Create a new database named `crud_db`:

   ```sql
   CREATE DATABASE crud_db;
   USE crud_db;
   ```

3. **Create the Users Table**:

   Create a `users` table to store user data:

   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       age INT
   );
   ```

### Step 4: Update Database Connection Details

In `db.py`, ensure the database connection details match your MySQL setup. Here’s how the `db.py` file should look:

```python
# db.py

import asyncio
from xmysql import XMySQL

# Function to create a connection pool to MySQL
async def create_connection_pool():
    return await XMySQL.connect(
        host="localhost",       # MySQL host
        port=3306,              # MySQL port (default 3306)
        user="root",            # MySQL username (default 'root')
        password="password",    # MySQL password (change this)
        database="crud_db"      # MySQL database name
    )
```

Make sure to replace `"password"` with your actual MySQL password.

## Running the Application

Once you have cloned the repository and set up the database, you can run the application.

### Step 1: Run the Application

Execute the following command to run the application:

```bash
python app.py
```

The app will:
1. Insert two sample records (`Alice`, `Bob`) into the `users` table.
2. Retrieve all records from the table and display them.
3. Update the `name` and `age` of the first record.
4. Delete the second record.
5. Print the updated records after all changes.

### Example Output:

```bash
Record created: Alice, 30
Record created: Bob, 25
All records: [(1, 'Alice', 30), (2, 'Bob', 25)]
Record updated: Alice Smith, 31
Record deleted: Bob
All records after changes: [(1, 'Alice Smith', 31)]
```

## Project Structure

Here's a look at the structure of the project:

```
crud-app/
│
├── app.py               # Main application file
├── db.py                # Database connection setup
├── models.py            # Database models and CRUD logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

- **app.py**: The main file containing the logic to execute the CRUD operations.
- **db.py**: Manages the connection to MySQL and the connection pool.
- **models.py**: Contains functions for creating, reading, updating, and deleting records in the database.
- **requirements.txt**: Lists the required Python libraries for the application.

## Video Tutorial

For a step-by-step guide on how to set up and run this project, check out the video tutorial linked below:

[Watch the Tutorial Video](https://drive.google.com/file/d/1FswXvDmT_AbS-5m8lQ4Ir2CubxVRKUDs/view?usp=drive_link)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [xmysql](https://github.com/o1lab/xmysql) for the awesome database library.
- Inspired by open-source projects in the Python ecosystem.

---

This `README.md` provides a comprehensive guide for setting up the repository, configuring the database, running the application, and contributing. It also includes the project structure for better understanding, and a tutorial video to make the process easier.
``` 

This format includes the project structure and the video tutorial link. Let me know if you need any more adjustments!
