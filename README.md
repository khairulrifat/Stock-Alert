# Stock Price and News Notifier 📈📰

This project is a stock price and news notification system that automatically monitors specified stock price changes and sends relevant news articles via email. It's designed for users interested in staying informed on stock movements and related news, all from a simple, automated service.

## Project Overview
The program tracks a specified stock (in this case, Tesla, Inc. - TSLA) and checks for price fluctuations. If the stock price changes by more than a specified percentage (e.g., 5%), the system fetches relevant news articles about the company and emails them to the user. This keeps the user informed of both financial and related news updates in real-time.

## Features
- **Stock Price Monitoring**: Uses [Twelve Data API](https://twelvedata.com/) to fetch daily stock data.
- **News Fetching**: Retrieves relevant news articles from [NewsAPI](https://newsapi.org/) when there are significant stock changes.
- **Automated Notifications**: Sends email notifications containing stock change information and top related news articles.
  
## Technologies Used
- **Python**: Core programming language for script development.
- **APIs**: 
  - **Twelve Data API**: For fetching stock price data.
  - **NewsAPI**: For retrieving relevant news articles.
- **SMTP**: For sending email notifications.
- **dotenv**: To securely manage sensitive information through environment variables.
- **AWS Lambda (Optional)**: Can be configured for serverless execution and automation.

## Installation and Setup
1. Clone the repository:
      ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
3. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt

5. Create a .env file to securely store your API keys and email credentials:
   ```bash
   STOCK_API_KEY=your_stock_api_key_here
    NEWS_API_KEY=your_news_api_key_here
    MY_EMAIL=your_email_here
    MY_PASSWORD=your_password_here

7. Run the project:
    ```bash
    python main.py



## Use Cases

Daily Market Watch: Stay updated on price movements for personal investments.

Automated Alerts: Save time by automating news tracking and notifications for significant market changes.

Financial News Aggregation: Automatically get related news when important stock fluctuations occur.

## Challenges
API Rate Limits: Managing rate limits and avoiding request throttling for continuous data fetching.

Handling Sensitive Data: Implemented environment variables to protect API keys and email credentials.

Error Handling: Ensuring the program handles network errors, API downtime, and email service issues gracefully.

## Importance
This project provides a quick, real-time way for users to monitor stock price changes and get relevant news without having to manually check financial news or stock prices, helping users make informed financial decisions quickly.

   

