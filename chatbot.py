import streamlit as st
from openai import OpenAI

# Predefined responses
responses = {
    "What does the eligibility verification agent (EVA) do?": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}
# Function to get a response
def get_response(question):
    if question in responses:
        return responses[question]
    else:
        return get_llm_response(question)

# Fallback to LLM response
def get_llm_response(question):
    # Use an LLM API like OpenAI or another to get a generic response
    response = OpenAI.query(question)
    return response

# Streamlit app
st.title("Thoughtful AI Customer Support")
user_input = st.text_input("Ask a question about Thoughtful AI:")

if user_input:
    answer = get_response(user_input)
    st.write("Answer:", answer)