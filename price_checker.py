import requests
import csv
import os
from datetime import datetime, UTC
import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt


def get_price():
    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={config.CRYPTO_ID}&vs_currencies={config.CURRENCY}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[config.CRYPTO_ID][config.CURRENCY]
    except requests.RequestException as e:
        print(f"Error fetching price: {e}")
        return None


def log_price(price):
    if price is None:
        return

    file_exists = os.path.isfile(config.LOG_FILE)

    with open(config.LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp_utc", "price"])

        timestamp = datetime.now(UTC).isoformat()
        writer.writerow([timestamp, price])


def check_threshold(price):
    if price is None:
        return

    if price >= config.UPPER_THRESHOLD:
        print("ALERT: Price exceeded upper threshold!")
    elif price <= config.LOWER_THRESHOLD:
        print("ALERT: Price dropped below lower threshold!")


def send_email_notification(current_price):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    subject = "Bitcoin Price Alert!"
    body = f"The current Bitcoin price is {current_price}, which has crossed your threshold of {THRESHOLD_PRICE}."

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email notification sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def plot_price_trends():
    if not os.path.isfile(config.LOG_FILE):
        print("No price log file found to plot.")
        return

    timestamps = []
    prices = []

    with open(config.LOG_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamps.append(datetime.fromisoformat(row["timestamp_utc"]))
            prices.append(float(row["price"]))

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, marker="o", linestyle="-", color="b")
    plt.title("Bitcoin Price Trends")
    plt.xlabel("Timestamp (UTC)")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    price = get_price()

    if price is None:
        print("Price check failed.")
        return

    print(f"Current price: {price}")
    log_price(price)
    check_threshold(price)

    # Plot price trends
    plot_price_trends()


if __name__ == "__main__":
    main()