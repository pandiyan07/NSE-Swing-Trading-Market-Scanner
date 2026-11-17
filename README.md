# Project Title

**Swing Trading Market Scanner**

## Table of Contents

-   About The Project
-   Built With
-   Key Features
-   Getting Started
-   Technologies Used (Prerequisites)
-   Installation
-   Usage
-   Project Structure
-   How It Works
-   Main Python Functions
-   Configuration
-   Future Enhancements
-   License Description
-   Disclaimer

## About The Project

This project is a multiprocessing-based swing trading scanner for Indian
equities. It combines Yahoo Finance, NSELive (Jugaad Data), and NSELib
data to identify abnormal volume activity, stocks near weekly highs/lows
(ORB), recent block and bulk deals, and generates ranked tables for
swing trading opportunities. The scanner processes a large watchlist in
parallel and consolidates the results into Pandas DataFrames.

### Built With

-   Python 3
-   yfinance
-   pandas
-   jugaad-data
-   nselib
-   multiprocessing

### Key Features

-   Historical EOD volume analysis
-   Weekly and monthly volume spike detection
-   ORB percentage calculation using weekly high/low
-   Block deal analysis
-   Bulk deal analysis
-   Yahoo Finance integration
-   NSELive integration
-   Parallel processing
-   Automatic retry on network failures
-   Ranked output tables

## Getting Started

### Technologies Used (Prerequisites)

-   Python 3.10+
-   Internet connection
-   pip

Required packages:

``` bash
pip install pandas yfinance nselib jugaad-data
```

### Installation

``` bash
git clone https://github.com/yourusername/swing-trading-scanner.git
cd swing-trading-scanner
pip install -r requirements.txt
python "SWING trading v1.py"
```

## Usage

Run the script to download market data, analyze all configured stocks,
and generate console tables for: - Volume spikes - ORB ranking - Block
deals - Bulk deals

## Project Structure

``` text
SWING trading v1.py
│
├── Watchlist Configuration
├── Yahoo Finance Downloader
├── NSELive Data Fetcher
├── ORB Calculator
├── Volume Spike Detector
├── Block/Bulk Deal Analyzer
├── Multiprocessing Engine
└── Output Table Generator
```

## How It Works

1.  Initialize watchlist and multiprocessing objects.
2.  Download block and bulk deal reports.
3.  Split stocks across CPU cores.
4.  Download historical OHLCV data.
5.  Fetch weekly high/low from NSE.
6.  Compute ORB percentage.
7.  Detect abnormal weekly and monthly volume spikes.
8.  Aggregate block and bulk deal quantities.
9.  Merge results from worker processes.
10. Build ranked DataFrames.
11. Display ORB, volume spike, block deal and bulk deal tables.

## Main Python Functions

  Function                     Description
  ---------------------------- -------------------------------------------------------
  `JUGAAD_DATA()`              Retrieves weekly high/low data from NSELive.
  `FETCHER()`                  Retries failed NSE requests.
  `ORB()`                      Calculates proximity to weekly high/low.
  `DATA_FETCHER()`             Coordinates Yahoo Finance and NSELive processing.
  `OUTPUT_CALCULATOR()`        Records abnormal volume events.
  `ABNORMAL_VOLUME_FINDER()`   Detects weekly/monthly volume spikes.
  `WEEKLY_AVERAGE()`           Weekly volume analysis.
  `MONTHLY_AVERAGE()`          Monthly volume analysis.
  `ONE_DATA_DOWNLOADER()`      Downloads OHLCV data for all stocks.
  `THE_MAIN()`                 Executes complete analysis pipeline for each process.

## Configuration

-   Editable watchlist
-   Weekly/monthly volume thresholds
-   Multiprocessing support
-   Retry logic for network failures

## Future Enhancements

-   RSI and moving-average filters
-   52-week high scanner
-   Pre-market scanner
-   Flask dashboard integration
-   Excel/CSV export
-   TradingView alerts

## License Description

Recommended: MIT License.

Permission is granted to use, modify, distribute and commercialize the
software while retaining the copyright notice.

## Disclaimer

This project is intended for educational and research purposes only. It
does not constitute investment advice. Verify all trading decisions
independently before live trading.
