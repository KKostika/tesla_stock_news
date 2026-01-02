import requests
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT =  "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
bot_token = os.getenv("BOT_TOKEN")
bot_chatID = os.getenv("BOT_CHAT_ID")




def telegram_bot(bot_message):

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        "chat_id": bot_chatID,
        "text": bot_message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)
    return response.json()


# Get the yesterday's closing price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT,params=stock_params )
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

#It finds the positive difference between 1 and 2
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# The percent of the difference
dif_percent = round((difference / float(yesterday_closing_price)) * 100)
print(dif_percent)

# Getting the first 3 articles/ news of the company we are interested in whenever there is a difference bigger than 3%.
if dif_percent > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    print('\n')


    formatted_articles = [f"{STOCK_NAME}: {up_down}{dif_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)


    for article in formatted_articles:
        message = telegram_bot(article)
        print(message)




