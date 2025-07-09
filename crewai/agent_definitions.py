from crewai import Agent

live_prediction_agent = Agent(
    role="Market Predictor",
    goal="Predict short-term and intraday price movement for a given stock",
    backstory="An expert in financial data modeling and machine learning, especially using XGBoost to analyze price trends.",
    verbose=True
)

twitter_sentiment_agent = Agent(
    role="Public Sentiment Analyst",
    goal="Summarize real-time public sentiment for a stock from Twitter",
    backstory="Analyzes stock-related tweets using LLMs to detect public optimism, fear, or concern.",
    verbose=True
)

news_summary_agent = Agent(
    role="News Analyst",
    goal="Summarize recent news headlines about a stock",
    backstory="Specializes in collecting and summarizing recent financial and economic news articles using LLMs.",
    verbose=True
)

fundamentals_agent = Agent(
    role="Company Fundamentals Analyst",
    goal="Extract and summarize a stock's key financial ratios and indicators",
    backstory="Reads balance sheet data and extracts metrics such as P/E ratio, ROE, and growth.",
    verbose=True
)

final_llm_agent = Agent(
    role="LLM Decision Assistant",
    goal="Analyze model output, public sentiment, news, and fundamentals to generate a final stock outlook",
    backstory="Combines all available data to provide a high-level LLM interpretation and final recommendation.",
    verbose=True
) 
