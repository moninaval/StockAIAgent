import argparse
import os

from shared.llm_interface.llm_interface import summarize_text_block

def read_text_file(path):
    if not os.path.exists(path):
        print(f"[!] Missing file: {path}")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def prepare_combined_input(symbol):
    fundamentals_path = f"data/{symbol}_fundamentals.txt"
    prediction_path = f"data/{symbol}_live_prediction.txt"

    fundamentals_text = read_text_file(fundamentals_path)
    prediction_text = read_text_file(prediction_path)

    combined_input = (
        f"Company: {symbol}\n\n"
        f"[Fundamentals]\n{fundamentals_text.strip()}\n\n"
        f"[Model Prediction]\n{prediction_text.strip()}\n"
    )
    return combined_input

def run_llm_prediction(symbol):
    combined_text = prepare_combined_input(symbol)
    if not combined_text.strip():
        print("[!] Cannot proceed — missing input.")
        return

    final_summary = summarize_text_block(
        text=combined_text,
        purpose="fundamentals_and_prediction"
    )
    print(f"\n📈 Final LLM-Based Insight for {symbol}:\n{final_summary}\n")

    output_path = f"data/{symbol}_llm_final_summary.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_summary)
    print(f"[+] Saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True, help="Stock symbol")
    args = parser.parse_args()
    run_llm_prediction(args.symbol)
