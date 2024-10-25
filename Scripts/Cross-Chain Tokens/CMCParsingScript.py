import requests
import time

# Insert your CoinMarketCap API key
API_KEY = 'KEY'

# URL for getting the list of tokens
url_listings = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# URL for getting token information
url_info = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info"

# Request parameters for the token listings
parameters_listings = {
    'limit': 2000,
    'aux': 'platform'
}

# Request headers
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

# Execute request to get the list of tokens
response_listings = requests.get(url_listings, headers=headers, params=parameters_listings)

# Check if the request was successful
if response_listings.status_code == 200:
    data_listings = response_listings.json()
    
    # List to store results
    results = []

    # Process the data
    for token in data_listings['data']:
        token_id = token['id']
        
        # Execute request to get information about each token
        parameters_info = {
            'id': token_id
        }
        
        response_info = requests.get(url_info, headers=headers, params=parameters_info)
        
        if response_info.status_code == 200:
            data_info = response_info.json()
            token_info = data_info['data'][str(token_id)]
            
            # Get contract addresses
            contract_addresses = token_info.get('contract_address', [])
            
            # Check the number of contract addresses
            if len(contract_addresses) > 1:
                # Get the website URL
                urls = token_info.get('urls', {})
                website_list = urls.get('website', [])
                website = website_list[0] if website_list else 'No website available'
                token_name = token_info.get('name', 'Unknown Token')
                results.append(f"{token_name} : {website}")
        
        # Add a pause between requests to avoid exceeding API limits
        time.sleep(1)
    
    # Write results to a file
    with open('tokens_with_multiple_addresses.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

    print("Results have been saved to tokens_with_multiple_addresses.txt")

else:
    print(f"Failed to retrieve data: {response_listings.status_code} - {response_listings.text}")
