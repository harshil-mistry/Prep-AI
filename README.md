# 📚 PrepAI – AI-Powered Exam Preparation Assistant

**PrepAI** is a smart exam preparation web application designed to help students study more effectively. It allows users to create separate exam spaces, upload study materials, chat with an AI to generate personalized notes, and download conversations for later use. 

Built using Django, Google Gemini, and a clean HTML/CSS/JS frontend, PrepAI creates a personalized study environment for every student.

---

## 🚀 Features

### 👤 User Authentication & Session Security
- Secure **signup and login system**
- Every request is authenticated to ensure **only logged-in users** can access features

### 📚 Exam-Specific Chat Contexts
- Users can **create multiple exams**
- Each exam has its **own chat** to keep conversations organized and focused

### 📄 Upload Study Materials
- Upload exam PDFs, lecture notes, or any custom content
- AI uses uploaded material to **generate context-aware notes and answers**

### 🤖 AI Chat (Powered by Google Gemini)
- Ask questions about your exam content
- Receive **intelligent, context-aware** responses
- Gemini understands and remembers the **exam context**

### 💡 Smart Follow-Up Suggestions
- After each reply, users get **suggested follow-up prompts**
- Helps users clarify doubts and **explore related topics naturally**

### 📥 Downloadable PDF Notes
- Download the generated notes as a **well-formatted PDF**
- Share with friends or use for revision later

---

## 🛠️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| **Backend** | Python, Django        |
| **Frontend**| HTML, CSS, JS              |
| **AI Engine** | Google Gemini        |
| **Database**| Django ORM (Supabase) |

---

## 📸 Screenshots

> _Below are key screenshots showcasing the main features of PrepAI._

### Dashboard 
<img src="https://res.cloudinary.com/de4yjlmry/image/upload/v1750441246/project_images/homepage.png" alt="Dashboard" width="700"/>

### Login Page
<img src="https://res.cloudinary.com/de4yjlmry/image/upload/v1750441258/project_images/login.png" alt="Chat Interface" width="700"/>

###  Creating Exam Spaces
<img src="https://res.cloudinary.com/de4yjlmry/image/upload/v1750441262/project_images/newchat.png" alt="Upload Material" width="700"/>

###  AI Chat for Preps
<img src="https://res.cloudinary.com/de4yjlmry/image/upload/v1750441221/project_images/aichat.png" alt="Download PDF" width="700"/>

---

## ⚙️ How to Run Locally 

# 1. Clone the repository 
```bash 
git clone https://github.com/your-username/prepai.git 
cd prepai 
```

# 2. Create a virtual environment and activate it 
```bash
python -m venv env 
source env/bin/activate # On Windows: env\Scripts\activate 
```

# 3. Install dependencies 
```bash
pip install -r requirements.txt 
```
# 4. Configure the env files from env example file 
>Note: There are two .env files to be configured
> 1. In the core app
> 2. In the prepai project

# 5. Apply migrations 
```bash
python manage.py makemigrations 
python manage.py migrate 
```

# 6. Run the development server 
```bash 
python manage.py runserver 
```

# 7. Open your browser and visit: 
> http://localhost:8000

---

## 🙋‍♂️ Author

**Harshil Mistry**  
- 🔗 [GitHub](https://github.com/harshil-mistry)  
- 💼 [LinkedIn](https://www.linkedin.com/in/harshilmistry295)  
- 📧 Email: harshilmistry31@gmail.com
