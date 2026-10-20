# College FAQ Chatbot

## Project Overview
The College FAQ Chatbot is a Python-based application that answers frequently asked questions related to college admissions, courses, fees, scholarships, and other college services.

It uses Natural Language Processing (NLP) techniques and cosine similarity to identify the FAQ that best matches the user's question and display the corresponding answer. A simple graphical user interface is developed using Tkinter.

## Features
- Stores frequently asked questions and answers in a JSON file.
- Preprocesses text using NLTK.
- Converts questions into numerical representations using TF-IDF.
- Matches user questions with stored FAQs using cosine similarity.
- Displays relevant answers through a chatbot interface.
- Provides a fallback response when no sufficiently similar FAQ is found.
- Includes Send and Clear Chat functionality.

## Technologies Used
- **Programming Language:** Python
- **NLP Library:** NLTK
- **Text Matching:** Scikit-learn (TF-IDF and cosine similarity)
- **User Interface:** Tkinter
- **Data Storage:** JSON

## Project Structure

```text
FAQChatbot/
├── main.py
├── chatbot.py
├── faqs.json
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone or Download the Project
Download the project files and open the project folder in VS Code.

### 2. Install Dependencies

Open the terminal in the project directory and run:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Chatbot

Start the application by running:

```bash
python main.py
```

The chatbot window will open, allowing users to enter questions and receive answers.

## How It Works

1. **FAQ Collection:** Questions and answers are stored in `faqs.json`.
2. **Text Preprocessing:** User questions and stored FAQ questions are converted to lowercase, cleaned, and tokenized using NLTK.
3. **TF-IDF Vectorization:** The questions are converted into numerical vectors.
4. **Similarity Matching:** Cosine similarity compares the user's question with the stored FAQ questions.
5. **Answer Generation:** The chatbot returns the answer associated with the closest matching FAQ if the similarity score meets the configured threshold.
6. **User Interaction:** Tkinter provides the interface for submitting questions and viewing responses.

## Example Interaction

**User:** How do I apply for admission?

**Chatbot:** You can apply for admission through the college's official website by completing the application form.

**User:** How can I pay my fees?

**Chatbot:** You can contact the college accounts office to learn about available fee payment methods.

## Future Enhancements
- Add more FAQs and support additional topics.
- Improve question matching and handling of synonyms.
- Add a confidence score for matched answers.
- Store FAQs in a database.
- Enhance the chatbot interface.

## Requirements
- Python 3.x
- NLTK
- Scikit-learn
- Tkinter (usually included with standard Python installations)

