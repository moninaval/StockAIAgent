import argparse
import os
import yfinance as yf
from shared.llm_interface.llm_interface import summarize_text_block

def get_fundamentals(symbol: str) -> dict:
    try:
        ticker = yf.Ticker(symbol + ".NS")  # ".NS" suffix for NSE stocks
        info = ticker.info

        return {
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "Debt/Equity": info.get("debtToEquity", "N/A"),
            "ROE": f"{info.get('returnOnEquity', 0) * 100:.2f}%" if info.get("returnOnEquity") else "N/A",
            "Revenue Growth": f"{info.get('revenueGrowth', 0) * 100:.2f}%" if info.get("revenueGrowth") else "N/A",
            "Net Profit Margin": f"{info.get('netMargins', 0) * 100:.2f}%" if info.get("netMargins") else "N/A",
            "Market Cap": f"₹{round(info.get('marketCap', 0) / 1e5):,} Lakhs" if info.get("marketCap") else "N/A",
            "Dividend Yield": f"{info.get('dividendYield', 0) * 100:.2f}%" if info.get("dividendYield") else "N/A",
        }

    except Exception as e:
        print(f"[!] Failed to fetch fundamentals for {symbol}: {e}")
        return {
            "P/E Ratio": "N/A",
            "Debt/Equity": "N/A",
            "ROE": "N/A",
            "Revenue Growth": "N/A",
            "Net Profit Margin": "N/A",
            "Market Cap": "N/A",
            "Dividend Yield": "N/A"
        }

def format_fundamentals(fundamentals: dict) -> str:
    return "\n".join(f"{key}: {value}" for key, value in fundamentals.items())

def save_fundamentals_text(symbol: str, text: str):
    os.makedirs("data", exist_ok=True)
    path = f"data/{symbol}_fundamentals.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[+] Saved fundamentals to: {path}")

def main(symbol: str):
    fundamentals = get_fundamentals(symbol)
    text = format_fundamentals(fundamentals)
    save_fundamentals_text(symbol, text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True, help="Stock symbol (e.g., RELIANCE)")
    args = parser.parse_args()
    main(args.symbol)
