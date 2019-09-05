from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url="https://www.imdb.com/"
uClient=uReq(my_url)
html_page=uClient.read()
uClient.close()
page_soup=soup(html_page,'html.parser')
contain=page_soup.find_all("div",{"class":"trending-list-rank-item"})
for i in contain:
    title=i.find("span",{"class":"trending-list-rank-item-name"})
    print(title.a.text)
