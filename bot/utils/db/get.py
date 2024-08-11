import pandas as pd
import datetime

from .connect import database


def get_events():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    with database() as (cur, conn, status):
        sql = "SELECT id, name, description, min_grade, max_grade, reg_url FROM cpm_data.events WHERE end_date > %s ORDER BY max_grade, min_grade, is_primary DESC"
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


def get_question(bot_message_id):
    with database() as (cur, conn, status):
        sql = "SELECT id, user_message_id, question_text, user_id, date FROM cpm_data.questions WHERE bot_message_id = %s"
        cur.execute(sql, [bot_message_id])
        result = cur.fetchone()
        data = pd.Series(result, index = ["id", "user_message_id", "question_text", "user_id", "date"])
    return data
