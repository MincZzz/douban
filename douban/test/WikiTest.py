# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import ssl
import pymysql.cursors

# This restores the same behavior as before.
context = ssl._create_unverified_context()

resp = request.urlopen("https://en.wikipedia.org/wiki/Main_Page", context=context).read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
list = soup.findAll("a", href=re.compile("^/wiki/"))
for i in list:
    if not re.search("\.(jpg|JPG)$", i["href"]):
        print(i.get_text(), "  <---->   ", "https://en.wikipedia.org" + i["href"])

        conn = pymysql.connect(host="localhost",
                               user="root",
                               password="a9702310451b",
                               db="db_wiki",
                               charset="utf8mb4")

        try:
            with conn.cursor() as cursor:
                sql = "insert into `urls` (`urlname`,`urlhref`) values (%s,%s)"
                cursor.execute(sql, (i.get_text(), "https://en.wikipedia.org" + i["href"]))
                conn.commit()
        finally:
            conn.close()
