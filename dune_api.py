import os
import requests
import io
import pandas as pd

# Configuration: set your query_id and API key here
api_key = ""
url = "https://api.dune.com/api/v1/query/4931834/results/csv"

headers = {"X-DUNE-API-KEY": api_key}
limit = 500000  # Maximum rows per page (adjust if needed)
offset = 0      # Starting offset
page_num = 1    # Counter for file naming

# Directory to save CSV files
output_dir = "cexdex_tx"
os.makedirs(output_dir, exist_ok=True)

while True:
    params = {"limit": limit, "offset": offset, "sort_by": "block_number", "sort_order": "asc"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Failed to fetch data. Status code:", response.status_code)
        break

    # Load CSV text into a pandas DataFrame
    csv_data = io.StringIO(response.text)
    df = pd.read_csv(csv_data)

    # Convert the block_number column to integer, if it exists.
    if "block_number" in df.columns:
        try:
            df["block_number"] = df["block_number"].astype(int)
        except Exception as e:
            print(f"Error converting block_number column: {e}")

    # Save the modified DataFrame to a CSV file
    file_path = os.path.join(output_dir, f"{page_num}.csv")
    df.to_csv(file_path, index=False)
    print(f"Saved page {page_num} to {file_path}")

    # Check for the next offset from response headers
    next_offset = response.headers.get("x-dune-next-offset")
    if next_offset:
        offset = int(next_offset)
        page_num += 1
    else:
        print("No more pages to fetch.")
        break

print("Finished fetching all pages.")

