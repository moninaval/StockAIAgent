from crewai import Crew
from crewai.tasks import all_tasks
from crewai.agent_definitions import (
    live_prediction_agent,
    twitter_sentiment_agent,
    news_summary_agent,
    fundamentals_agent,
    final_llm_agent
)


def main():
    crew = Crew(
        agents=[
            live_prediction_agent,
            twitter_sentiment_agent,
            news_summary_agent,
            fundamentals_agent,
            final_llm_agent
        ],
        tasks=all_tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("\n🧠 Final CrewAI Output:\n")
    print(result)


if __name__ == "__main__":
    main()
