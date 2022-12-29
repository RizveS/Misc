import requests
import bs4
from datetime import datetime

#Get HTML string
try:
    html_string = requests.get("https://www.google.com/finance/quote/SBS:NYSE")
except:
    print("Was not able to get the data")


#Get BeautifulSoup to parse HTML for quick indexing
parser = bs4.BeautifulSoup(html_string.content,"html.parser")
#Index based on class
price_data = parser.find_all("div",class_="YMlKec fxKbKc")
print(datetime.now(), price_data[0].get_text())
data_to_write = str(datetime.now()) + " " + price_data[0].get_text() + "\n"
with open("SBS_DATA.txt","a") as file:
    file.write(data_to_write)

    