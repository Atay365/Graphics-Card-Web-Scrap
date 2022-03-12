from cgitb import text
from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)


