import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Use RandomForestRegressor for regression tasks
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
data = pd.read_csv('House_Price_Predection.csv')  # Update the dataset filename

# Data preprocessing (modify this based on your dataset)
# Assuming columns 'num_bedrooms', 'num_bathrooms', 'square_footage', 'location', and 'price'
data['location'] = data['location'].astype('category').cat.codes  # Encode categorical variables if needed

# Prepare feature and target variables
X = data[['num_bedrooms', 'num_bathrooms', 'square_footage', 'location']]  # Adjust features as needed
y = data['price']  # Target variable for house prices

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)  # Change to RandomForestRegressor
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")

# Save the model
joblib.dump(model, 'house_price_model.pkl')
