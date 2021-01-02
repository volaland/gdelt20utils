"""
Database connection helpers
"""
import psycopg2
import psycopg2.extras

def get_db_connection(config):
    """
    Return database connection

    @param config: config object
    @return: data base connection object
    """
    conn = psycopg2.connect(
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        dbname=config["DB_NAME"],
        host=config["DB_HOST"],
        port=config["DB_PORT"]
    )

    conn.set_session(readonly=True, autocommit=False)

    return conn


def get_db_cursor(conn):
    """
    Return database cursor

    @param conn: db connection object
    @return: cursor object
    """
    return conn.cursor()


def get_db_dict_cursor(conn):
    """
    Return database cursor with Dict factory

    @param conn: db connection object
    @return: cursor object
    """
    return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
