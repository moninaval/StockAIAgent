import argparse
import os
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib


def train_xgboost_for_stock(symbol: str):
    csv_path = f"data/{symbol}_training.csv"
    model_path = f"models/{symbol}_model.json"
    os.makedirs("models", exist_ok=True)

    if not os.path.exists(csv_path):
        print(f"[!] No training data found for {symbol} at {csv_path}")
        return

    print(f"[~] Loading training data for {symbol}...")
    df = pd.read_csv(csv_path)

    # Drop rows with missing values
    df = df.dropna()

    # Define features and target
    feature_columns = ["open", "high", "low", "close", "volume"]
    target_column = "close"  # or "prediction" if you're doing self-supervised refinement

    X = df[feature_columns]
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("[~] Training XGBoost model...")
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"[✓] Model trained. MSE on test set: {mse:.4f}")

    # Save model
    model.save_model(model_path)
    print(f"[+] Model saved to {model_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True, help="Stock symbol (e.g., RELIANCE)")
    args = parser.parse_args()

    train_xgboost_for_stock(args.symbol)
