# 💰 Expense Predictor & Budget Recommendation System

An end-to-end Machine Learning web application built using **Python**, **Scikit-Learn**, and **Streamlit**. This tool enables users to forecast future personal expenses based on historical financial behaviors and receives automated, personalized budget recommendations across various spending categories.

---

## 📌 Features

* **Expense Forecasting:** Uses a trained **Random Forest Regression** model to predict upcoming financial expenditures based on historical transactional and categorical features.
* **Smart Budget Recommendations:** Generates rule-based and ML-assisted advice to optimize monthly budgets and savings target ratios.
* **Interactive UI:** Built with **Streamlit** for real-time visualization, metric tracking, and intuitive user inputs.
* **Privacy & Security:** Runs locally without storing sensitive user financial records on remote databases.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.9+
* **Frontend / Web Framework:** Streamlit
* **Machine Learning Library:** Scikit-Learn (Random Forest)
* **Data Processing & Manipulation:** Pandas, NumPy
* **Version Control:** Git & GitHub

---

## 📁 Repository Structure

```text
├── dataset/
│   └── expenses.csv              # Sanitized training/testing dataset
├── model/
│   └── train_model.py            # Model training & preprocessing script
├── app.py                        # Streamlit web application interface
├── requirements.txt              # Project dependencies
├── .gitignore                    # Excluded files
└── README.md                     # Project documentation

🚀 Getting Started Locally
Follow these steps to set up and run the application on your local machine:

1. Clone the Repository
Bash
git clone [https://github.com/hassannn434/expense-predictor-budget-system.git](https://github.com/hassannn434/expense-predictor-budget-system.git)
cd expense-predictor-budget-system

2. Create and Activate a Virtual Environment
Windows (PowerShell):

PowerShell
python -m venv venv
.\venv\Scripts\activate

3. Install Required Dependencies
Bash
pip install -r requirements.txt

4. Train the Model (Optional / Local Setup)
If model.pkl is not present in your local project directory, generate it by running:

Bash
python model/train_model.py

5. Launch the Web Dashboard
Bash
streamlit run app.py
The app will automatically open in your web browser at http://localhost:8501

## 🖼️ Local Demo & Output Screenshots

### 📸 Screenshots

![Dashboard Overview]
<img width="1913" height="801" alt="image" src="https://github.com/user-attachments/assets/dc5a23f3-fd49-46bb-ac4f-f69d7bf0c2f8" />


![Expense Analytics]

<img width="1906" height="888" alt="image" src="https://github.com/user-attachments/assets/2836bdf2-89c8-4537-8087-9159c8cb08a5" />


![Budget Recommendation]

<img width="1913" height="755" alt="image" src="https://github.com/user-attachments/assets/51d4ce0b-7782-4db4-a0ba-245942bb04e7" />


![Category Breakdown]

<img width="1883" height="822" alt="image" src="https://github.com/user-attachments/assets/d6a4a483-d349-4e6a-988e-aafb94b92956" />


![Model Prediction Results]

<img width="1913" height="894" alt="image" src="https://github.com/user-attachments/assets/32b131c1-6712-4aaf-8a69-5f6abf9155f3" />


---

### 🎥 Video Demonstration

▶️ **[Click here to watch the full application walkthrough video]

[3a50ab87-c5ad-44f5-81ee-07c131a2fc96.webm](https://github.com/user-attachments/assets/1667f049-1160-4f5f-85c5-d15670f1002e)


---

### 🌐 Local Access

To run and view the interface locally on your machine:
```text
streamlit run app.py
(Access it in your browser at http://localhost:8501)

⚙️ How It Works
User Input: Enter income details, past category expenses (e.g., Food, Utilities, Entertainment, Rent), and monthly savings targets into the Streamlit interface.

Machine Learning Forecast: A trained Random Forest Regression model processes historical spending trends to predict upcoming monthly expenditures.

Smart Budget Recommendations: The system compares predicted expenses against standard budgeting rules (e.g., the 50/30/20 framework) to provide personalized spending limits and saving tips.

📊 Machine Learning Pipeline & Metrics
Algorithm: Random Forest Regressor
Preprocessing: Feature scaling via StandardScaler and categorical encoding with Pandas/Scikit-Learn.
Evaluation Metrics: Evaluated using Mean Absolute Error (MAE) and $R^2$ Score for reliable financial forecasting.

Built With
Streamlit - Interactive web interface

Scikit-Learn - Machine learning modeling and preprocessing

Pandas & NumPy - Data manipulation and numerical operations

🤝 Contributing
Contributions, issues, and feature requests are welcome!

Fork the Repository

Create your Feature Branch (git checkout -b feature/NewFeature)

Commit your Changes (git commit -m 'Add NewFeature')

Push to the Branch (git push origin feature/NewFeature)

Open a Pull Request

📜 License
Distributed under the MIT License.
