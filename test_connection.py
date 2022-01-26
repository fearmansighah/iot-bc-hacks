import psycopg2


def testConnection(cursor):
    # use the cursor to interact with your database
    cursor.execute("SELECT 'hello world'")
    print(cursor.fetchone())


def main():
    conn = psycopg2.connect(dbname='bchacks',
                            user='postgres',
                            password='password',
                            host='34.130.148.127',
                            port='5432')

    cursor = conn.cursor()

    testConnection(cursor)

    cursor.close()  # closes cursor
    conn.close()  # closes connection


if __name__ == "__main__":
    main()
