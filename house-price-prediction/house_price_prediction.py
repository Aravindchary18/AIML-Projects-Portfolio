# Import NumPy for numerical operations
import numpy as np
# Import LinearRegression model from scikit-learn
from sklearn.linear_model import LinearRegression


# Features: Size (sqft), Rooms, Age (years)
X=np.array([[1000,2,5],
            [1200,3,4],
            [1500,3,6],
            [1800,4,3]])


# Target: House prices
y=np.array([200000,240000,300000,360000])

# Create Linear Regression model
model=LinearRegression()

# Train the model with house data
model.fit(X,y)

# New house to predict price
new_house=[[1600,3,4]]

# Predict house price
prediction=model.predict(new_house)


# Print predicted price
print("prediction house price:",prediction[0])
