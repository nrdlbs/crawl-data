import requests
import json
import time
import os
import sys
import multiprocessing
from typing import List, Dict, Any, Optional, Tuple

# API endpoints
MARKET_BY_ID_URL = "https://gamma-api.polymarket.com/markets/{market_id}"
MARKET_BY_CONDITION_URL = "https://clob.polymarket.com/markets/{condition_id}"
PRICE_HISTORY_URL = "https://clob.polymarket.com/prices-history?interval=1m&market={token_id}&fidelity=10"

# API call counter and delay settings
API_CALL_THRESHOLD = 1000000000
API_DELAY = 1  # 1 second delay after threshold API calls

# Output file settings
TOKENS_THRESHOLD = 50  # Write to file after collecting this many tokens
NUM_PROCESSES = 8  # Number of processes to use

def read_market_ids(file_path: str) -> List[str]:
    """Read market IDs from file and sort in descending order"""
    with open(file_path, 'r') as f:
        market_ids = [line.strip() for line in f.readlines() if line.strip()]
    
    market_ids.sort(reverse=True)  # Sort in descending order
    return market_ids

def check_api_call_delay(api_call_count: int) -> int:
    """Check if we need to add a delay after API calls"""
    api_call_count += 1
    
    if api_call_count % API_CALL_THRESHOLD == 0:
        print(f"Made {api_call_count} API calls. Pausing for {API_DELAY} second...")
        time.sleep(API_DELAY)
    
    return api_call_count

def get_market_by_id(market_id: str, api_call_count: int) -> Tuple[Optional[Dict[str, Any]], int]:
    """Call API 1 to get market details by ID"""
    url = MARKET_BY_ID_URL.format(market_id=market_id)
    try:
        response = requests.get(url)
        api_call_count = check_api_call_delay(api_call_count)
        
        if response.status_code == 200:
            return response.json(), api_call_count
        else:
            print(f"Error fetching market {market_id}: {response.status_code}")
            return None, api_call_count
    except Exception as e:
        print(f"Exception fetching market {market_id}: {e}")
        return None, api_call_count

def get_market_by_condition(condition_id: str, api_call_count: int) -> Tuple[Optional[Dict[str, Any]], int]:
    """Call API 2 to get market details by condition ID"""
    url = MARKET_BY_CONDITION_URL.format(condition_id=condition_id)
    try:
        response = requests.get(url)
        api_call_count = check_api_call_delay(api_call_count)
        
        if response.status_code == 200:
            return response.json(), api_call_count
        else:
            print(f"Error fetching condition {condition_id}: {response.status_code}")
            return None, api_call_count
    except Exception as e:
        print(f"Exception fetching condition {condition_id}: {e}")
        return None, api_call_count

def get_price_history(token_id: str, api_call_count: int) -> Tuple[Optional[List[Dict[str, Any]]], int]:
    """Call API 3 to get price history for token"""
    url = PRICE_HISTORY_URL.format(token_id=token_id)
    try:
        response = requests.get(url)
        api_call_count = check_api_call_delay(api_call_count)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('history', []), api_call_count
        else:
            print(f"Error fetching history for token {token_id}: {response.status_code}")
            return None, api_call_count
    except Exception as e:
        print(f"Exception fetching history for token {token_id}: {e}")
        return None, api_call_count

