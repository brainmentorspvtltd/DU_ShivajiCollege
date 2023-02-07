import bs4
import urllib.request as url

product = input("Enter product : ")
product = product.replace(' ', '+')
path = "https://www.flipkart.com/search?q="+product
response = url.urlopen(path)

page = bs4.BeautifulSoup(response)

titleList = page.find_all('div', {'class' : '_4rR01T'})
priceList = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})
for i in range(len(titleList)):
    print("Title :",titleList[i].text)
    print("Price :",priceList[i].text)
    print("*" * 20)
