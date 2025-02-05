AI-Powered Financial Chatbot
This Streamlit app uses SEC filings (10-K and 10-Q reports) to answer specific questions about public companies. It leverages LangChain, OpenAI's GPT API, and the SEC API to retrieve and summarize financial data.

Features
Fetches and summarizes 10-K and 10-Q filings.
Allows users to ask specific questions about filings.
Provides AI-generated answers based on filing content.

Installations
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Add a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
SEC_API_KEY=your_sec_api_key
USER_AGENT=your_application_name/1.0 (your_email@example.com)
Run the app:

Usage
Select a 10-K or 10-Q report.
Enter a stock ticker (e.g., AAPL, TSLA).
Ask a question (e.g., "What are the risk factors?").
Click Get Answer to retrieve the information.

Example Questions
AAPL 10-K: "What are Apple's risk factors?"
TSLA 10-Q: "What financial metrics does Tesla report for the quarter?"
Troubleshooting

Missing API Keys: Check your .env file.
No Filings Found: Verify the stock ticker or report availability.
Context Limit Exceeded: Try rephrasing or narrowing your query.
