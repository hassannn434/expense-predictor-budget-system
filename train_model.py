import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('expenses.csv')

# Inputs (Features)
X = df[['Income', 'Age', 'Family_Size', 'Lifestyle_Score', 'City_Tier', 'Credit_Score']]

# Multi-outputs (Total + 6 detailed categories)
y = df[['Total_Expense', 'Rent', 'Food', 'Utilities', 'Entertainment', 'Healthcare', 'Miscellaneous']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Optimized Random Forest Regressor
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Advanced multi-output model trained successfully with 10k rows!")