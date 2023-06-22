#parsing the html inside the webpage to locate the data we need
#done with beautifulsoup #3rd party
import bs4 , requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('<span id="price" class="a-size-medium a-color-price header-price a-text-normal">₹2,429.00</span>')
    return elems[0].text.strip()



price = getAmazonPrice ('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?crid=2Q3WZYXT6CUQ0&keywords=automate+the+boring+stuff+with+python&qid=1687319362&sprefix=automate%2Caps%2C217&sr=8-1')
print ('The price is ' + price)

