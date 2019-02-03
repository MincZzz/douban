import pymysql.cursors

conn = pymysql.connect(host="localhost",
                       user="root",
                       password="a9702310451b",
                       db="db_wiki",
                       charset="utf8mb4")

try:
    with conn.cursor() as cursor:
        sql = "select `urlname`,`urlhref` from `urls`"
        count = cursor.execute(sql)
        print(count)

        result1 = cursor.fetchone()
        print(result1)
        result2 = cursor.fetchone()
        print(result2)
        result3 = cursor.fetchmany(size=2)
        print(result3)
        result4 = cursor.fetchall()
        print(result4)

        conn.commit()
finally:
    conn.close()
