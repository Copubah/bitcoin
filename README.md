# Bitcoin Price Checker

## Description
The Bitcoin Price Checker is a Python script that fetches the current price of Bitcoin from the CoinGecko API, logs the price to a CSV file, and provides additional features such as:

- Logging price data with timestamps.
- Sending email notifications when the price crosses a defined threshold.
- Visualizing price trends over time using a graph.

## Features
1. Fetch Current Price: Retrieves the latest Bitcoin price in the specified currency.
2. Log Price Data: Saves the price along with a timestamp to a CSV file.
3. Threshold Alerts: Alerts the user if the price exceeds or falls below predefined thresholds.
4. Graphical Visualization: Generates a graph of price trends over time.

## Requirements
- Python 3.8 or higher
- Required Python libraries:
  - requests
  - matplotlib
  - csv

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Configuration
Update the `config.py` file with the following settings:
- CRYPTO_ID: The cryptocurrency ID (e.g., bitcoin).
- CURRENCY: The currency to fetch the price in (e.g., usd).
- LOG_FILE: Path to the CSV file for logging prices.
- UPPER_THRESHOLD: Upper price threshold for alerts.
- LOWER_THRESHOLD: Lower price threshold for alerts.

## Usage
1. Run the script to fetch the current price:
   ```bash
   python3 price_checker.py
   ```
2. The script will log the price to the CSV file and display alerts if thresholds are crossed.
3. To visualize price trends, ensure the CSV file has data and run the script. A graph will be displayed automatically.

## Example Output
- Console Output:
  ```
  Current price: 68591
  ALERT: Price exceeded upper threshold!
  ```
- Graph:
  A line graph showing price trends over time.

## License
This project is licensed under the MIT License.