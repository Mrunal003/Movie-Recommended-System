# 🎬 Movie Recommendation System – GenreMatch

A simple and interactive movie recommendation system built with **NLP techniques** and **Streamlit**.  
This app allows users to input a genre and get personalized movie suggestions based on genre similarity.

---

## 🚀 Features

- 🔍 Recommends movies based on the genre you type
- 🧠 Uses NLP to calculate similarity between genres
- 📊 Lightweight and fast interface with Streamlit
- 📁 Reads from a movie dataset for suggestions

---

## 🛠️ Tech Stack

- **Python**  
- **Streamlit**  
- **scikit-learn (NLP + similarity)**  
- **Pandas**

---

## 📸 Demo

![Demo Screenshot](demo_image.png)  
<!-- Replace this with an actual image or GIF of the app if available -->

---

## 🧠 How It Works

1. The app processes the movie dataset using NLP.
2. User inputs a genre (e.g., "sci-fi", "comedy").
3. System calculates similarity scores between user input and movie genres.
4. Returns the most relevant movies sorted by similarity.

---

## Interaction with the application
https://practice-fxvmqyjkja3daprnnbhfju.streamlit.app/

## 📦 Installation

```bash
git clone https://github.com/Mrunal003/Movie-Recommended-System.git
cd Movie-Recommended-System
pip install -r requirements.txt
streamlit run app.py

