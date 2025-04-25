# Asha_AI_Chatbot
# 📘 Web Scraper & AI-Powered Q&A API

A robust FastAPI-based microservice designed to scrape web content, preprocess and store it, and deliver AI-powered answers to user queries. This API integrates modern scraping, NLP-based preprocessing, vector search, and GPT-driven natural language response generation.

---

## 📌 Key Features

- **🔍 Web Scraping**: Asynchronously scrapes and extracts content and metadata from any valid URL.
- **🧼 Text Preprocessing**: Cleans raw HTML, segments content, and prepares it for vector storage.
- **🔎 Semantic Search**: Embeds user questions and finds the most relevant content using vector similarity search.
- **🧠 GPT Integration**: Uses LLMs to generate contextually accurate responses based on relevant content chunks.
- **📊 Modular Architecture**: Cleanly separated logic for scraping, processing, and chatbot services.

---
## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/LizaArora/Asha_AI_Chatbot.git
cd Asha_AI_Chatbot

### 2. Install Dependencies
pip install -r requirements.txt

### 3. You are ready to code

HAVE A NICE CODING

🚀 Running the Application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

📒 Logging
This service uses Python’s built-in logging module to log events, errors, and key actions throughout the scraping and Q&A pipeline.

📦 Dependencies
fastapi

uvicorn

httpx or aiohttp (async scraping)

beautifulsoup4

sentence-transformers / transformers

openai / langchain / neo4j (as applicable)

All dependencies must be listed in requirements.txt.

🔐 Security Recommendations
Add authentication and authorization to endpoints (e.g., OAuth2, API key).

Sanitize and validate all external URLs and inputs.

Monitor usage and set rate limits in production.




