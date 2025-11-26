
# 📖 Anime Chatbot

A simple **Anime Chatbot** built with Python and Streamlit that can answer questions about anime, genres, history, and popular titles. The chatbot uses a hybrid approach: **rule-based responses** for common queries and **TF-IDF similarity** for everything else.

---

## 🛠 Features

* Rule-based answers for common questions:

  * What is anime?
  * Types/genres of anime
  * Best anime recommendations
* TF-IDF similarity for other queries
* Easy to use **web interface** built with Streamlit
* Works offline with a local text file (`anime.txt`)

---

## 📂 Project Structure

```
anime-chatbot/
│
├── app.py           # Main Streamlit app
├── anime.txt        # Anime knowledge base
├── README.md        # This file
└── requirements.txt # Python dependencies
```

---

## ⚡ How It Works

1. The bot loads `anime.txt` and splits it into sentences.
2. Each sentence is preprocessed (lowercased, cleaned).
3. A **TF-IDF vectorizer** is built on the sentences.
4. When a user asks a question:

   * If it matches a **rule-based pattern**, a predefined answer is returned.
   * Otherwise, the TF-IDF similarity function finds the most relevant sentence.

---

## 🛠 Installation

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/anime-chatbot.git
cd anime-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**OR manually:**

```bash
pip install streamlit nltk scikit-learn numpy
```

3. Download required NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

---

## 🚀 Running the App

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the URL displayed in your terminal to interact with the chatbot.

---

## 💡 Example Queries

* `what is anime`
* `types of anime`
* `best anime`
* `tell me about Naruto`
* `history of anime`

---

## ⚙ Future Improvements

* Add **anime character lookup**
* Include a **recommendation system** based on genres
* Upgrade similarity search with **sentence embeddings**
* Add **chat history** for more interactive conversations

---

## 📜 License

This project is **open-source** and free to use.


