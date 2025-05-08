# Polymarket API Data Extraction Project

## API Endpoint get market by id: API 1

### Endpoint
```
curl --location 'https://gamma-api.polymarket.com/markets/:id'
```
### Response
```json
{
    "id": "531492",
    "question": "Over 239.5",
    "conditionId": "0x834e57936657ae5ddaea6d9e18ee780d04d588018ab6b9b18a44cc5317e5f6f2",
    "slug": "nba-mem-okc-2025-03-27-total-239pt5",
    "resolutionSource": "https://www.nba.com/",
    "endDate": "2025-04-04T00:00:00Z",
    "liquidity": "0",
    "startDate": "2025-03-27T00:23:18.481638Z",
    "fee": "20000000000000000",
    "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/super+cool+basketball+in+red+and+blue+wow.png",
    "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/super+cool+basketball+in+red+and+blue+wow.png",
    "description": "In the upcoming NBA game, scheduled for March 27 at 8:00PM ET:\nIf the total score of the game is less than or equal to the line 239, the market will resolve to \"Under\".\nElse, the market will resolve to \"Over\".\nIf the game is canceled entirely, with no make-up game, this market will resolve 50-50.",
    "outcomes": "[\"Over\", \"Under\"]",
    "outcomePrices": "[\"0\", \"1\"]",
    "active": true,
    "closed": true,
    "marketMakerAddress": "",
    "createdAt": "2025-03-27T00:20:21.718786Z",
    "updatedAt": "2025-03-28T04:35:27.631217Z",
    "closedTime": "2025-03-28 04:34:20+00",
    "wideFormat": true,
    "new": true,
    "sentDiscord": true,
    "archived": false,
    "resolvedBy": "0xb21182d0494521Cf45DbbeEbb5A3ACAAb6d22093",
    "restricted": true,
    "groupItemTitle": "Over 239.5",
    "questionID": "0x4f4598cf6af36ca9540c66e35a0ca0ac1f10f31d53c6d5b2f2e040096ea50941",
    "umaEndDate": "2025-03-28T04:34:20Z",
    "enableOrderBook": true,
    "orderPriceMinTickSize": 0.01,
    "orderMinSize": 5,
    "umaResolutionStatus": "resolved",
    "liquidityNum": 0,
    "endDateIso": "2025-04-04",
    "startDateIso": "2025-03-27",
    "hasReviewedDates": true,
    "readyForCron": false,
    "volume1wk": 0,
    "volume1mo": 0,
    "volume1yr": 0,
    "gameStartTime": "2025-03-28 00:00:00+00",
    "secondsDelay": 3,
    "clobTokenIds": "[\"111921395645355300487518569145849548118782457875824781317525262592604421091895\", \"63900173641965756847547093054309931316785483274507634668979439177621966623897\"]",
    "fpmmLive": true,
    "volume1wkAmm": 0,
    "volume1moAmm": 0,
    "volume1yrAmm": 0,
    "volume1wkClob": 0,
    "volume1moClob": 0,
    "volume1yrClob": 0,
    "liquidityAmm": 0,
    "liquidityClob": 0,
    "acceptingOrders": false,
    "negRisk": false,
    "notificationsEnabled": false,
    "ready": false,
    "funded": false,
    "acceptingOrdersTimestamp": "2025-03-27T00:22:09Z",
    "cyom": false,
    "competitive": 0,
    "pagerDutyNotificationEnabled": false,
    "approved": true,
    "rewardsMinSize": 0,
    "rewardsMaxSpread": 0,
    "spread": 0.99,
    "automaticallyResolved": true,
    "oneDayPriceChange": -0.005,
    "oneHourPriceChange": 0,
    "oneWeekPriceChange": 0,
    "oneMonthPriceChange": 0,
    "oneYearPriceChange": 0,
    "bestAsk": 0.99,
    "automaticallyActive": true,
    "clearBookOnStart": true,
    "manualActivation": false,
    "negRiskOther": false,
    "gameId": "0x89c8b43e447b7cc907aa780b7019bc9c9a19b979c5c8aa372c167636c3f301cd",
    "sportsMarketType": "totals",
    "line": 239.5,
    "umaResolutionStatuses": "[]",
    "pendingDeployment": false,
    "deploying": false
}
``` 

## API get market by condition id: API 2

###Endpoint
```
curl --location 'https://clob.polymarket.com/markets/:condition_id
```

