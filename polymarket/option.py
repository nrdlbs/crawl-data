from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON

def main():
    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=POLYGON,
    )

    market_id = "522328"

    tokens = client.get_tokens_by_market(market_id=market_id)
    for token in tokens:
        print(f"Token: {token['id']}, Name: {token['name']}, Ticker: {token['ticker']}")

if __name__ == "__main__":
    main()