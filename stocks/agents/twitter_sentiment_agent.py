import argparse
import snscrape.modules.twitter as sntwitter
from shared.llm_interface.llm_interface import summarize_text_block

def fetch_tweets(symbol: str, max_tweets: int = 20):
    query = f"{symbol} stock"
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append(tweet.content)
    return tweets

def summarize_tweets(tweets: list, symbol: str):
    raw_text = "\n".join(tweets)
    summary = summarize_text_block(
        text=raw_text,
        purpose="summarize_news"
    )
    print(f"\n🧠 Summary for {symbol} based on Twitter:\n{summary}\n")
    return summary

def main(symbol: str):
    tweets = fetch_tweets(symbol)
    if not tweets:
        print("[!] No tweets found.")
        return
    summarize_tweets(tweets, symbol)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True, help="Stock symbol to analyze")
    args = parser.parse_args()
    main(args.symbol)