def process_market(market_id: str, api_call_count: int) -> Tuple[Optional[List[Dict[str, Any]]], int]:
    """Process a market ID through all APIs and return tuples"""
    results = []
    
    # Call API 1 to get condition_id
    print(f"Fetching market data for ID: {market_id}")
    market_data_result = get_market_by_id(market_id, api_call_count)
    market_data, api_call_count = market_data_result

    if not market_data:
        print(f"No market data found for {market_id}, skipping")
        return None, api_call_count
    
    condition_id = market_data.get('conditionId')
    if not condition_id:
        print(f"No condition ID found for market {market_id}, skipping")
        return None, api_call_count
    
    # Call API 2 to get tokens
    print(f"Fetching condition data for ID: {condition_id}")
    condition_data_result = get_market_by_condition(condition_id, api_call_count)
    condition_data, api_call_count = condition_data_result
    
    if not condition_data:
        print(f"No token data found for condition {condition_id}, skipping")
        return None, api_call_count
    
    tokens = condition_data.get('tokens', [])
    market_slug = condition_data.get('market_slug', '')
    
    # For each token, get price history and create tuple
    for token in tokens:
        token_id = token.get('token_id')
        if not token_id:
            continue
        
        # Call API 3 to get price history
        print(f"Fetching price history for token: {token_id}")
        history_result = get_price_history(token_id, api_call_count)
        history, api_call_count = history_result
        
        if history is None or len(history) == 0:  # Empty history is fine, but None means error
            continue
        
        # If we get empty history for a token, we might want to skip this market ID
        # and all smaller ones based on the requirement, but for robustness we'll just
        # continue processing other tokens in this market
        
        # Create tuple
        result = {
            'token_id': token_id,
            'outcome': token.get('outcome', ''),
            'price': token.get('price', 0),
            'market_id': market_id,
            'market_slug': market_slug,
            'history_price': history, 
            'outcomes': market_data.get('outcomes', []),
            'outcome_prices': market_data.get('outcomePrices', [])
        }
        
        results.append(result)
    
    return results, api_call_count

def append_to_json_file(data: List[Dict[str, Any]], file_path: str):
    """Append data to a JSON file containing an array"""
    # Track total records for return value
    total_records = 0
    
    # If file doesn't exist yet, create it with initial data
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            f.write("[\n")
            for i, item in enumerate(data):
                json_line = json.dumps(item)
                if i < len(data) - 1:
                    f.write(f"  {json_line},\n")
                else:
                    f.write(f"  {json_line}\n")
            f.write("]")
        total_records = len(data)
    else:
        # File exists - use a more efficient approach without loading the entire file
        try:
            # Open file in read mode to count records
            with open(file_path, 'r') as f:
                # Just count the records without loading the entire structure
                first_char = f.read(1)
                if first_char != '[':
                    print(f"Warning: Existing data in {file_path} is not a list. Creating new file.")
                    with open(file_path, 'w') as f:
                        f.write("[\n")
                        for i, item in enumerate(data):
                            json_line = json.dumps(item)
                            if i < len(data) - 1:
                                f.write(f"  {json_line},\n")
                            else:
                                f.write(f"  {json_line}\n")
                        f.write("]")
                    total_records = len(data)
                    return total_records
                
                # Count records by counting commas between objects at the top level
                f.seek(0)
                content = f.read()
                # Count objects by finding top-level commas between objects
                # This is a rough estimate that works for well-formatted JSON arrays
                depth = 0
                in_string = False
                escape_next = False
                comma_count = 0
                
                for char in content:
                    if escape_next:
                        escape_next = False
                        continue
                    
                    if char == '\\':
                        escape_next = True
                    elif char == '"' and not escape_next:
                        in_string = not in_string
                    elif not in_string:
                        if char == '{' or char == '[':
                            depth += 1
                        elif char == '}' or char == ']':
                            depth -= 1
                        elif char == ',' and depth == 1:  # Top-level comma
                            comma_count += 1
                
                # Number of objects is comma count + 1 (if file has at least one object)
                if '[' in content and ']' in content:
                    total_records = comma_count + 1
                    if '[]' in content.replace(' ', ''):  # Empty array
                        total_records = 0
                
                # Rewrite the file with the new data appended
                # We'll rewrite by finding the closing bracket and inserting before it
                with open(file_path, 'r+') as f:
                    f.seek(0, os.SEEK_END)  # Go to end of file
                    pos = f.tell() - 1
                    
                    # Find the last closing bracket
                    while pos > 0:
                        f.seek(pos)
                        char = f.read(1)
                        if char == ']':
                            break
                        pos -= 1
                    
                    if pos > 0:
                        f.seek(pos)
                        # If array wasn't empty, add a comma
                        prefix = ",\n" if total_records > 0 else ""
                        
                        # Write each item on a single line
                        f.seek(pos)
                        for i, item in enumerate(data):
                            json_line = json.dumps(item)
                            if i == 0:
                                f.write(f"{prefix}  {json_line}")
                            else:
                                f.write(f",\n  {json_line}")
                        
                        f.write("\n]")
                        f.truncate()
                        
                        total_records += len(data)
        except Exception as e:
            # If any error occurs, fall back to the simple approach
            print(f"Warning: Error during optimized append: {str(e)}. Using fallback method.")
            try:
                with open(file_path, 'r') as f:
                    all_data = json.load(f)
                
                if not isinstance(all_data, list):
                    all_data = []
                
                all_data.extend(data)
                total_records = len(all_data)
                
                with open(file_path, 'w') as f:
                    f.write("[\n")
                    for i, item in enumerate(all_data):
                        json_line = json.dumps(item)
                        if i < len(all_data) - 1:
                            f.write(f"  {json_line},\n")
                        else:
                            f.write(f"  {json_line}\n")
                    f.write("]")
            except:
                # Last resort - overwrite with just the new data
                with open(file_path, 'w') as f:
                    f.write("[\n")
                    for i, item in enumerate(data):
                        json_line = json.dumps(item)
                        if i < len(data) - 1:
                            f.write(f"  {json_line},\n")
                        else:
                            f.write(f"  {json_line}\n")
                    f.write("]")
                total_records = len(data)
    
    print(f"Appended {len(data)} records to {file_path}. Total records: {total_records}")
    return total_records

