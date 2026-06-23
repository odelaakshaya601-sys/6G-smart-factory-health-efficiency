import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

INPUT_PATH = "../data/raw/Thales_Group_Manufacturing.csv"

def train_predictive_model():
    print("--- Starting Process Health Machine Learning Model ---")
    try:
        # Load the dataset you just uploaded
        df = pd.read_csv(INPUT_PATH)
        
        # Identify features and target column dynamically based on your layout
        # Column O is the last column (Risk Profile: High, Medium, Low)
        target_col = df.columns[-1] 
        print(f"Target variable identified for Process Health: {target_col}")
        
        # Select numeric sensor columns (Columns E through L) as your training features
        feature_cols = df.select_dtypes(include=[np.number]).columns
        
        # Separate features (X) and label (y)
        X = df[feature_cols].fillna(df[feature_cols].median()) # clean any remaining blanks
        y = df[target_col].astype(str).str.strip()
        
        # Split data: 80% for training the model, 20% for testing its accuracy
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize a Random Forest Classifier model
        print("Training Random Forest Classifier on 6G industrial sensor logs...")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Predict on test data
        predictions = model.predict(X_test)
        
        # Print results
        print("\n--- Model Performance Results ---")
        print(f"Total Accuracy Score: {accuracy_score(y_test, predictions):.2%}")
        print("\n--- Detailed Classification Report ---")
        print(classification_report(y_test, predictions))
        
    except Exception as e:
        print(f"Model execution skipped. Technical note: {e}")
        print("Check if column headers match your spreadsheet exactly.")

if __name__ == "__main__":
    train_predictive_model()
