import psycopg2
import contextlib
import enum

from data import config


class Status(enum.Enum):
    OK = 1
    ERROR = 2


@contextlib.contextmanager
def database(url=None):
    """
    It creates a database connection, creates a cursor, and then yields the cursor and the connection to the caller
    """
    url = config.URL if url is None else url
    conn = psycopg2.connect(url)
    # conn = psycopg2.connect(
    #     host=config.HOST,
    #     dbname=config.DATABASE,
    #     user=config.USER,
    #     password=config.PASSWORD,
    #     port=config.PORT
    # )
    cur = conn.cursor()
    status = Status.OK
    try:
        yield cur, conn, status
    except Exception as err:
        print(err)
        status = Status.ERROR
    finally:
        cur.close()
        conn.close()
