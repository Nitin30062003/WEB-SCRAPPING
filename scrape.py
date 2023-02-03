import csv
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

urls=["https://www.snapdeal.com/search?keyword=bags&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=travel%20bag&santizedKeyword=bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=hiking%20bags&santizedKeyword=hiking+bag&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=waist%20bag&santizedKeyword=hiking+bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=laptop%20carry%20bag&santizedKeyword=laptop+bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=side%20bags&santizedKeyword=trolley+bags&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=kids%20bags&santizedKeyword=side+bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=ladies%20bags&santizedKeyword=kids+bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=sports%20gym%20bags&santizedKeyword=sport+bag&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=cover%20bags&santizedKeyword=sports+gym+bags&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=baggit%20sling%20bag&santizedKeyword=cover+bags&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy",
     "https://www.snapdeal.com/search?keyword=cotton%20bags&santizedKeyword=hand+bags&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"]




with open('scrape2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Product name", "Price", "Rating", "No. of ratings","No. of reviews", "Product id", "Seller details", "Product URL"])
    for url in urls:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        product_list = soup.find_all("div", {"class": "product-tuple-description"})

        for product in product_list:
            product_name = product.find("p", {"class": "product-title"}).text
            product_price = product.find("span", {"class": "product-price"}).text
            product_url = product.find("a")["href"]


            num_rating = product.find("p", {"class": "product-rating-count"})
            if num_rating:
                num_ratings=num_rating.text.replace('(','').replace(')','')
            else:
                num_ratings="N/A"

            resp=requests.get(product_url,headers=headers)
            soup2=BeautifulSoup(resp.text,"html.parser")

            rating=soup2.find('span',{'class':'avrg-rating'})
            if rating:
                product_rating = rating.text.replace('(','').replace(')','')
            else:
                product_rating = "N/A"

            pid=soup2.find('li',{'id':'highlightSupc'})
            if pid:
                product_id=pid.text.replace('SUPC:','').strip()
            else:
                product_id="N/A"

            seller=soup2.find('a',{'class':'blackText'})
            if seller:
                sell=seller.text.strip()
            else:
                sell="N/A"

            rev=soup2.find('span',{'class':'numbr-review'})
            if rev:
                reviews=rev.text.replace(' Reviews','').replace(' Review','').strip()
            else:
                reviews="N/A"


            print("Product Name:", product_name)
            print("Product Price:", product_price)
            print("Product Rating:",product_rating)
            print("Number of Ratings:", num_ratings)
            print("Product id:", product_id)
            print("Seller details:", sell)
            print("Number of reviews:", reviews)
            print("Product URL:", product_url)
            print("-" * 100)
            writer.writerow([product_name,product_price,product_rating,num_ratings,reviews,product_id,sell,product_url])
