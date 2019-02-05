from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

resp = urlopen("https://en.wikipedia.org/robots.txt", context=context).read().decode("utf-8")

print(resp)

