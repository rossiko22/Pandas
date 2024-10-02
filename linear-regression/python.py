import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("dataset/AmesHousing.csv")

# Display null values in each column
print(df.isnull().sum())

# Step 1: Handle missing values
df.replace('NA', np.nan, inplace=True)
df.fillna(0, inplace=True)

# Step 2: Handle non-numeric data
df = pd.get_dummies(df, drop_first=True)

# Step 3: Check data types
print(df.dtypes)

# Step 4: Plot heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=False, cmap="coolwarm")  # Disable annot to reduce clutter
plt.title('Correlation Heatmap')
plt.show()

# Step 5: Plot scatter plot - Living Area vs Sale Price
plt.figure(figsize=(8, 6))
plt.scatter(df['GrLivArea'], df['SalePrice'], alpha=0.5)  # Adjust alpha for transparency
plt.xlabel('Living Area (sq ft)')
plt.ylabel('Sale Price ($)')
plt.title('Living Area vs Sale Price')
plt.grid(True)
plt.show()

# Step 6: Train-test split for linear regression
X = df[['GrLivArea']]  # Feature(s)
y = df['SalePrice']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Step 10: Plot the regression line with test data
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Test Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')

# Improve axis display
plt.xlabel('Living Area (sq ft)')
plt.ylabel('Sale Price ($)')
plt.title('Living Area vs Sale Price with Regression Line')
plt.grid(True)
plt.legend()

# Limit the number of tick labels to avoid crowding
plt.xticks(np.arange(min(X_test['GrLivArea']), max(X_test['GrLivArea']), step=500))  # Adjust step based on your data
plt.yticks(np.arange(min(y_test), max(y_test), step=50000))

plt.show()