def worker_process(start_idx: int, end_idx: int, market_ids: List[str], output_file: str, mile_stone: str):
    import os
    
    # Print the process ID for debugging and monitoring
    print(f"Worker process ID: {os.getpid()}")

    """Worker process to handle a range of market IDs"""
    print(f"Process starting: Processing market IDs from index {start_idx} to {end_idx}")
    print(f"Output file: {output_file}")


    
    all_results = []
    api_call_count = 0
    total_saved_records = 0
    active = False
    # consecutive_empty_count = 0
    
    try:
        for i in range(start_idx, end_idx + 1):
            if i >= len(market_ids):
                break
                
            market_id = market_ids[i]
            if market_id == mile_stone:
                active = True
                continue
            # if not active:
            #     print('22222')
            #     continue

            print(f"\n[{i+1}/{len(market_ids)}] Processing market ID: {market_id}")
            
            results_tuple = process_market(market_id, api_call_count)
            results, api_call_count = results_tuple

            if not results or len(results) == 0:
                print(f"No results for market {market_id}, continuing to next market")
                continue
            
            # if not results:
            #     consecutive_empty_count += 1
            #     print(f"No results for market {market_id}, continuing to next market")
                
            #     # If we get too many consecutive empty results, we might break
            #     # (based on the requirement about breaking the loop when history is empty)
            #     if consecutive_empty_count > 5:  # Allow some failures before giving up
            #         print(f"Too many consecutive empty results. Breaking the loop.")
            #         break
                
            #     continue
            
            # Reset consecutive empty counter when we find results
            # consecutive_empty_count = 0
            
            all_results.extend(results)
            print(f"Completed processing market ID: {market_id}. Total records in memory: {len(all_results)}")
            
            # Check if we should append to the file
            if len(all_results) >= TOKENS_THRESHOLD:
                total_saved_records = append_to_json_file(all_results, output_file)
                all_results = []  # Clear the in-memory results after saving
        
        # Save any remaining results
        if all_results:
            total_saved_records = append_to_json_file(all_results, output_file)
        
        print(f"Process complete. Total records saved: {total_saved_records}")
        print(f"Total API calls made: {api_call_count}")
    
    except Exception as e:
        print(f"Error in worker process: {e}")
        # Save partial results if error occurs
        if all_results:
            partial_output = f"{output_file}.partial.json"
            append_to_json_file(all_results, partial_output)
            print(f"Saved {len(all_results)} partial records to {partial_output}")
