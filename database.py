import sqlite3

from auth.auth import hash_password, verify_password

DATABASE = "database/styleai.db"


# --------------------------
# Connection
# --------------------------

def get_connection():

    conn = sqlite3.connect(DATABASE)

    return conn


# --------------------------
# Create Tables
# --------------------------

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password BLOB

    )
    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS wardrobe(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        category TEXT,

        color TEXT,

        image_path TEXT,

        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        occasion TEXT,

        weather TEXT,

        recommendation TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()


# --------------------------
# User
# --------------------------

def add_user(name, email, password):

    conn = get_connection()

    cursor = conn.cursor()

    password = hash_password(password)

    try:

        cursor.execute(

            """

            INSERT INTO users(

            name,

            email,

            password

            )

            VALUES(

            ?,?,?

            )

            """,

            (

                name,

                email,

                password

            )

        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# --------------------------
# Login
# --------------------------

def login_user(email, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE email=?",

        (email,)

    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return None

    if verify_password(

        password,

        user[3]

    ):

        return user

    return None


# --------------------------
# Wardrobe
# --------------------------

def add_clothing(

    user_id,

    category,

    color,

    image_path

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO wardrobe(

        user_id,

        category,

        color,

        image_path

        )

        VALUES(

        ?,?,?,?

        )

        """,

        (

            user_id,

            category,

            color,

            image_path

        )

    )

    conn.commit()

    conn.close()


def get_wardrobe(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT *

        FROM wardrobe

        WHERE user_id=?

        """,

        (

            user_id,

        )

    )

    clothes = cursor.fetchall()

    conn.close()

    return clothes


def delete_clothing(item_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM wardrobe

        WHERE id=?

        """,

        (

            item_id,

        )

    )

    conn.commit()

    conn.close()


# --------------------------
# History
# --------------------------

def save_history(

    user_id,

    occasion,

    weather,

    recommendation

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO history(

        user_id,

        occasion,

        weather,

        recommendation

        )

        VALUES(

        ?,?,?,?

        )

        """,

        (

            user_id,

            occasion,

            weather,

            recommendation

        )

    )

    conn.commit()

    conn.close()


def get_history(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT *

        FROM history

        WHERE user_id=?

        """,

        (

            user_id,

        )

    )

    history = cursor.fetchall()

    conn.close()

    return history


# --------------------------
# Initialize Database
# --------------------------

create_tables()
