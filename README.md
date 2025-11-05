Data Science Advance Project
# Computer Vision OCR App

A lightweight, fully local OCR app that extracts text from images using Tesseract OCR, OpenCV, and Streamlit. Paste this entire content into README.md in your repository.

Features
- Local OCR processing using Tesseract
- Streamlit web interface for image upload and text extraction
- Simple setup and usage instructions for Windows

Prerequisites
- Python 3.9 or later
- 16 GB RAM recommended (works on lower RAM for small models)
- Tesseract OCR installed on your system (Windows instructions included)

Quick setup (Windows)
  1. Install Python and ensure python and pip are on PATH.
  2. Install Tesseract (Windows):
     - Download the Windows installer from the UB Mannheim builds:
       https://github.com/UB-Mannheim/tesseract/wiki
     - Run the installer and note the installation path (default: C:\Program Files\Tesseract-OCR\).
     - During installation, enable the option to add Tesseract to your system PATH if available.
     - Verify installation:
       Open a new Command Prompt and run:
         tesseract --version
       You should see Tesseract version information.

Project setup (one-time)
  1. Clone or create project folder and place app.py and chatbot.py as needed.
  2. Create and activate a virtual environment (recommended):
     Windows:
       python -m venv venv
       venv\Scripts\activate
     macOS / Linux:
       python3 -m venv venv
       source venv/bin/activate
  3. Install Python dependencies:
     pip install streamlit opencv-python pytesseract Pillow numpy

Run the app
  1. Ensure Tesseract is installed and reachable (either in PATH or configured via pytesseract.pytesseract.tesseract_cmd).
  2. Activate your Python environment.
  3. Start Streamlit:
     streamlit run app.py
  4. Open the URL printed by Streamlit (usually http://localhost:8501).

File structure
  Chatbot-OCR/
  ├── app.py
  └── requirements.txt

## Contributing
Contributions are welcome!
Feel free to fork the repository, improve the game, and open a pull request. Let's grow this classic game together!

## License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## Author
**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)


