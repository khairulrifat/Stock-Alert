import requests
from twilio.rest import Client
import smtplib
import requests

import smtplib

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")



MY_PASSWORD = "axcc roxv scrc kvdi"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://api.twelvedata.com/time_series"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



# Get yesterday's closing stock price
stock_params = {
    "symbol": STOCK_NAME,
    "interval": "1day",
    "apikey": STOCK_API_KEY,
    "outputsize": "2",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["values"]
yesterday_data = data[0]
yesterday_closing_price = yesterday_data["close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data[1]
day_before_yesterday_closing_price = day_before_yesterday_data["close"]
print(day_before_yesterday_closing_price)

# Find the positive difference
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"

# Calculate the percentage difference
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# Get news articles if the difference percentage is greater than 1%
if abs(diff_percent) > .5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # Format articles and send notifications
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]


    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="khairulrifat000@gmail.com",
                msg=f"Subject:Stock price changed!\n\n{article}".encode('utf-8')
            )