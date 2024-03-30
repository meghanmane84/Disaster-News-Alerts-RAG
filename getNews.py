import feedparser
import csv
import datetime
import time

def fetch_google_news_feed(rss_url):
    feed = feedparser.parse(rss_url)
    if feed.get('entries'):
        return feed.entries
    else:
        print("Failed to fetch data from Google News RSS feed.")
        return None

def save_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Timestamp', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for item in data:
            writer.writerow({'Title': item.get('title', ''), 
                             'Timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                             'Content': item.get('summary', '')})

def main():
    rss_url = 'https://news.google.com/rss/search?q=disaster'
    num_iterations = 4
    iteration = 0
    while iteration < num_iterations:
        data = fetch_google_news_feed(rss_url)
        if data:
            save_to_csv(data, './DisasterNews/disasternews.csv')
            print("Data extracted from Google News RSS feed and saved successfully.")
        else:
            print("Failed to fetch data from the Google News RSS feed.")
        iteration += 1
        if iteration < num_iterations:
            print(f"Waiting for 5 minutes before the next iteration...")
            time.sleep(5 * 60)  # Wait for 5 minutes (300 seconds) before the next iteration

if __name__ == "__main__":
    main()
