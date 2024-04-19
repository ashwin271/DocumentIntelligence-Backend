## Document Intelligence - Backend

This document provides instructions for setting up and running the backend component of the Document Intelligence project.

**Prerequisites**

- Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- pip (usually comes bundled with Python)

**Installation**

1. **Configure API and Install Dependencies:**

   - Run the following command in your terminal:

     ```bash
     python setup.py
     ```

   - This script will handle API configuration and dependency installation.
   - Alternatively, to manually install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

2. **Obtain Gemini API Key:**

   - Access the Gemini API key from Google AI Studio: [aistudio.google.com](https://aistudio.google.com).
   - To gain access to Google AI Studio, you'll need to accept the terms and conditions from either:
     - Google Cloud Console: [console.cloud.google.com](https://console.cloud.google.com)
     - Google Vertex AI: [console.cloud.google.com/vertex-ai](https://console.cloud.google.com/vertex-ai)

3. **Install and Configure Tesseract-OCR:**

   - Download and install Tesseract-OCR from [github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki).
     - The version used during development was [tesseract-ocr-w64-5.3.3.20231005](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe)
   - Follow the installation instructions on the Tesseract-OCR GitHub repository (link provided above).
   - Ensure Tesseract-OCR is added to your system's PATH environment variable. For Windows users, the default path might be:

     ```
     C:\Program Files\Tesseract-OCR
     ```

   - You can verify the installation by running `tesseract --version` in your terminal. If Tesseract-OCR is not found, adjust your PATH environment variable accordingly.

**Running the Backend**

1. Navigate to the `backend` folder within your project directory.
2. Start the server by running the following command:

   ```bash
   python backend.py
   ```

This will initiate the Document Intelligence backend server.
