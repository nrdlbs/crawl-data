# Polymarket API Data Extraction Project

## API Endpoint
The Polymarket API provides data about events and markets. Below is a sample endpoint:

```http
GET https://gamma-api.polymarket.com/events?limit=1&offset=10000
```

## Sample Response
The API returns data in JSON format. Here's a sample response:

```json
[
    {
        "id": "18007",
        "ticker": "cbb-psu-ucla-2025-02-08",
        "slug": "cbb-psu-ucla-2025-02-08",
        "title": "Penn State vs. UCLA",
        "description": "In the upcoming CBB game, scheduled for February 8 at 4:00PM ET:\nIf the Penn State win, the market will resolve to "Penn State".\nIf the UCLA win, the market will resolve to "UCLA".\nIf the game is postponed, this market will remain open until the game has been completed.\nIf the game is canceled entirely, with no make-up game, this market will resolve 50-50.",
        "startDate": "2025-02-08T07:15:46.417639Z",
        "creationDate": "2025-02-08T21:00:00Z",
        "endDate": "2025-02-08T21:00:00Z",
        "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/ncaab1.png",
        "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/ncaab1.png",
        "active": true,
        "closed": true,
        "archived": false,
        "new": false,
        "featured": false,
        "restricted": true,
        "liquidity": 0,
        "openInterest": 0,
        "createdAt": "2025-02-08T07:12:19.157172Z",
        "updatedAt": "2025-02-09T02:54:17.699201Z",
        "competitive": 0,
        "volume1wk": 0,
        "volume1mo": 0,
        "volume1yr": 0,
        "enableOrderBook": true,
        "liquidityAmm": 0,
        "liquidityClob": 0,
        "negRisk": false,
        "commentCount": 0,
        "markets": [
            {
                "id": "522328",
                "question": "Penn State vs. UCLA",
                "conditionId": "0x8603ec82b8d9385c3b280d69fe393c4241da036f7c6eb6f8f95a3794d1add2c8",
                "slug": "cbb-psu-ucla-2025-02-08",
                "resolutionSource": "https://www.ncaa.com/",
                "endDate": "2025-02-15T21:00:00Z",
                "liquidity": "0",
                "startDate": "2025-02-08T07:14:42.019982Z",
                "fee": "20000000000000000",
                "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/ncaab1.png",
                "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/ncaab1.png",
                "description": "In the upcoming CBB game, scheduled for February 8 at 4:00PM ET:\nIf the Penn State win, the market will resolve to "Penn State".\nIf the UCLA win, the market will resolve to "UCLA".\nIf the game is postponed, this market will remain open until the game has been completed.\nIf the game is canceled entirely, with no make-up game, this market will resolve 50-50.",
                "outcomes": "[\"Penn State\", \"UCLA\"]",
                "outcomePrices": "[\"0\", \"1\"]",
                "active": true,
                "closed": true,
                "marketMakerAddress": "0x33A8c2f83a087677F4dE20D97E65dFF727b73a55",
                "createdAt": "2025-02-08T07:12:19.343859Z",
                "updatedAt": "2025-02-09T02:54:17.694745Z",
                "closedTime": "2025-02-09 02:50:05+00",
                "wideFormat": true,
                "new": true,
                "sentDiscord": true,
                "archived": false,
                "resolvedBy": "0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74",
                "restricted": true,
                "groupItemTitle": "Penn State vs. UCLA",
                "questionID": "0x7411ed2526a3d73b91da15c61918febe61cb219b6cc435ac5cf124b1f1d17ab5",
                "umaEndDate": "2025-02-09T02:50:05Z",
                "enableOrderBook": true,
                "orderPriceMinTickSize": 0.001,
                "orderMinSize": 5,
                "umaResolutionStatus": "resolved",
                "liquidityNum": 0,
                "endDateIso": "2025-02-15",
                "startDateIso": "2025-02-08",
                "hasReviewedDates": true,
                "readyForCron": false,
                "volume1wk": 0,
                "volume1mo": 0,
                "volume1yr": 0,
                "gameStartTime": "2025-02-08 21:00:00+00",
                "secondsDelay": 3,
                "clobTokenIds": "[\"113023474901647011498361902149718134685741058978167627570944185996798261802309\", \"12809409563306826550512441154195843217337351603252186024870400514900864241161\"]",
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
                "acceptingOrdersTimestamp": "2025-02-08T07:13:34Z",
                "cyom": false,
                "competitive": 0,
                "pagerDutyNotificationEnabled": false,
                "approved": true,
                "rewardsMinSize": 0,
                "rewardsMaxSpread": 0,
                "spread": 0.01,
                "automaticallyResolved": true,
                "oneHourPriceChange": 0,
                "oneWeekPriceChange": 0,
                "oneMonthPriceChange": 0,
                "oneYearPriceChange": 0,
                "bestAsk": 0.01,
                "automaticallyActive": true,
                "clearBookOnStart": true,
                "manualActivation": false,
                "negRiskOther": false,
                "umaResolutionStatuses": "[]",
                "pendingDeployment": false,
                "deploying": false
            }
        ],
        "series": [
            {
                "id": "10012",
                "ticker": "ncaab",
                "slug": "ncaab",
                "title": "NCAAB",
                "seriesType": "single",
                "recurrence": "daily",
                "image": "https://sg-images-bucket.nyc3.cdn.digitaloceanspaces.com/wp-content/uploads/2024/06/NCAAB.png",
                "icon": "https://sg-images-bucket.nyc3.cdn.digitaloceanspaces.com/wp-content/uploads/2024/06/NCAAB.png",
                "active": true,
                "closed": false,
                "archived": false,
                "featured": false,
                "restricted": true,
                "createdAt": "2025-01-30T21:38:35.238967Z",
                "updatedAt": "2025-04-23T12:58:24.210241Z",
                "commentCount": 7
            }
        ],
        "tags": [
            {
                "id": "1",
                "label": "Sports",
                "slug": "sports",
                "forceShow": false,
                "publishedAt": "2023-10-24 22:37:50.296+00",
                "updatedBy": 15,
                "createdAt": "2023-10-24T22:37:50.31Z",
                "updatedAt": "2024-07-05T21:07:21.800664Z",
                "forceHide": true
            },
            {
                "id": "101178",
                "label": "CBB",
                "slug": "cbb",
                "createdAt": "2024-11-04T20:09:35.892479Z"
            },
            {
                "id": "100639",
                "label": "Games",
                "slug": "games",
                "forceShow": false,
                "createdAt": "2024-09-23T22:41:37.670714Z"
            }
        ],
        "cyom": false,
        "closedTime": "2025-02-09T02:50:05Z",
        "showAllOutcomes": false,
        "showMarketImages": true,
        "automaticallyResolved": true,
        "enableNegRisk": false,
        "automaticallyActive": true,
        "eventDate": "2025-02-08",
        "startTime": "2025-02-08T21:00:00Z",
        "eventWeek": 14,
        "seriesSlug": "ncaab",
        "period": "FT",
        "live": false,
        "ended": true,
        "negRiskAugmented": false,
        "pendingDeployment": false,
        "deploying": false
    }
]
```

## Data Retrieval Strategy
- Fetch records in batches of 100 per request
- Process each batch and continue until all data is retrieved

## Data Model
The data follows this entity relationship:
- **Market** (n) → **Event** (1)
- **Event** (n) → **Series** (1)

## Required Data Fields
For each market, extract the following attributes (use null if data is not available):

| Field | Description |
|-------|-------------|
| id | Market ID |
| slug | Market slug |
| startDate | Start date of the market |
| endDate | End date of the market |
| volume | Trading volume |
| liquidity | Available liquidity |
| description | Market description |
| event_title | Title of the parent event |
| event_slug | Slug of the parent event |
| event_description | Description of the parent event |
| series_title | Title of the series |
| series_slug | Slug of the series |

## Project Objective
Create a Python script (main.py) that:
1. Crawls the Polymarket API data
2. Extracts the required fields for each market
3. Exports the data to an Excel file


