# Polymarket Data Crawler

This script crawls market data from the Polymarket API and exports it to an Excel file.

## Requirements

- Python 3.7+
- Required packages listed in `requirements.txt`

## Installation

Install required packages:

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies (order matters for NumPy and Pandas compatibility)
pip install -r requirements.txt
```

## Troubleshooting

If you encounter NumPy/Pandas compatibility errors like:
```
ValueError: numpy.dtype size changed, may indicate binary incompatibility
```

Try reinstalling the packages in this specific order:
```bash
pip uninstall -y numpy pandas
pip install numpy==1.24.3
pip install pandas==2.1.1
pip install openpyxl tqdm requests
```

## Usage

Run the script:

```bash
python main.py
```

The script will:
1. Fetch data from Polymarket API in batches of 100 records
2. Extract the required fields for each market
3. Export the data to an Excel file named `polymarket_data.xlsx`

## Output Data

The Excel file contains the following columns for each market:
- id
- slug
- startDate
- endDate
- volume
- liquidity
- description
- event_title
- event_slug
- event_description
- series_title
- series_slug 