🏗️ Concrete Compressive Strength Predictor

This project is a machine learning application that predicts the compressive strength of concrete (measured in MPa) based on key input features such as cement content, water, aggregates, and curing age.
The model is powered by a Random Forest Regressor trained on the Concrete Compressive Strength dataset (UCI Repository)
.
My AppLink:https://main-ml-project-tq2c9q3oghopnsufvndabo.streamlit.app/
📊 This project helps civil engineers, researchers, and construction professionals estimate concrete strength quickly without destructive lab testing.

🚀 Features

Accurate Predictions: Estimates compressive strength (MPa) based on 8 key ingredients.

Interactive App (optional with Streamlit/Gradio): Adjust input values to test different concrete mixes.

Model Comparison: Evaluates different ML algorithms for best performance.

Data Visualization: Includes correlation heatmaps, feature importance, and regression plots.

🛠️ Tech Stack

Backend: Python 🐍

Machine Learning: Scikit-learn, Pandas, NumPy

Visualization: Matplotlib, Seaborn

UI Framework (optional): Streamlit or Gradio

📂 Dataset

concrete_data.csv contains 1,030 samples with 9 variables:

Feature	Description (per m³ of mixture)
Cement (kg)	Cement content
Blast Furnace Slag	Mineral admixture
Fly Ash	Supplementary cement material
Water (kg)	Mixing water
Superplasticizer (kg)	Chemical admixture
Coarse Aggregate (kg)	Gravel content
Fine Aggregate (kg)	Sand content
Age (days)	Curing age (1–365 days)
Strength (MPa)	Target variable (compressive strength)
📊 Data Analysis & Visualizations

1️⃣ Correlation Matrix

Cement, water, and age strongly influence compressive strength.

2️⃣ Feature Importance (Random Forest)

Top predictors: Cement, Age, and Water.

3️⃣ Prediction Distribution

Visuals compare actual vs. predicted strength.

🤖 Model Performance

Several regression models were tested in project.ipynb.

Model                     R² (Test)	RMSE (Test)
Linear Regression          	0.59	   10.12
Decision Tree Regressor	    0.79	   6.32
Random Forest Regressor	    0.84	   5.49
Gradient Boosting Regressor	0.82	   5.97

✅ Random Forest Regressor achieved the best balance of accuracy and generalization.

⚙️ Setup & Installation

Clone the repository:

git clone <your-repo-link>
cd concrete-strength-predictor


Create a virtual environment:

python -m venv venv
# Activate:
# Linux/Mac: source venv/bin/activate
# Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Requirements (requirements.txt)
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit   # optional
gradio      # optional

▶️ Running the Notebook

Open project.ipynb in Jupyter Notebook or VS Code:

jupyter notebook project.ipynb

▶️ Running the App (Optional)

If you built a frontend (app.py with Streamlit or Gradio):

streamlit run app.py


or

python app.py

📁 Project Structure
.
├── concrete_data.csv       # Dataset
├── project.ipynb           # Notebook (EDA, model training & evaluation)
├── app.py                  # Optional interactive app
├── requirements.txt        # Dependencies
└── README.md               # Documentation
