MEDICAL CHATBOT - PRESCRIPTION READER & VIRTUAL ASSISTANT
==========================================================

This project is a Medical Chatbot that helps patients by reading prescriptions from doctors,
diagnosing them, and providing relevant health information in an interactive chat format.
The system uses Natural Language Processing (NLP), Optical Character Recognition (OCR),
and conversational AI to assist patients in understanding their prescriptions and conditions.

----------------------------------------------------------
FEATURES
----------------------------------------------------------
- Extracts and reads medical prescriptions using OCR
- Identifies medicines, dosages, and health conditions
- Provides medical guidance and explanation of prescriptions
- Chatbot functionality for patient interaction
- Built with Python, Flask, NLP, and OCR libraries

----------------------------------------------------------
TECHNOLOGIES USED
----------------------------------------------------------
- Frontend   : HTML, CSS, JavaScript
- Backend    : Python (Flask / Django)
- OCR        : Tesseract OCR, OpenCV
- NLP        : NLTK / spaCy / Transformers
- Database   : SQLite / MySQL (optional)

----------------------------------------------------------
PROJECT STRUCTURE
----------------------------------------------------------
medical-chatbot/
│── static/               # CSS, JS, and image assets
│── templates/            # HTML templates
│── models/               # NLP/ML models
│── app.py                # Flask backend
│── requirements.txt      # Dependencies
│── README.txt            # Project documentation

----------------------------------------------------------
INSTALLATION & SETUP
----------------------------------------------------------
1. Clone the repository:
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot

2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate (Mac/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000

----------------------------------------------------------
DISCLAIMER
----------------------------------------------------------
This chatbot is for educational and informational purposes only.
It is NOT a replacement for professional medical advice, diagnosis,
or treatment. Always consult a doctor for serious medical concerns.

----------------------------------------------------------
AUTHOR
----------------------------------------------------------
Developed by: Amol Kantela
