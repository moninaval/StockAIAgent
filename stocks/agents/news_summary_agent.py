import argparse
import requests
from shared.llm_interface import summarize_text_block

# Replace with actual News API later if needed
def fetch_mock_news(symbol: str):
    return [
        f"{symbol} announces quarterly earnings beating analyst expectations",
        f"{symbol} signs strategic deal in EV battery sector",
        f"{symbol} faces mild regulatory headwinds in export markets"
    ]

def summarize_news(news_list: list, symbol: str):
    raw_text = "\n".join(news_list)
    summary = summarize_text_block(
        text=raw_text,
        purpose="summarize_news"
    )
    print(f"\n🧠 Summary for {symbol} based on News:\n{summary}\n")
    return summary

def main(symbol: str):
    news_list = fetch_mock_news(symbol)
    summarize_news(news_list, symbol)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    args = parser.parse_args()
    main(args.symbol)
