from .connect import database

import pandas as pd
import datetime


def get_events():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    with database() as (cur, conn, status):
        sql = "SELECT id, name, description, min_grade, max_grade, reg_url FROM cpm_data.events WHERE end_date > %s"
        cur.execute(sql, [current_date])
        result = cur.fetchall()
        data = pd.DataFrame(result, columns=['id', 'name', 'description', 'min_grade', 'max_grade', 'reg_url'])
    return data


def get_event(event_id):
    with database() as (cur, conn, status):
        sql = "SELECT name, description, min_grade, max_grade, reg_url FROM cpm_data.events WHERE id = %s"
        cur.execute(sql, [event_id])
        result = cur.fetchone()
        data = pd.Series(result, index=['name', 'description', 'min_grade', 'max_grade', 'reg_url'])
    return data