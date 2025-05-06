# Import Statements
import requests
from bs4 import BeautifulSoup
# function to scrap the web
def scraper(bbc_url):
    """scrap the bbc website extract your specific need and show to the user"""
    response = requests.get(bbc_url)
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())

    news_from = soup.find_all(id='bbc')
    for news in news_from:
        print(f'From:{news.text} News\n')

    new_title = soup.find_all('title')
    for title in new_title:
        print(f"New Title: {title.text}\n")

    news_title_article = soup.find_all('div', class_='fDtfvH')
    for article in news_title_article:
        news_heading = article.text
        print(f"The News Heading: {news_heading}\n")
    

    main_content_news = soup.find_all('div', class_='dEGcKf')
    for news_contents in main_content_news:
        news_body = news_contents.find_all('p', class_='hxuGS')
        for message in news_body:
            print(f"Read the news body: {message.text}\n")

        
            
    



url = 'https://www.bbc.com/news/articles/cjr7e2z1rxyo'
scraper(url)

# show the results