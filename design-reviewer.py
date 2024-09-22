import streamlit as st
import PyPDF2
import io
import anthropic
from google.cloud import storage
from google.oauth2 import service_account

# Set your Anthropic API key
ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_KEY"

# Set up GCS client
credentials = service_account.Credentials.from_service_account_file('YOUR_GCP_SERVICE_CREDENTIALS.json')
storage_client = storage.Client(credentials=credentials)

def download_pdf_from_gcs(gcs_path):
    bucket_name, blob_name = gcs_path.replace("gs://", "").split("/", 1)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    pdf_contents = blob.download_as_bytes()
    return io.BytesIO(pdf_contents)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_feedback(text):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.completions.create(
        model="claude-2.1",
        prompt=f"Human: Please review the following engineering design document and review for functional design requirements, production considerations, scaling to millions of users and follow best practices:\n\n{text}\n\nAssistant: Here is my feedback on the engineering design document:",
        max_tokens_to_sample=1000
    )
    return response.completion

st.title("Engineering Design Review App")

gcs_path = st.text_input("Enter the GCS path of the PDF file (e.g., gs://your-bucket/your-file.pdf)")

if gcs_path:
    if st.button("Get Feedback"):
        with st.spinner("Downloading and analyzing the PDF..."):
            try:
                pdf_file = download_pdf_from_gcs(gcs_path)
                text = extract_text_from_pdf(pdf_file)
                feedback = get_feedback(text[:100000])  # Limit to first 100,000 characters
                st.subheader("Feedback:")
                st.write(feedback)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")