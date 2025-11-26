
import streamlit as st
import nltk
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')


# -----------------------------------------
# Load and preprocess text
# -----------------------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

# Load text file
with open("anime.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

sentences = nltk.sent_tokenize(raw_text)
preprocessed_sentences = [preprocess(s) for s in sentences]

# Build TF-IDF model
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)

# -----------------------------------------
# Similarity function
# -----------------------------------------
def get_most_relevant_sentence(user_query):
    user_query_clean = preprocess(user_query)
    user_vec = vectorizer.transform([user_query_clean])
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()

    best_index = np.argmax(similarities)
    best_score = similarities[best_index]

    return sentences[best_index], best_score

# -----------------------------------------
# Chatbot logic
# -----------------------------------------
def chatbot(query):
    q = query.lower()

    # Rule-based responses
    if "what is anime" in q or q.strip() == "anime":
        return "Anime is a style of Japanese animation known for vibrant art and storytelling."

    if "types" in q or "genres" in q:
        return "Major anime genres include Shonen, Shojo, Seinen, Josei, Isekai, Mecha, Sports, and Slice of Life."

    if "best anime" in q:
        return "Popular anime include Fullmetal Alchemist Brotherhood, Attack on Titan, Demon Slayer, Naruto, and One Piece."

    # Similarity fallback
    response, score = get_most_relevant_sentence(query)

    if score < 0.05:
        return "I'm not sure. Try asking about anime genres, characters, or recommendations."
    
    return response

# -----------------------------------------
# Streamlit Interface
# -----------------------------------------
def main():
    st.title("Anime Chatbot 🎌🤖")
    st.write("Ask me anything about anime!")

    user_input = st.text_input("Your question:")

    if st.button("Ask"):
        if user_input.strip() != "":
            answer = chatbot(user_input)
            st.write("### 🤖 AnimeBot:")
            st.write(answer)

if __name__ == "__main__":
    nltk.download("punkt")
    main()
