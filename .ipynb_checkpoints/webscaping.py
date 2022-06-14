import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com/"

# get the html
r=requests.get(url)   # brings plain content
htmlcontent=r.content
# print(htmlcontent)


# parse the html
soup=BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)



# html tree traversal
title=soup.title
print(title)