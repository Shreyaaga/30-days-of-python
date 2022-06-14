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

# get the title of the html page 
title=soup.title
print(title)
# to print all paragraph tags
paras=soup.find_all('p')
print(paras)
# to get classes of first paragraph
para=soup.find('p')['class']
print(para)
# find all the elements with class lead
print(soup.find_all("p",class_='text-sm'))
# get the text from the tage
print(soup.find('p').get_text())
# get al anchor tags and links within it
anchor=soup.find_all('a')
for link in anchor:
     print(link.get('href')) #.get is used to grab teh particular attribute
#childer
ul = soup.find("ul")
for i in ul.children:
	print(i)

#previous child
ul = soup.find(id="li")
print(ul.next_sibling.next_sibling)
