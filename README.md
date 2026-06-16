# 📚 StudyPilot Engine

An AI-powered study planner that extracts subjects and topics from syllabus PDFs, generates structured study plans, and exports personalized schedules.

## 🚀 Features

* Upload syllabus PDFs
* Extract syllabus content using AI
* Convert syllabus into structured JSON
* Automatically identify subjects and topics
* Generate study schedules based on available study hours
* Display topic-wise study recommendations
* Export study plans as PDF files
* Interactive Streamlit dashboard

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API (Llama 3.3 70B)
* PyPDF
* ReportLab
* python-dotenv

---

## 📂 Project Structure

study-pilot/

├── app.py

├── planner.py

├── syllabus_parser.py

├── pdf_export.py

├── email_sender.py

├── requirements.txt

├── .env

└── data/

```
├── syllabus.pdf

└── syllabus.json
```

---

## ⚙️ How It Works

### 1. Upload Syllabus

The user uploads a syllabus PDF through the Streamlit interface.

### 2. AI Processing

The syllabus text is extracted using PyPDF and sent to the Groq API.

### 3. Structured JSON Generation

The AI converts the syllabus into structured JSON containing:

* Subject names
* Topics for each subject

### 4. Study Plan Generation

The planner allocates available study hours across subjects and creates a daily schedule.

### 5. Export

The generated study plan can be exported as a PDF timetable.

---

## 📸 Screenshots

### Dashboard
<img width="1067" height="747" alt="upload" src="https://github.com/user-attachments/assets/f51de81a-44e9-4393-b912-c0ee83f39133" />



### Study Plan
<img width="1057" height="716" alt="topics" src="https://github.com/user-attachments/assets/9259984d-4ffc-4d8b-8fec-614eeb03fb64" />


### PDF Export
<img width="705" height="595" alt="plan" src="https://github.com/user-attachments/assets/9b74fdf6-4720-4c4e-b765-38d70563e3b5" />



---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd study-pilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* Email reminders
* Exam-date based prioritization
* Weekly study planning
* Calendar integration
* Progress tracking
* Cloud deployment

---

## 👨‍💻 Author

 Pallavi Gupta 
