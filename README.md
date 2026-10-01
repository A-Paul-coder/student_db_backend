# 🎓 Student Database Management System – AI Backend

An AI-powered backend application for managing student records using **FastAPI, SQLAlchemy, Gemini, LangGraph, and Qdrant**.

## 🚀 Features

* Student CRUD operations
* FastAPI REST APIs
* Swagger API documentation
* Gemini AI integration
* AI chatbot using LangGraph
* Student database interaction through chatbot
* Qdrant vector database for semantic search
* Docker support
* Environment-based API key management

## 🛠️ Technologies

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Gemini API
* LangChain
* LangGraph
* Qdrant
* Docker

## 📁 Project Structure

```text
app/
├── api/
├── ai/
├── core/
├── models/
├── repositories/
├── schemas/
└── services/

tests/
.env.example
requirements.txt
Dockerfile
README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/student-database-ai-backend.git
cd student-database-ai-backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env` from `.env.example` and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key
DATABASE_URL=sqlite:///./students.db
QDRANT_URL=http://localhost:6333
```

## 🐳 Run Qdrant

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🤖 Example Chatbot Questions

```text
How many students are there?
Tell me about student 1.
Show me students from the AI department.
```


