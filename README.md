# 📈 Tesla Stock News

This Python bot monitors daily stock price changes for **Tesla (TSLA)** using the [Alpha Vantage API](https://www.alphavantage.co/) and sends **Telegram alerts** when significant fluctuations (>3%) occur. If such a change is detected, the bot fetches relevant news articles from [NewsAPI](https://newsapi.org/) and automatically delivers them to a specified Telegram chat.

## 🚀 Features

- Retrieves the last two closing prices for TSLA
- Calculates the percentage change between them
- If the change exceeds 3%, fetches related news headlines
- Sends the top 3 articles to Telegram using a bot

## 🧰 Technologies Used

- Python 3
- `requests` for HTTP requests
- `dotenv` for secure API key management
- Telegram Bot API
- Alpha Vantage API
- NewsAPI

## 🔐 Environment Variables (.env)

Create a `.env` file in the root directory and include:

```env
STOCK_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_newsapi_key
BOT_TOKEN=your_telegram_bot_token
BOT_CHAT_ID=your_chat_id

📦 Installation
git clone https://github.com/yourusername/tesla-stock-alert-bot.git
cd tesla-stock-alert-bot
pip install -r requirements.txt
python main.py

📬 Telegram Output Example
Headline: Tesla shares surge after earnings beat.
Brief: Tesla reported better-than-expected Q3 results, pushing the stock up 5%.

👩‍💻 Author
Kyriaki Kostika
