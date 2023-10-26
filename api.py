from flask import Flask, render_template, request
from myclass import classify_url, train_url_classifier  # Import the necessary functions

app = Flask(__name__)

# Initialize the model and tfidf_vectorizer
model, tfidf_vectorizer, _, _ = train_url_classifier('your_training_dataset.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    url = request.form['url']
    result = classify_url(url, model, tfidf_vectorizer)  # Pass 'model' and 'tfidf_vectorizer'
    return render_template('result.html', result=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
