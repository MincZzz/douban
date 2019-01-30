# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

resp = request.urlopen("https://en.wikipedia.org/wiki/Main_Page" , context=context).read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
list = soup.findAll("a", href=re.compile("^/wiki/"))
for i in list:
    if not re.search("\.(jpg|JPG)$",i["href"]):
        print(i.get_text(),"  <---->   ","https://en.wikipedia.org" + i["href"])
