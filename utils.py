from dotenv import load_dotenv
import os

# Load the .env file explicitly
load_dotenv()

# Fetch the SEC_API_KEY
SEC_API_KEY = os.getenv("SEC_API_KEY")
if not SEC_API_KEY:
    raise ValueError("SEC_API_KEY is missing! Check your .env file.")
