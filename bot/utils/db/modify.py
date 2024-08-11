import pandas as pd

from .connect import database


def add_answer(_id, answer_text, admin_id):
    with database() as (cur, conn, status):
        sql = "UPDATE cpm_data.questions SET answer_text = %s, admin_id = %s WHERE id = %s"
        cur.execute(sql, [answer_text, admin_id, _id])
    conn.commit()
    return status
