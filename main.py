# Import Statements
import requests
from bs4 import BeautifulSoup
# function to scrap the web
def scraper(bbc_url,):
    """scrap the bbc website extract your specific need and show to the user"""
    response = requests.get(bbc_url)
    print(response.status_code)

    # covert the result to html parser
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())


    news_from = soup.find_all(id='bbc')
    for news in news_from:
        print(f'From:{news.text} News\n')

    # news_title = soup.find('title')
    # print(f"News Title: {news_title}")

    # extract the news heading and format it to plan text.
    news_title_article = soup.find_all('div', class_='fDtfvH')

    # loop through all the div to be able to get proper text formatting
    for article in news_title_article:
        news_heading = article.text
        print(f"The News Heading: {news_heading}\n")
    
    # get the main news content loop through it and show the user the result
    main_content_news = soup.find_all('div', class_='dEGcKf')
    for news_contents in main_content_news:
        news_body = news_contents.find_all('p', class_='hxuGS')
        for message in news_body:
            news_body_contents = f'Read News Content: {message.text}\n'
            print(news_body_contents)
        print('Thanks for read the news')
        
            
    

url = 'https://www.bbc.com/news/articles/cjr7e2z1rxyo'

# show the results