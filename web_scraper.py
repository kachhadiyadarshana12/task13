import requests
from bs4 import BeautifulSoup
import csv

#scrape friendly website.
URL = "https://quotes.toscrape.com/" # type: ignore

#html content using requests.
try:
    print("Connecting to website........")
    response = requests.get(URL)
    #check if request was successful (status code 200 means ok).
    if response.status_code == 200:
        print("Website fetched successfully..")
    else:
        print("Failed to fetch website. status code:", response.status_code)
        exit()

except requests.exceptions.RequestException as e:
    #handle connection errors.
    print("Request Error : ", e)
    exit()

#parse html using beautifulsoup and python's built-in html parser
soup = BeautifulSoup(response.text, "html.parser")
#identify html tags and attributes and quote is inside div with class "quote"
quote_blocks = soup.find_all("div", class_="quote")

#open csv file in write mode
with open("scraped_quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    #column headers
    writer.writerow(["Quote Text", "Author", "Author Link"])
    #loop of quote block
    for quote in quote_blocks:

        #extract quote text
        text_tag = quote.find("span", class_="text")
        if text_tag:
            text = text_tag.text.strip() 
        else:
            "Not Available"
        
        #extract author name
        author_tag = quote.find("small", class_="author") 
        if author_tag:
            author = author_tag.text.strip()
        else: 
            "Not Available"

        #extract author profile link
        link_tag = quote.find("a")
        if link_tag:
            link = "https://quotes.toscrape.com" + link_tag["href"]
        else:
            "Not Available"

        #extracted data into csv file
        writer.writerow([text, author, link])

print("Data sucessfully saved to scraped_quotes.csv")
print("Scraping completed ethically from a legal practice website.")