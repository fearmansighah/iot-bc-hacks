import psycopg2
from math import sin, pi
from datetime import datetime
from time import sleep


def send_sine(t_start, s_id, cursor, conn):

    t = t_start
    while t < 60:  # do 60 inserts
        y = sin(2*pi*0.1*t) + 1  # generating sine at point t
        y = round(y, 2)  # rounding value to 2 dp
        t = t + 1  # step forward in time

        now = datetime.now()  # get current time and date
        # format date and time for timescale inserts
        dt = now.strftime("%Y-%m-%d %H:%M:%S") + "-08"

        cursor.execute("""
                    INSERT INTO sensor_data (time, sensor_id, measurement)
                    VALUES (%s, %s, %s);
                    """, (dt, s_id, y))
        conn.commit()  # makes changes permanent

        sleep(1)  # wait 1 second before doing another insert


def main():
    conn = psycopg2.connect(dbname='bchacks',
                            user='postgres',
                            password='password',
                            host='34.130.148.127',
                            port='5432')

    cursor = conn.cursor()

    send_sine(t_start=0, s_id=1, cursor=cursor, conn=conn)

    cursor.close()  # closes cursor
    conn.close()  # closes connection


if __name__ == "__main__":
    main()
