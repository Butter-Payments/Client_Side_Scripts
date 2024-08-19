# Stripe Object Downloader

This program is designed to export data from your stripe instance to a local file system for historical analysis.


# Setup

Stripe download libraries are defined in *butter_downloaders-1.0.0.tar.gz*

Before running, please run `pip install butter_downloaders-1.0.0.tar.gz`

## Configuration

The python file `StripeObjectDownload.py` contains configuration that determine how much and what to download:

Set the date range for the download, we recommend the past year and 2 months
`from_date  =  "2024-01-01"`
`to_date  =  "2024-01-02"`

Set the proper api_key and object_type

API key will come from your system. Object type can accept one of these values per run
 - "Coupon", 
 - "Customer", 
 - "Dispute", 
 - "Event", 
 - "Invoice", 
 - "PaymentIntent",
 -  "Payout", 
 - "Plan",
 - "Price", 
 - "Product", 
 - "Refund",
 - "Subscription"

downloader  = StripeDownloader(
	`api_key="xxxx",'`
    `object_type="Charge",`
)

We recommend pulling the following minimum data set:
Dispute, Invoice, PaymentIntent, Plan, Price, Refund, Subscription

Your implementation may vary so please confirm with the Butter team.

## Running the downloader

`python StripeObjectDownload.py` after installing the above dependencies will create files of the specified type for time periods under this installation root `<application_home>/files` folder.
For example:

> python StripeObjectDownload.py
Downloading from 2024-01-01T00:00:00 to 2024-01-01T02:00:00
files/transactions_1704085200_1704092400.jsonl.gz
Downloading from 2024-01-01T02:00:00 to 2024-01-01T04:00:00
files/transactions_1704092400_1704099600.jsonl.gz
Downloading from 2024-01-01T04:00:00 to 2024-01-01T06:00:00
files/transactions_1704099600_1704106800.jsonl.gz