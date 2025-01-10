import requests as rq
from twilio.rest import Client
import os
from datetime import datetime,timedelta




STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "GC5KG4L52FY85ZXG"
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY="4a5191f6c487473bba48dab2816fa460"
news_parameters={
    "apiKey":NEWS_KEY,
    "qInTitle": COMPANY_NAME,
}

account_sid = "AC77812d86d34bccafde0f51f523235923"
auth_token = os.environ.get("AUTH_TOKEN")

day_before = datetime.today() - timedelta(days=3)
day_before = day_before.strftime('%Y-%m-%d')

yesterday = datetime.today() - timedelta(days=2)
yesterday = yesterday.strftime('%Y-%m-%d')

stock_rq = rq.get(url=STOCK_ENDPOINT,params=stock_parameters)
stock_data = stock_rq.json()

yesterday_stock = round(float(stock_data["Time Series (Daily)"][yesterday]["4. close"]),2)
day_before_stock = round(float(stock_data["Time Series (Daily)"][day_before]["4. close"]),2)

difference = (yesterday_stock-day_before_stock)
diff_percent = (difference/yesterday_stock) * 100
up_down = None
if difference >0:
    up_down = "🔺"
else:
    up_down= "🔻"
if abs(diff_percent) > 5:
    news_response = rq.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_="+16014363633",
            to="+5553981613401",
        )


