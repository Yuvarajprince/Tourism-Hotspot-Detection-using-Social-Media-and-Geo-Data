# 🌍 Tourism Hotspot Finder

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0-orange)](https://streamlit.io/)

A comprehensive tourism recommendation system that helps travelers discover popular destinations, with features including place search, saved favorites, analytics, and an AI-powered chatbot.

> **Note**: This project is associated with our published paper: [Paper Title](link-to-paper) (replace with actual details)

## Features

- 🔍 **Interactive Search**: Filter tourist places by country, state, city, and category
- 📌 **Saved Places**: Bookmark your favorite destinations with MongoDB storage
- 📊 **Analytics Dashboard**: View statistics and top-rated places
- 🤖 **AI Chatbot**: Get travel recommendations powered by OpenAI
- 🏆 **Machine Learning Models**: Predict family-friendly destinations

Tourism-Hotspot-Finder/
├── docs/                       # Documentation files
│   ├── Literature_Survey.docx  # Your literature survey document
│   └── paper.pdf               # Your published paper (if available)
│
├── src/                        # Source code
│   ├── app.py                  # Streamlit application
│   ├── train.py                # Model training script
│   └── liter.py                # Literature survey generator
│
├── models/                     # Trained models
│   ├── logistic_regression_model.pkl
│   ├── svc_model.pkl
│   └── random_forest_model.pkl
│
├── data/                       # Dataset
│   └── updated_tourist_places_dataset.csv
│
├── README.md                   # Main project documentation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files to ignore
└── LICENSE                     # Project license


<div align="center">
  <img src="data/diagram.png" alt="App Screenshot" width="600"/>
</div>

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Tourism-Hotspot-Finder.git
cd Tourism-Hotspot-FinderTourism-Hotspot-Finder/
