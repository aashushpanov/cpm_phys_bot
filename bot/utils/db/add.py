import pandas as pd

from .connect import database


def add_question(user_id, user_message_id, bot_message_id, question_text, timestamp):
    with database() as (cur, conn, status):
        sql = "INSERT INTO cpm_data.questions (user_id, user_message_id, bot_message_id, question_text, date) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, [user_id, user_message_id, bot_message_id, question_text, timestamp])
        conn.commit()
    return status
