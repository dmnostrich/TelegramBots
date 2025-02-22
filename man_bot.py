import requests
import feedparser
from telegram import Bot

TELEGRAM_BOT_TOKEN = "##BOT_TOKNE_HERE##"
TELEGRAM_CHANNEL_ID = "@CHANNEL_ID_HERE"  # OR "-100XXXXXXXXXX"

# List of Cybersecurity News RSS Feeds
RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.darkreading.com/rss.xml",
    "https://www.cshub.com/rss/articles",
    "https://www.securityweek.com/rss.xml",
    "https://www.scmagazine.com/home/feed/",
    "https://www.infosecurity-magazine.com/rss/news/"
]

# Initialize Telegram Bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Function to Fetch Latest Cybersecurity News
def fetch_news():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        if feed.entries:
            latest_news = feed.entries[0]  # Get the latest news entry
            title = latest_news.title
            link = latest_news.link
            message = f"🔥 *Cybersecurity News Update* 🔥\n\n📰 {title}\n🔗 Read more: {link}"
            send_telegram_message(message)
        else:
            print(f"No news found for {feed_url}")

# Function to Send News to Telegram Channel
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHANNEL_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, data=data)
    print("News sent!", response.json())

if __name__ == "__main__":
    print("Fetching latest cybersecurity news...")
    fetch_news()
    print("Execution completed.")
