# 📢 Notice2Action AI

### AI-Powered Notice Understanding and Action Assistant

Notice2Action AI is an AI-powered application that converts notice images into clear, actionable information.

Users can upload a college or official notice image. The application uses **OCR (Optical Character Recognition)** to extract the text and an **LLM (Large Language Model)** to analyze the content and identify important information such as summaries, dates, required actions, and deadlines.

---

## 🚀 Features

- 📤 Upload notice images
- 🔍 Extract text using OCR
- 🤖 Analyze notice using an LLM
- 📌 Generate a simple summary
- 📅 Identify important dates
- ℹ️ Extract important information
- ✅ Identify required actions
- ⏰ Detect deadlines
- 🖥️ Simple and interactive Streamlit interface

---
 🔄 How It Works

text
        📄 Notice Image
              │
              ▼
       🔍 Tesseract OCR
              │
              ▼
        📝 Extracted Text
              │
              ▼
          🤖 LLM
       (Groq API)
              │
              ▼
     ✨ Notice2Action Result
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Summary   Dates   Actions
              │
              ▼
          ⏰ Deadline

 🛠️ Technologies Used

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Main programming language       |
| 🎨 Streamlit     | Web application interface       |
| 🔍 Tesseract OCR | Extract text from images        |
| 🧩 Pytesseract   | Python wrapper for Tesseract    |
| 🤖 Groq API      | LLM API                         |
| 🧠 LLM           | Notice analysis                 |
| 🖼️ Pillow       | Image processing                |
| 🔐 python-dotenv | Environment variable management |
| 💻 VS Code       | Development                     |
| 🐙 GitHub        | Version control                 |

---

## 📁 Project Structure
text
Notice2Action-AI/
│
├── app.py
├── ocr.py
├── llm.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

### File Description
app.py → Streamlit application and user interface
ocr.py → OCR text extraction using Tesseract
llm.py → Groq LLM integration and notice analysis
requirements.txt → Required Python packages
.env → Stores the Groq API key
.gitignore → Prevents sensitive/unnecessary files from being uploaded
README.md → Project documentation

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/Notice2Action-AI.git

cd Notice2Action-AI

### 2. Create a virtual environment

python -m venv venv

powershell
venv\Scripts\activate

### 3. Install required packages

python -m pip install -r requirements.txt


---

## 🔍 Tesseract OCR Setup

Notice2Action AI uses **Tesseract OCR** to extract text from notice images.

Install Tesseract OCR on your computer.

On Windows, the default installation path is usually:

text
C:\Program Files\Tesseract-OCR\tesseract.exe


The path is configured in  ocr.py.

---

## 🔑 Groq API Setup

Create a Groq API key from:

text
https://console.groq.com/

Create a .env file in the project folder:

env
GROQ_API_KEY=your_groq_api_key


⚠️ **Never upload your .env file to GitHub.**

---

## ▶️ Run the Application

Start the Streamlit application:


streamlit run app.py


The application will open in your browser.

---

## 🖼️ Example Usage

### Step 1

Upload a college or official notice image.

### Step 2

Click:
🔍 Analyze Notice


### Step 3

The application extracts the text using OCR.

### Step 4

The extracted text is analyzed by the LLM.

### Step 5

The application displays:

📌 Summary

📅 Important Dates

ℹ️ Important Information

✅ Actions Required

⏰ Deadline


## 💡 Example

### Input

A college notice containing:


Internal Assessment – II

The assessment will be conducted
from 15 October 2026 to 18 October 2026.

Last date for assignment submission:
12 October 2026.

Students must bring their college ID card.


### Output


📌 Summary
Internal Assessment – II will be conducted
from 15–18 October 2026.

📅 Important Dates
• Assessment: 15–18 October 2026
• Assignment deadline: 12 October 2026

ℹ️ Important Information
• Bring college ID card.

✅ Actions Required
• Submit the assignment.
• Attend the assessment.

⏰ Deadline
12 October 2026




## 🎯 Use Cases

Notice2Action AI can be useful for:

* 🎓 College students
* 🏫 Educational institutions
* 🏢 Organizations
* 📋 Administrative notices
* 📢 Event announcements
* 📝 Assignment notifications
* 📅 Exam schedules
* ⏰ Deadline-based notices

---

## 🔐 Security

The Groq API key is stored using an environment variable instead of being hardcoded in the source code.

The .env file should be included in .gitignor:

text
.env
venv/
__pycache__/

Never expose your API key publicly.

---

## 🔮 Future Enhancements

Future versions can include:

* 📄 PDF notice support
* 🌐 Multiple language support
* ✍️ Handwritten notice recognition
* 🔊 Text-to-speech output
* 📅 Automatic calendar reminders
* 📧 Email notifications
* 📱 Mobile-friendly interface
* 💬 Chat with the uploaded notice
* 🗂️ Notice history
* 🔔 Deadline reminders

---

## 🌟 Project Highlights

This project demonstrates the integration of:


Computer Vision
      +
OCR
      +
Generative AI
      +
LLM
      +
Prompt Engineering
      +
Web Application Development


## 👩‍💻 Author

**Sruthi S**

B.Sc. Computer Science with Artificial Intelligence

### GitHub

[https://github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!