### Response
```json
{
    "enable_order_book": false,
    "active": true,
    "closed": true,
    "archived": false,
    "accepting_orders": false,
    "accepting_order_timestamp": "2025-04-18T15:20:03Z",
    "minimum_order_size": 5,
    "minimum_tick_size": 0.001,
    "condition_id": "0x396cff35d0089be0dd7a31c3dd8893dba91087cb204f36fd596ea8e176c8194f",
    "question_id": "0x0d3ecb119ebc29f6f40017ac97c2564aef5bebea98817d0c64ce7aedc7de1500",
    "question": "Will the price of Bitcoin be greater than $89000 on Apr 25?",
    "description": "This market will resolve according to the final \"Close\" price of the Binance 1 minute candle for BTCUSDT 25 Apr '25 12:00 in the ET timezone (noon). Otherwise, this market will resolve to \"No\".\n\nThe resolution source for this market is Binance, specifically the BTCUSDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar.\n\nIf the reported value falls exactly between two brackets, then this market will resolve to the higher range bracket.\n\nPlease note that this market is about the price according to Binance BTCUSDT, not according to other sources or spot markets.",
    "market_slug": "will-the-price-of-bitcoin-be-greater-than-89000-on-apr-25",
    "end_date_iso": "2025-04-25T00:00:00Z",
    "game_start_time": null,
    "seconds_delay": 0,
    "fpmm": "",
    "maker_base_fee": 0,
    "taker_base_fee": 0,
    "notifications_enabled": true,
    "neg_risk": true,
    "neg_risk_market_id": "0x0d3ecb119ebc29f6f40017ac97c2564aef5bebea98817d0c64ce7aedc7de1500",
    "neg_risk_request_id": "0x7fa7eb8bd7827b336929b9ec82a4568d498ef5bd40240fe246928ba64624a9c8",
    "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/btc+moon+explode+psychedelic.png",
    "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/btc+moon+explode+psychedelic.png",
    "rewards": {
        "rates": [
            {
                "asset_address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                "rewards_daily_rate": 5
            }
        ],
        "min_size": 100,
        "max_spread": 3.5
    },
    "is_50_50_outcome": false,
    "tokens": [
        {
            "token_id": "56301394996158099288337148092833602815489233233695788581935629307696915237267",
            "outcome": "Yes",
            "price": 1,
            "winner": true
        },
        {
            "token_id": "24020800886044361928297303482313439338060103716147186009149855318565271604084",
            "outcome": "No",
            "price": 0,
            "winner": false
        }
    ],
    "tags": [
        "Crypto",
        "Bitcoin",
        "Crypto Prices",
        "Recurring"
    ]
}
```

## API get history price of token: API 3 (when call this api interval=1 and fidelity = 10 always)
### Endpoint
```
curl --location 'https://clob.polymarket.com/prices-history?interval=1m&market=111921395645355300487518569145849548118782457875824781317525262592604421091895&fidelity=10'
```
### Response
```json
{
    "history": [
        {
            "t": 1743036005,
            "p": 0.5
        },
        {
            "t": 1743036605,
            "p": 0.5
        },
        {
            "t": 1743037206,
            "p": 0.5
        },
        {
            "t": 1743037805,
            "p": 0.5
        },
        {
            "t": 1743038405,
            "p": 0.5
        },
        {
            "t": 1743039005,
            "p": 0.5
        },
        {
            "t": 1743039605,
            "p": 0.5
        },
        {
            "t": 1743040206,
            "p": 0.5
        },
        {
            "t": 1743040805,
            "p": 0.5
        },
        {
            "t": 1743041405,
            "p": 0.5
        },
        {
            "t": 1743042006,
            "p": 0.5
        },
        {
            "t": 1743042606,
            "p": 0.5
        },
        {
            "t": 1743043206,
            "p": 0.5
        },
        {
            "t": 1743043806,
            "p": 0.5
        },
        {
            "t": 1743044406,
            "p": 0.5
        },
        {
            "t": 1743045006,
            "p": 0.5
        },
        {
            "t": 1743045605,
            "p": 0.5
        },
        {
            "t": 1743046206,
            "p": 0.5
        },
    ]
}
```

## Workflow
- Read market_id from market_id.txt (loop ordered by DESC and break the loop when get history price response is empty. I think that if bigger market_id can't get history, smaller market_id can't do too) 
- Call API 1 to get condition_id
- Call API 2 to get token 
- Call API 3 to get history with every token

- From data of three apis we make the tuple including fields: token_id, outcome, price, market_id, market_slug, history_price(type is array of {t, p}) 

## Multiprocessing Implementation
Note 1: If response of api have error code, missing filed in response or history_price is empty, you should be continue and call next martket_id 
Note 2: The `market_id.txt` file contains too many market IDs (45712), so you should implement task of asyncio in `main.py` to distribute the workload across 6 task:

The `main.py` script should accept a parameter `numOfLines` and distribute the workload across 6 processes:

| Task | Market ID Range | Output File |
|---------|----------------|-------------|
| Task 1 | Line 1 to line (numOfLines/6) | `price_1.json` |
| Task 2 | Line (numOfLines/6 + 1) to line (numOfLines/6 * 2) | `price_2.json` |
| Task 3 | Line (numOfLines/6 * 2 + 1) to line (numOfLines/6 * 3) | `price_3.json` |
| Task 4 | Line (numOfLines/6 * 3 + 1) to line (numOfLines/6 * 4) | `price_4.json` |
| Task 5 | Line (numOfLines/6 * 4 + 1) to line (numOfLines/6 * 5) | `price_5.json` |
| Task 6 | Line (numOfLines/6 * 5 + 1) to line numOfLines | `price_6.json` |

Each Task will export its results as an array of records to its respective output file. Per record is wrote only a  line

- After crawl full records and export to multiple file price_x.json. Read from them to union all to `price.json`'
- My OS is MacOS
