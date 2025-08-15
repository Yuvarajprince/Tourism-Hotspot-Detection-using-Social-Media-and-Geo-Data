# 🌍 Tourism Hotspot Finder

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0-orange)](https://streamlit.io/)


An intelligent tourism exploration platform built with **Streamlit**, **Machine Learning**, and **MongoDB** to help users discover the best tourist destinations worldwide.  
The system enables search by country/state/city, stores favorite spots, provides analytics, and integrates a travel chatbot for instant guidance.

---

## 📌 Features

### 1. **Interactive Search**
- Search tourist spots by country, state, city, and category.
- View detailed information such as ratings, best visiting time, nearby attractions, fees, and more.
- Open locations directly in Google Maps.

### 2. **Saved Places**
- Save selected spots to a MongoDB database for quick access.
- View and manage your saved locations with details and map links.

### 3. **Tourist Place Analytics**
- View statistics like:
  - Total number of tourist places
  - Countries represented
  - Average ratings
  - Top 5 most popular destinations

### 4. **Travel Chatbot**
- Get instant answers to common travel-related queries.
- Includes a set of predefined popular questions.
- Falls back to **OpenAI API** for dynamic responses.

### 5. **Machine Learning Models**
- Models trained to classify "Family-Friendly" tourist spots:
  - Logistic Regression
  - Support Vector Classifier (SVC)
  - Random Forest Classifier

### 6. **Automated Literature Survey Generator**
- Generates a structured **DOCX** file containing related academic works.
- Saves the file automatically in the `DOC/` folder.

---

## 🗂 Project Structure

```
Tourism-Hotspot-Finder/
│
├── docs/                       # Documentation files
│   ├── Literature_Survey.docx  # Literature survey document
│   └── paper.pdf               # Published paper (optional)
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
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # Project license
└── README.md                   # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/Yuvarajprince/Tourism-Hotspot-Detection-using-Social-Media-and-Geo-Data.git
cd 🌍 Tourism Hotspot Finder
```

2. **Create and activate a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Setup MongoDB**  
- Ensure MongoDB is installed and running locally.
- Default connection URI: `mongodb://localhost:27017`
- The app will create/use the database `tourism_db` and collection `places`.

5. **Configure OpenAI API Key**  
- In `src/app.py`, set:
```python
OPENAI_API_KEY = "your-openai-api-key"
```

---

## 🚀 Usage

### **Run the Streamlit Application**
```bash
streamlit run src/app.py
```

### **Train the Machine Learning Models**
```bash
python src/train.py
```
Models will be saved in the `models/` directory.

### **Generate Literature Survey**
```bash
python src/liter.py
```
Output: `DOC/Tourism_Hotspot_Literature_Survey.docx`

---

## 📊 Dataset

The dataset (`updated_tourist_places_dataset.csv`) contains fields like:
- Country, State, City
- Tourist Place
- Reviews
- Best Visiting Time
- Nearby Attractions
- Entry Fee
- Family-Friendly
- Adventure Level
- Accessibility
- Google Maps Link

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Contributions are welcome!  
Please:
1. Fork the repo
2. Create a new branch (`feature/my-feature`)
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 🙌 Acknowledgements
- **Streamlit** for interactive UI
- **Scikit-learn** for machine learning models
- **MongoDB** for data persistence
- **OpenAI API** for chatbot responses
- **Pandas** for data handling
