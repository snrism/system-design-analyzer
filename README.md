# System Design Review App

## Overview

The Engineering system design Review App is a Streamlit-based application that allows users to upload design document files from Google Cloud Storage (GCS) and receive AI-generated feedback on the content. This tool leverages the Anthropic API to analyze the text and provide insights, making it useful for quick document reviews, content analysis, or as a starting point for more in-depth document processing workflows.

## Features

- Input PDF files via Google Cloud Storage paths
- Extract text from PDF documents
- Generate AI-powered feedback using the Anthropic API
- User-friendly interface built with Streamlit

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.7 or higher
- A Google Cloud Platform (GCP) account with a project set up
- An Anthropic API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/system-design-analyzer.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Cloud credentials:
   - Create a service account in your GCP project
   - Download the JSON key file
   - Place the key file in a secure location

4. Set up your Anthropic API key:
   - Sign up for an Anthropic account and obtain an API key
   - Set the API key as an environment variable or update it in the script

## Configuration

1. Open `design-reviewer.py` and update the following:
   - Replace `"your_anthropic_api_key_here"` with your actual Anthropic API key
   - Update the path to your GCP service account key file:
     ```python
     credentials = service_account.Credentials.from_service_account_file('path/to/your/service-account-key.json')
     ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run pdf_review_app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Enter the GCS path of your PDF file in the format `gs://your-bucket/your-file.pdf`

4. Click "Get Feedback" to process the PDF and receive AI-generated feedback

## Limitations

- The current implementation is limited to processing the first 100,000 characters of the PDF
- Very large PDFs may cause performance issues or exceed API limits
- The quality of the feedback depends on the capabilities of the Anthropic AI model

## Contributing

Contributions to improve the PDF Review App are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

[Insert your chosen license here, e.g., MIT License, Apache 2.0, etc.]

## Acknowledgments

- This project uses the Streamlit framework for the user interface
- PDF text extraction is performed using PyPDF2
- AI-powered feedback is generated using the Anthropic API
- Google Cloud Storage is used for file storage and retrieval