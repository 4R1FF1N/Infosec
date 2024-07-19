import requests 
from bs4 import BeautifulSoup

headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

HTML = requests.get("https://www.google.com/search?q=tesla+stock+price", headers=headers)
soup = BeautifulSoup(HTML.text, "lxml")
text = soup.find("div", attrs={"class": "PZPZlf ssJ7i B5dxMb"}).text + " | " + soup.find("span", attrs={"jsname": "vWLAgc"}).text + soup.find("span", attrs={"jsname": "T3Us2d"}).text
print(text)
