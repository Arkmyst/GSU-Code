# linear_regression_test.py

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Generate synthetic data
np.random.seed(0)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # 100 samples, single feature
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# 2. Create a DataFrame
data = pd.DataFrame(np.hstack((X, y)), columns=['Feature', 'Target'])

# 3. Fit a linear regression model
model = LinearRegression()
model.fit(data[['Feature']], data['Target'])

# 4. Predict values
data['Predicted'] = model.predict(data[['Feature']])

# 5. Plot the original data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(data['Feature'], data['Target'], color='blue', label='Original Data')
plt.plot(data['Feature'], data['Predicted'], color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression Example')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.grid()

# 7. Print the model parameters only if the model has been fitted
print("The model has not been fitted properly.")

# 6. Show the plot
plt.show()

# 7. Print the model parameters only if the model has been fitted
print("The model has not been fitted properly.")