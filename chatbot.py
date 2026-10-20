
import json
import re
from pathlib import Path

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download the tokenizer data if it is not already installed
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


# Load FAQs from the JSON file
faq_path = Path(__file__).with_name("faqs.json")

with open(faq_path, "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Clean and tokenize text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = word_tokenize(text)
    return " ".join(tokens)


# Prepare FAQ questions
questions = [faq["question"] for faq in faqs]
processed_questions = [preprocess_text(q) for q in questions]


# Convert questions into numerical vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)


# Find the best answer for a user question
def get_answer(user_question):
    if not user_question.strip():
        return "Please enter a question."

    processed_input = preprocess_text(user_question)
    input_vector = vectorizer.transform([processed_input])

    similarities = cosine_similarity(input_vector, question_vectors)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]

    # Avoid returning an unrelated answer
    if best_score < 0.20:
        return "Sorry, I couldn't find a relevant answer. Please try asking another question."

    return faqs[best_index]["answer"]


# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", get_answer(user_input))
