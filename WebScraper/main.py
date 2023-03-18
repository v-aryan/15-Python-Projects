# this project is to be done on cmd where first you will pip install requests and bs4
# Then enter into python >>>
# write the below code:

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com"
r = requests.get(url)
r

# when you write r and press enter you will get message Response 200

soup = BeautifulSoup(r.content,'lxml')
title = soup.find_all('h1',{'class':'post-title'})
title

# after clicking on title you will get all the h1 things present on the website

# if you want any one heading then
title[0].getText()

# and if you want to get all the heading at a time then we can use for loop
#  for t in title:
#      print(t.getText())
