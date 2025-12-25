
# 📚 Urdu Ai Assistant (RAG-based Urdu PDF Query System)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](YOUR_LIVE_DEMO_LINK_HERE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI GPT-4o](https://img.shields.io/badge/Model-GPT--4o-orange.svg)](https://openai.com/)

An advanced **Retrieval-Augmented Generation (RAG)** system designed to process and query Urdu PDF documents. This project solves the unique challenges of Right-to-Left (RTL) script processing and semantic retrieval for the Urdu language.

---

## 🌟 Key Features

* **Urdu-Centric RAG Pipeline:** Specialized handling for Urdu text normalization and ligature processing using `LughaatNLP`.
* **Intelligent PDF Parsing:** Efficiently extracts and chunks Urdu text while preserving semantic meaning.
* **Semantic Search:** Uses OpenAI's `text-embedding-3-small` to find relevant context even with varying Urdu dialects or synonyms.
* **Interactive RTL UI:** A clean Streamlit interface with full Right-to-Left support for a native Urdu user experience.
* **AI-Powered Reasoning:** Leverages **OpenAI GPT-4o** to provide accurate, context-aware answers in fluent Urdu.

---

## 🏗️ Technical Architecture

This system follows a modular RAG architecture:

1.  **Data Ingestion:** Urdu PDFs are loaded and split into manageable chunks using `PyPDFLoader`.
2.  **Normalization:** Text is cleaned using `LughaatNLP` to ensure consistent script representation.
3.  **Vectorization:** Each chunk is converted into a 1536-dimensional vector embedding.
4.  **Retrieval:** The system identifies the top-k most relevant chunks based on the user's query.
5.  **Augmentation & Generation:** The retrieved context is fed into GPT-4o with a custom Urdu-specific prompt to generate the final response.

---

## 🛠️ Tech Stack

* **LLM:** OpenAI GPT-4o / GPT-4o-mini
* **Orchestration:** LangChain
* **NLP Tools:** LughaatNLP (Urdu Normalization)
* **Frontend:** Streamlit
* **Environment:** Python 3.10+

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* An OpenAI API Key

### Installation

1. Clone the repository:
   ```bash
   git clone [https://https://github.com/bushra387/Urdu-AI-Assistant.git](https://https://github.com/bushra387/Urdu-AI-Assistant.git)
   cd Urdu-AI-RAG

```

2. Install dependencies:
```bash
pip install -r requirements.txt

```


3. Run the application:
```bash
streamlit run app.py

```



---

## 💡 Why This Matters

Standard LLMs often struggle with low-resource languages like Urdu due to script complexity and lack of specialized training data. This project demonstrates how **AI Engineering** can bridge that gap by combining modern RAG techniques with specialized NLP preprocessing, making digital Urdu knowledge more accessible.

---

## 👤 Author

Bushra Rehman Computer Science Student | AI Enthusiast | 3.92 CGPA* [LinkedIn](www.linkedin.com/in/bushra-rehman-475356260 | [Portfolio])


```
