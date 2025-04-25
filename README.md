# Asha_AI_Chatbot
# 📘 Web Scraper & AI-Powered Q&A API

A robust FastAPI-based microservice that scrapes web content, preprocesses and stores it in **Neo4j**, and delivers AI-powered answers to user queries. This API integrates modern scraping, NLP-based preprocessing, vector search using Neo4j, and GPT-driven natural language response generation.

---

## 📌 Key Features

- **🔍 Web Scraping**: Asynchronously scrapes and extracts content and metadata from any valid URL.
- **🧼 Text Preprocessing**: Cleans raw HTML, segments content into chunks, and embeds it for semantic search.
- **🧠 Vector Storage with Neo4j**: Stores vector embeddings in a Neo4j graph database for efficient similarity search.
- **🔎 Semantic Search**: Embeds user queries and retrieves the most relevant content chunks using cosine similarity.
- **💬 GPT-Powered Answers**: Generates intelligent, context-aware answers using retrieved data and an LLM.
- **🧩 Modular Design**: Clear separation between scraping, processing, embedding, vector search, and response generation.


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




