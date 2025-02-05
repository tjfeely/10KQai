from dotenv import load_dotenv
import os
from sec_api import QueryApi

# Load the .env file explicitly
load_dotenv()

# Fetch the SEC_API_KEY
SEC_API_KEY = os.getenv("SEC_API_KEY")
if not SEC_API_KEY:
    raise ValueError("SEC_API_KEY is missing! Check your .env file.")

query_api = QueryApi(api_key=SEC_API_KEY)

def fetch_tenk_report(ticker):
    search_params = {
        "query": f"ticker:{ticker} AND formType:10-K",
        "from": "0",
        "size": "1",
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    response = query_api.get_filings(search_params)

    if response["filings"]:
        latest_filing = response["filings"][0]
        filing_url = latest_filing["linkToFilingDetails"]
        extracted_text = "Extracted text from the filing goes here."  # Replace with actual text extraction logic
        metadata = {
            "ticker": ticker,
            "company_name": latest_filing["companyName"],
            "form_type": latest_filing["formType"],
            "filed_at": latest_filing["filedAt"],
        }
        return extracted_text, metadata
    else:
        raise ValueError(f"No 10-K filings found for {ticker}.")

def fetch_tenq_report(ticker):
    search_params = {
        "query": f"ticker:{ticker} AND formType:10-Q",
        "from": "0",
        "size": "1",
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    response = query_api.get_filings(search_params)

    if response["filings"]:
        latest_filing = response["filings"][0]
        filing_url = latest_filing["linkToFilingDetails"]
        extracted_text = "Extracted text from the filing goes here."  # Replace with actual text extraction logic
        metadata = {
            "ticker": ticker,
            "company_name": latest_filing["companyName"],
            "form_type": latest_filing["formType"],
            "filed_at": latest_filing["filedAt"],
        }
        return extracted_text, metadata
    else:
        raise ValueError(f"No 10-Q filings found for {ticker}.")
