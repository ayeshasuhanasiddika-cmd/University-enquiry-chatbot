# University Admission Enquiry Chatbot – Davanagere University,University
This is a web-based enquiry chatbot system developed using Dialogflow and Flask, designed specifically for  Davanagere University,University . The chatbot assists prospective MCA students with frequently asked queries related to admissions, courses, fees, placements, facilities, and more.

---

## 🎯 Project Objective

The objective of this project is to streamline the undergraduate admission enquiry process using an AI-powered chatbot. It provides instant, accurate, and consistent responses to commonly asked questions, thereby improving accessibility and user engagement.

---

## 🚀 Features

- Responds to queries about:
  - Available BTech courses and specializations
  - Direct Second Year (DSE) admissions
  - Admission process (via CAP rounds)
  - Fee structure
  - College infrastructure and facilities
  - Placement statistics
- Natural language understanding using **Dialogflow ES**
- User-friendly web interface (Flask + HTML/CSS/JS)
- Modular code with separate files for routing and Dialogflow logic
- Can be easily extended with more intents or domains

---

## 🛠️ Technologies Used

- **Dialogflow ES** – NLP and intent recognition  
- **Python (Flask)** – Backend API framework  
- **HTML5, CSS3, JavaScript** – Frontend technologies  
- **Google Dialogflow API** – Backend integration  
- **Git & GitHub** – Version control and deployment  

---

## 📁 Project Structure

```
college-enquiry-chatbot/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── dialogflow_handler.py
│   ├── dialogflow_utils.py
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📌 Current Status Overview

### ✅ Completed:
- Frontend (UI): A fully responsive interface built using HTML, CSS, JavaScript integrated with Flask.
- Flask Backend: Set up routes and integrated Dialogflow API with backend logic.
- Dialogflow Intents: Created and trained intents such as:
  - ask_courses
  - ask_admission
  - ask_dse_admission
  - ask_fees
  - ask_facilities
  - ask_placements
  - greetings
  - goodbye
  - fallback
- Dialogflow Integration: Working with service account key and tested API connectivity.

### 🔄 Planned Improvements:
- Improve bot responses to be **more specific** and **context-aware**, avoiding lengthy default paragraphs.
- Add support for **course-specific answers**, e.g., “Tell me about IT” should give a focused reply.
- Optionally include more intents for **college clubs**, **events**, **timings**, or **faculty information**.
- Optional Deployment: Host the project on platforms like **Heroku**, **Render**, or **Vercel** for live demo.


---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/UNiversity-enquiry-chatbot.git
   cd University-enquiry-chatbot

2. Set up virtual environment

python -m venv env
# Activate:
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows

3. Install dependencies

pip install -r requirements.txt

4. Add your Dialogflow key

Download your dialogflow_key.json from your Dialogflow service account.

Place it in the root directory (do NOT upload this file to GitHub).

5. Run the Flask server

python run.py

6. Visit in browser

http://localhost:5000

---

## Author

**Ayesha Siddika S**  
  Davanagere University,University
---

## Disclaimer

This chatbot is created for academic and demonstration purposes only.  
For official and up-to-date information, please visit the [official college website](https://www.shahandanchor.com/).



