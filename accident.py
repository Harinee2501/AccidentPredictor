import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE

# Load the data
data = pd.read_csv('cleaned.csv')  # Update this path

# Define feature columns based on the dataset
features = data[['Age', 'sex', 'education', 'driverrelation', 'experience', 'lanes', 'junctype', 'roadtype', 'light', 'weather', 'collision', 'direction', 'pedestrian', 'cause']]
target = data['severity']

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Define preprocessing steps (one-hot encoding for all categorical features)
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), features.columns)])

# Preprocess the training data
x_train_transformed = preprocessor.fit_transform(x_train)
x_test_transformed = preprocessor.transform(x_test)

# Apply SMOTE to oversample the minority classes
smote = SMOTE(random_state=42)
x_train_resampled, y_train_resampled = smote.fit_resample(x_train_transformed, y_train)

# Define the pipeline with the classifier (Random Forest)
pipeline = Pipeline(steps=[
    ('classifier', RandomForestClassifier(random_state=42))
])

# Fit the pipeline on the resampled data
pipeline.fit(x_train_resampled, y_train_resampled)

# Predict on test data
y_pred = pipeline.predict(x_test_transformed)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the evaluation metrics
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
