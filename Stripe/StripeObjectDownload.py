## Before running, please run `pip install butter_downloaders-1.0.0.tar.gz`

from datetime import datetime, timedelta
from typing import List, Tuple
from butter_downloaders.downloaders.stripe_downloader import StripeDownloader
from butter_downloaders.exporters.local_exporter import LocalExporter

ISO_DATE_FORMAT = "%Y-%m-%d"

def split_dates(
    starting_date: str, ending_date: str, time_delta: timedelta
) -> List[Tuple[str, str]]:
    """
    Splits beginning date and ending date window into single day increments.
    :param starting_date: Starting Date (Inclusive)
    :param ending_date: Ending Date (Exclusive)
    :param time_delta: Window Size
    :return: List of tuple pairings
    """
    return_list = []
    start_datetime = datetime.strptime(starting_date, ISO_DATE_FORMAT)
    end_datetime = datetime.strptime(ending_date, ISO_DATE_FORMAT)
    from_datetime = start_datetime
    to_datetime = start_datetime + time_delta
    while from_datetime != end_datetime:
        return_list.append((from_datetime.isoformat(), to_datetime.isoformat()))
        from_datetime = to_datetime
        to_datetime = from_datetime + time_delta
    return return_list

# Set the date range for the download, we recommend the past year and 2 months
from_date = "2024-01-01"
to_date = "2024-01-02"

# Please replace <INSERT STRIPE API KEY> with your actual Stripe API key
downloader = StripeDownloader(
    api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc",
    # Valid object types here are: "Charge", "Coupon", "Customer", "Dispute", "Event", "Invoice", "PaymentIntent", "Payout", "Plan", "Price", "Product", "Refund", "Subscription"
    object_type="Dispute",
)

downloader.connect()

# Local exporter will write each batch to a zipped JSON file within the ./files directory
exporter = LocalExporter()

# This value will set the granularity with which to download data. We recommend 2 hour intervals to keep the payloads small
time_delta = timedelta(minutes=120)

period_tuples = split_dates(from_date, to_date, time_delta)
for from_datetime, to_datetime in period_tuples:
    results = downloader.download(from_datetime, to_datetime)
    exporter.write_batch(from_datetime, to_datetime, results)

# After the download is complete, you can upload the ./files directory in it's entirety to the Butter S3 bucket