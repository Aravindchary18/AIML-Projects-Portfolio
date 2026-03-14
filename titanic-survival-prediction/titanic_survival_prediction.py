
# Import NumPy for array handling
import numpy as np
# Import Decision Tree Classifier from scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Features: Gender (0=male,1=female), Age, Class
X=np.array([
    [0,22,3],
    [1,38,1],
    [1,26,3],
    [0,35,1],
    [0,28,2]
])

# Target: survival (0=died,1=survived)
y=np.array([0,1,1,1,0])


# Create Decision Tree model
model=DecisionTreeClassifier()

# Train the model with passenger data
model.fit(X,y)

# New passenger to predict survival
new_passenger=[[1,30,2]]  # female, 30 years, 2nd class

# Predict survival
prediction=model.predict(new_passenger)


# Print predicted survival 
print("survival prediction:",prediction[0])
