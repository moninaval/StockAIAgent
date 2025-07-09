from crewai import Task
from .agent_definitions import (
    live_prediction_agent,
    twitter_sentiment_agent,
    news_summary_agent,
    fundamentals_agent,
    final_llm_agent
)

# Live prediction using model output
live_prediction_task = Task(
    agent=live_prediction_agent,
    description="Fetch the latest market data, run the XGBoost model, and predict price movement.",
    expected_output="Short-term trend direction and confidence score."
)

# Twitter sentiment
sentiment_task = Task(
    agent=twitter_sentiment_agent,
    description="Summarize the latest tweets about the stock and extract public sentiment.",
    expected_output="LLM-generated sentiment summary (positive, neutral, or negative) with reasons."
)

# News summary
news_task = Task(
    agent=news_summary_agent,
    description="Fetch and summarize recent news articles and headlines about the stock.",
    expected_output="Concise news summary highlighting bullish or bearish signals."
)

# Fundamentals parsing
fundamentals_task = Task(
    agent=fundamentals_agent,
    description="Extract P/E, ROE, debt/equity, and other financial indicators from company data.",
    expected_output="Tabular and textual summary of company fundamentals."
)

# Final LLM synthesis
final_llm_task = Task(
    agent=final_llm_agent,
    description="Combine model prediction, Twitter sentiment, news summary, and fundamentals to provide a final LLM-based analysis and recommendation.",
    expected_output="Final outlook summary with explanation: bullish, bearish, or neutral."
)

# Bundle all tasks into a list
all_tasks = [
    live_prediction_task,
    sentiment_task,
    news_task,
    fundamentals_task,
    final_llm_task
]
