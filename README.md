# 🎬 Movie Recommender System

A content-based Movie Recommender System built with **Python**, **Streamlit**, and **Machine Learning**.  
It suggests top 5 movies similar to the one selected by the user based on textual metadata such as **genres**, **keywords**, **cast**, and **crew**.

🔗 **Live Demo:** [movie-recommender-system-by-hp.streamlit.app](https://movie-recommender-system-by-hp.streamlit.app/)

---

## 📘 Project Overview

This project uses **Natural Language Processing (NLP)** and **Cosine Similarity** to analyze movie metadata and recommend similar titles.

The app interface is powered by **Streamlit**, providing an interactive and lightweight deployment for end users.

---

## ⚙️ How It Works

1. Dataset: [TMDB 5000 Movies + Credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
2. Features extracted:
   - Overview (plot summary)
   - Genres
   - Keywords
   - Cast
   - Crew
3. Text preprocessing:
   - Tokenization and stemming using `nltk.PorterStemmer`
   - Vectorization using `CountVectorizer` (Bag of Words)
4. Similarity computation using **Cosine Similarity**
5. Recommendations fetched dynamically along with posters via the **TMDB API**

---

## 🧠 Tech Stack

- **Python 3.9+**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **NLTK**
- **Streamlit**
- **Requests**
- **Pickle**

---
🧾 License

This project is open-source and available under the MIT License
.

✨ Author

Harsh Pandey
💼 LinkedIn
 | 📧 harshpandey@gmail.com.com

🖥️ Built with ❤️ using Python + Streamlit


