from fetchers import fetch_tenq_report
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.schema import Document  # Import Document class
from langchain_community.llms import OpenAI

def summarize_tenq(ticker):
    extracted_text, metadata = fetch_tenq_report(ticker)
    
    # Wrap the extracted text in a Document object
    document = Document(page_content=extracted_text, metadata=metadata)
    
    prompt_template = "Summarize the following 10-Q document:\n\n{input_documents}"
    summarize_chain = load_summarize_chain(
        OpenAI(temperature=0),
        chain_type="stuff",
        prompt=PromptTemplate(template=prompt_template),
        document_variable_name="input_documents",
    )
    return summarize_chain.invoke({"input_documents": [document]})  # Pass the Document object

def ask_about_tenq(ticker, question):
    extracted_text, metadata = fetch_tenq_report(ticker)
    
    # Wrap the extracted text in a Document object
    document = Document(page_content=extracted_text, metadata=metadata)
    
    prompt_template = "Context:\n{input_documents}\n\nQuestion: {question}\n\nAnswer:"
    summarize_chain = load_summarize_chain(
        OpenAI(temperature=0),
        chain_type="stuff",
        prompt=PromptTemplate(template=prompt_template),
        document_variable_name="input_documents",
    )
    return summarize_chain.invoke({"input_documents": [document], "question": question})
