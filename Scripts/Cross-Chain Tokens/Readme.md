# Cross-Chain Token Parser

This Python script fetches information about cryptocurrency tokens using the CoinMarketCap API. It retrieves tokens with multiple contract addresses and saves the relevant details to a text file.

## Features

- Fetches the latest cryptocurrency listings.
- Gathers detailed information about each token, including contract addresses and website URLs.
- Filters tokens with more than one contract address.
- Saves results to a text file for easy access.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install requests
   ```

3. **Obtain a CoinMarketCap API key**:
   - Sign up at [CoinMarketCap](https://coinmarketcap.com/) and get your API key.

4. **Add your API key**:
   - Replace the placeholder in the script:
   ```python
   API_KEY = 'your_api_key_here'
   ```

## Usage

1. **Run the script**:
   ```bash
   python token_info_fetcher.py
   ```

2. **Output**:
   - The results will be saved in a file named `tokens_with_multiple_addresses.txt`.

## Example Task

You can customize the script to fetch specific information. For example, to list tokens with a market cap over $50M that have multiple contract addresses, modify the relevant parts of the code.

## Notes

- Be mindful of the API rate limits. The script includes a delay to avoid exceeding them.
- Make sure to handle your API key securely.
