from tardis_dev import datasets
import os
import pandas as pd
import datetime


def download_for_date(exchange, data_type, date_str, candidate, api_key, download_dir) :
    """
    Downloads data for one day (from date_str to date_str+1 day) for a given candidate symbol
    into the specified download directory.
    Returns True if successful, False otherwise.
    """
    from_date = date_str
    to_date = (datetime.datetime.strptime(date_str, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    try :
        print(f"Downloading data for {candidate} on {date_str} into directory: {download_dir}")
        datasets.download(
            exchange=exchange,
            data_types=[data_type],
            from_date=from_date,
            to_date=to_date,  # Tardis downloads up to but not including to_date.
            symbols=[candidate],
            api_key=api_key,
            download_dir=download_dir
        )
        return True
    except Exception as e :
        print(f"  [!] Error downloading data for {candidate} on {date_str}: {e}")
        return False


# --- Configuration ---
exchange = "binance"
data_type = "quotes"
api_key = ""  # Replace with your actual Tardis API key
base_download_dir = "" ## define your download directory here

tokens = ["ETH"] # Add more tokens as needed

# date range
start_date = datetime.datetime(2023, 8, 8)
end_date = datetime.datetime(2023, 8, 8)
date_range = [(start_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in
              range((end_date - start_date).days + 1)]

# Process each token
for token in tokens :
    # Skip tokens that already include "USDT"
    if "USDT" in token :
        print(f"Skipping token {token} because it already contains 'USDT'.")
        continue


    candidate = token + "USDT"

    # Create directory for the token
    candidate1_dir = os.path.join(base_download_dir, candidate)
    os.makedirs(candidate1_dir, exist_ok=True)

    print(f"\n===== Processing token: {token} =====")
    print(f"Using candidate: {candidate} -> Directory: {candidate1_dir}")

    # Process each date in the range
    for date_str in date_range :
        success = download_for_date(exchange, data_type, date_str, candidate, api_key, candidate1_dir)
        if not success :
            print(
                f"  [!] Data not available for {token} on {date_str} using candidate {candidate}. Skipping this date.")
