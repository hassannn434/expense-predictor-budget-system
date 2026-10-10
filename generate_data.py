import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 10000

# Advanced Features
income = np.random.randint(25000, 200000, n_samples)
age = np.random.randint(18, 65, n_samples)
family_size = np.random.randint(1, 6, n_samples)
lifestyle_score = np.random.randint(1, 10, n_samples) # 1 = Frugal, 10 = Luxury
city_tier = np.random.choice([1, 2, 3], n_samples, p=[0.5, 0.3, 0.2]) # Tier 1 is higher cost
credit_score = np.random.randint(550, 850, n_samples)

# Cost scaling based on city tier
tier_multiplier = np.where(city_tier == 1, 1.3, np.where(city_tier == 2, 1.1, 1.0))

# Granular category-wise expense modeling
rent = (np.where(family_size > 3, income * 0.35, income * 0.25) * tier_multiplier) + np.random.normal(0, 1000, n_samples)
food = (income * 0.18 + (family_size * 1500)) * tier_multiplier + np.random.normal(0, 800, n_samples)
utilities = (income * 0.08) * tier_multiplier + np.random.normal(0, 500, n_samples)
entertainment = income * 0.05 * (lifestyle_score / 5) * tier_multiplier + np.random.normal(0, 600, n_samples)
healthcare = income * 0.04 + (family_size * 800) + np.random.normal(0, 400, n_samples)
miscellaneous = income * 0.03 * (lifestyle_score / 5) + np.random.normal(0, 300, n_samples)

# Clip values for absolute realism
rent = np.clip(rent, 4000, None)
food = np.clip(food, 2500, None)
utilities = np.clip(utilities, 1200, None)
entertainment = np.clip(entertainment, 500, None)
healthcare = np.clip(healthcare, 500, None)
miscellaneous = np.clip(miscellaneous, 300, None)

total_expense = rent + food + utilities + entertainment + healthcare + miscellaneous

df = pd.DataFrame({
    'Income': income,
    'Age': age,
    'Family_Size': family_size,
    'Lifestyle_Score': lifestyle_score,
    'City_Tier': city_tier,
    'Credit_Score': credit_score,
    'Rent': rent,
    'Food': food,
    'Utilities': utilities,
    'Entertainment': entertainment,
    'Healthcare': healthcare,
    'Miscellaneous': miscellaneous,
    'Total_Expense': total_expense
})

df.to_csv('expenses.csv', index=False)
print("Advanced 10,000-row dataset 'expenses.csv' created successfully!")