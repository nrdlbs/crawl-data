import requests
import pandas as pd
import time
from tqdm import tqdm

def fetch_data(limit=100, offset=0):
    """Fetch data from Polymarket API with pagination"""
    url = f"https://gamma-api.polymarket.com/events?limit={limit}&offset={offset}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def extract_market_data(event):
    """Extract market data from event"""
    markets_data = []
    
    # Event data
    event_id = event.get('id')
    event_slug = event.get('slug')
    event_title = event.get('title')
    event_description = event.get('description')
    
    # Series data
    series = event.get('series', [{}])[0] if event.get('series') else {}
    series_title = series.get('title')
    series_slug = series.get('slug')
    
    # Process each market in the event
    for market in event.get('markets', []):
        market_data = {
            'id': market.get('id'),
            'slug': market.get('slug'),
            'startDate': market.get('startDate'),
            'endDate': market.get('endDate'),
            'volume': market.get('volume1yr', 0),  # Using volume1yr as general volume
            'liquidity': market.get('liquidity', 0),
            'description': market.get('description'),
            'event_title': event_title,
            'event_slug': event_slug,
            'event_description': event_description,
            'series_title': series_title,
            'series_slug': series_slug
        }
        markets_data.append(market_data)
    
    return markets_data

def main():
    all_markets = []
    limit = 100
    offset = 0
    total_records = 0
    
    print("Fetching data from Polymarket API...")
    
    # First request to get an idea of total data
    initial_data = fetch_data(limit, offset)
    if initial_data:
        print(f"Successfully connected to API. Processing data in batches of {limit}...")
    
    # Continue fetching until we get an empty response
    with tqdm(desc="Fetching records") as pbar:
        while True:
            data = fetch_data(limit, offset) if offset > 0 else initial_data
            
            if not data:
                break
                
            for event in data:
                markets = extract_market_data(event)
                all_markets.extend(markets)
            
            records_fetched = len(data)
            total_records += records_fetched
            pbar.update(records_fetched)
            
            if records_fetched < limit:  # Last page
                break
                
            offset += limit
            time.sleep(0.5)  # To avoid hitting rate limits
    
    print(f"Finished fetching {total_records} events with {len(all_markets)} markets")
    
    # Convert to DataFrame and export to Excel
    if all_markets:
        df = pd.DataFrame(all_markets)
        
        # Save to Excel
        output_file = "polymarket_data.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Data successfully exported to {output_file}")
    else:
        print("No data to export")

if __name__ == "__main__":
    main()
