import requests
from bs4 import BeautifulSoup


url="https://www.codewithharry.com"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())
title = soup.title
# print(type(title))
# print(type(soup))
# print(title.string)

# to get all the paras present on website
paras = soup.find_all('p')

# to get all the anchor tags present on website
anchors = soup.find_all('a')

# to get the first paragraph content from the website
#print(soup.find('p'))

# to get the first paragraphs class names
#print(soup.find('p')['class'])

# to find all the elements with class mt-2
#print(soup.find_all("p",class_="mt-2"))

# to get text from tags/soup
#print(soup.find('p').get_text())

# to get all the links present in anchor tags are:
# anchor = soup.find_all('a')
# all_links = set()
# for link in anchor:
#      print(link.get('href'))


# IT will give all the links present on the website with clean display
# anchor = soup.find_all('a')
# all_links = set()
# for link in anchor:
#     if(link.get('href') != '#'):
#         linkText = "https://www.codewithharry.com" +link.get('href')
#         all_links.add(link)
#         print(linkText)


# comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

#finding
# find = soup.find({'class','hidden'})
# for elem in find.strings:
#     print(elem)

# print(elem.parent)


# print(soup.find('p')['class'])
#
# find = soup.find({'class','text-sm'})
# for t in find.strings:
#     print(t)

# print(t.parents)

print('text-sm'.previous_sibling.previous_sibling.previous_sibling)

elem = soup.select('.loginModal')
print(elem)