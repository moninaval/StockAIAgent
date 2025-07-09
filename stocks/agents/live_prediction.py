import argparse
import os
import pandas as pd
import datetime
import joblib
from stock.dataloader.fetch_stock_data import fetch_live_ohlcv
from stock.model.model_utils import load_model_and_features, predict_from_model


def append_to_csv(symbol: str, data: pd.DataFrame, prediction: float):
    csv_path = f"data/{symbol}_training.csv"
    os.makedirs("data", exist_ok=True)

    # Add prediction column
    data["prediction"] = prediction
    
    # Append to CSV
    if os.path.exists(csv_path):
        data.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        data.to_csv(csv_path, mode='w', header=True, index=False)

    print(f"[+] Data appended to {csv_path}")


def run_live_prediction(symbol: str):
    print(f"[~] Running live prediction for stock: {symbol}")

    # Fetch live OHLCV data (you define this in your fetch_stock_data.py)
    live_data = fetch_live_ohlcv(symbol)  # returns DataFrame with columns: open, high, low, close, volume

    # Load model
    model_path = f"models/{symbol}_model.json"
    if not os.path.exists(model_path):
        print(f"[!] Model not found: {model_path}")
        return

    model, feature_columns = load_model_and_features(model_path)

    # Make prediction
    X_live = live_data[feature_columns]
    prediction = predict_from_model(model, X_live)

    print(f"[✓] Prediction for {symbol}: {prediction}")

    # Append to training CSV
    append_to_csv(symbol, live_data, prediction)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True, help="Stock symbol (e.g., RELIANCE)")
    args = parser.parse_args()

    run_live_prediction(args.symbol)
