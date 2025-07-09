import argparse
import os
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging
from datetime import datetime


def train_xgboost_for_stock(symbol: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, "../../.."))

    csv_path = os.path.join(root_dir, f"data/{symbol}_training.csv")
    model_path = os.path.join(root_dir, f"models/{symbol}_model.json")
    log_path = os.path.join(root_dir, f"logs/training_{symbol}.log")

    os.makedirs(os.path.join(root_dir, "models"), exist_ok=True)
    os.makedirs(os.path.join(root_dir, "logs"), exist_ok=True)

    logging.basicConfig(filename=log_path, level=logging.INFO, 
                        format='%(asctime)s [%(levelname)s] %(message)s')

    if not os.path.exists(csv_path):
        msg = f"[!] No training data found for {symbol} at {csv_path}"
        print(msg)
        logging.error(msg)
        return

    print(f"[~] Loading training data for {symbol}...")
    df = pd.read_csv(csv_path)
    df = df.dropna()

    feature_columns = ["open", "high", "low", "close", "volume"]
    target_column = "close"

    X = df[feature_columns]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("[~] Training XGBoost model...")
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"[✓] Model trained. MSE on test set: {mse:.4f}")
    logging.info(f"Model trained for {symbol}. MSE: {mse:.4f}")

    model.save_model(model_path)
    print(f"[+] Model saved to {model_path}")
    logging.info(f"Model saved to {model_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True, help="Stock symbol (e.g., RELIANCE)")
    args = parser.parse_args()

    train_xgboost_for_stock(args.symbol)
