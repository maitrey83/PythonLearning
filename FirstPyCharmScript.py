import requests
import bs4
from os import urandom

print ("Hello")

url = "http://www.google.com"
response = requests.get(url).status_code
print (response)
if response != 200:
        print (url)

header = requests.get(url).headers
print(header)