def merge_json_files(input_files: List[str], output_file: str):
    """Merge multiple JSON files into a single file, keeping output as an array of records and per record is a line"""
    all_records = []
    total_records = 0
    
    for file in input_files:
        if os.path.exists(file) and os.path.getsize(file) > 0:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_records.extend(data)
                        records_added = len(data)
                        total_records += records_added
                        print(f"Added {records_added} records from {file}")
                    else:
                        print(f"Warning: {file} does not contain a list. Skipping.")
            except json.JSONDecodeError:
                print(f"Warning: Could not parse JSON in {file}. Skipping.")
            except Exception as e:
                print(f"Error processing {file}: {str(e)}. Skipping.")
    
    # Write each record on its own line
    try:
        with open(output_file, 'w') as out_f:
            for record in all_records:
                out_f.write(json.dumps(record) + '\n')
        print(f"Merged {total_records} total records into {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {str(e)}")
        # Try to write to an alternative file
        alt_output = f"{output_file}.backup.json"
        try:
            with open(alt_output, 'w') as out_f:
                for record in all_records:
                    out_f.write(json.dumps(record) + '\n')
            print(f"Saved to alternative file: {alt_output}")
        except Exception as backup_err:
            print(f"Failed to save backup: {str(backup_err)}")
    
    return total_records

def main():
    """Main function to distribute work across processes"""
    if len(sys.argv) < 2:
        print("Usage: python main.py <numOfLines>")
        sys.exit(1)
    
    num_of_lines = int(sys.argv[1])
    print(f"Processing a total of {num_of_lines} market IDs using {NUM_PROCESSES} processes")
    
    # Read market IDs from file
    market_ids = read_market_ids('market_id.txt')
    
    # Adjust num_of_lines if it's greater than the number of available market IDs
    num_of_lines = min(num_of_lines, len(market_ids))
    
    # Calculate the range for each process
    chunk_size = num_of_lines // NUM_PROCESSES
    
    mile_stones = ["0", "0", "0", "0", "0", "0", "0", "0"]
    # Prepare process arguments
    process_args = []
    for i in range(NUM_PROCESSES):
        start_idx = i * chunk_size
        
        # For the last process, include any remaining lines
        if i == NUM_PROCESSES - 1:
            end_idx = num_of_lines - 1
        else:
            end_idx = (i + 1) * chunk_size - 1
        
        output_file = f"price_{i+1}.json"
        process_args.append((start_idx, end_idx, market_ids, output_file, mile_stones[i]))
    
    # Start processes
    processes = []
    for args in process_args:
        p = multiprocessing.Process(target=worker_process, args=args)
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()

    
    print("All processes completed. Merging results...")
    
    # Merge all JSON files into a single file
    input_files = [f"price_{i+1}.json" for i in range(NUM_PROCESSES)]
    print('input_files', input_files)
    total_records = merge_json_files(input_files, "price.json")
    
    print(f"Data collection complete. Total records: {total_records}")

if __name__ == "__main__":
    # main()
    merge_json_files(["price_1.json", "price_2.json", "price_3.json", "price_4.json", "price_5.json", "price_6.json"], "price.json")
    # append_to_json_file([], "price.json")
    # append_to_json_file([{"abc": "1", "xyz": {"tyu": 1}}, {"abc": "2", "xyz": {"tyu": 2}}], "price.json")
    # append_to_json_file([{"abc": "3", "xyz": {"tyu": 3}}, {"abc": "4", "xyz": {"tyu": 4}}], "price.json")

    