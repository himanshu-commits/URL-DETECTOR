import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Function to train a URL classification model
def train_url_classifier(training_dataset_path):
    # Load the training dataset
    training_data = pd.read_csv('/Users/himanshugupta/Documents/python/Sec_Classifying_URL_Detection-main/Dataset on which Attack applied/Copy of Merged Dataset 1.csv')
    training_data.head()
    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Convert URLs into numerical features
    X_train_tfidf = tfidf_vectorizer.fit_transform(training_data['Domain Name'])
    y_train = training_data['Label']
    
    # Initialize and train a machine learning model (Random Forest, in this case)
    model = RandomForestClassifier()
    model.fit(X_train_tfidf, y_train)
    
    # Make predictions on the training data
    y_pred = model.predict(X_train_tfidf)
    
    # Calculate accuracy on the training data
    accuracy = accuracy_score(y_train, y_pred)
    
    # Generate a classification report
    report = classification_report(y_train, y_pred, target_names=['Safe', 'Malicious'])
    
    return model, tfidf_vectorizer, accuracy, report

# Function to classify a URL
def classify_url(url, model, tfidf_vectorizer):
    # Preprocess the input URL
    preprocessed_url = url
    
    # Convert the preprocessed URL into a TF-IDF vector
    url_tfidf = tfidf_vectorizer.transform([preprocessed_url])
    
    # Predict the label (0 for safe, 1 for malicious)
    prediction = model.predict(url_tfidf)
    
    if prediction[0] == 1:
        return "Malicious"
    else:
        return "Safe"

# Main function to interact with the user
def main():
    print("URL Classification System")
    
    # Training model
    training_dataset_path = 'your_training_dataset.csv'  # Replace with your dataset path
    print("Training the model...")
    model, tfidf_vectorizer, accuracy, report = train_url_classifier(training_dataset_path)
    print("Model training complete.")
    print(f"Training Accuracy: {accuracy:.2f}")
    print("Classification Report on Training Data:\n", report)
    
    while True:
        user_url = input("Enter a URL to classify (or 'exit' to quit): ")
        
        if user_url.lower() == 'exit':
            break

        result = classify_url(user_url, model, tfidf_vectorizer)
        print(f"The URL '{user_url}' is classified as: {result}")

if __name__ == "__main__":
    main()
