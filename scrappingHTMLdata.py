#Sample data: http://py4e-data.dr-chuck.net/comments_42.html
#actual data: http://py4e-data.dr-chuck.net/comments_649378.html


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

numlist =list()
for tag in tags:

    str = tag.decode()

    list = re.findall('[0-9]+',str)
    for num in list:
        numlist.append(num)

sum = 0
for num in numlist:
    x = int(num)
    sum = sum + x

print('Sum=',sum)
