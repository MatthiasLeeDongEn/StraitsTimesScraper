from bs4 import BeautifulSoup
import requests
import csv
import datetime

d = datetime.datetime.now()
dayofweek = d.strftime("%a")
day = d.strftime("%d")
month = d.strftime("%m")
year = d.strftime("%y")
filename = str(dayofweek + " " + day + "-" + month + "-" + year)+ ".csv"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

source = requests.get('https://www.straitstimes.com/container/custom-landing-page/breaking-news', headers=headers).text

#BeautifulSoup allows python to parse (analyze and work with) the html data
soup = BeautifulSoup(source, 'lxml')

csv_file = open(filename, 'w', newline="") #newline = "" to remove spaces between rows

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Article Link'])


#grabs all news article
articles = soup.findAll("h3", {"class":"story-title"})

article = articles[0]
for article in articles:
    headline = article.a.text
    link = article.a.get('href')
    fLink = str('https://www.straitstimes.com' + link)
    fullLink = str("=HYPERLINK(" + "\"" + (fLink)+ "\"" + ")")
    csv_writer.writerow([headline, fullLink])

csv_file.close
