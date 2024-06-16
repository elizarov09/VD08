from flask import Flask, render_template, jsonify
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
        translated_text = GoogleTranslator(source='en', target='ru').translate(quote['content'])
        quote['translated_content'] = translated_text
        return jsonify(quote)
    else:
        return jsonify({"content": "Error fetching quote", "author": "", "translated_content": ""})

if __name__ == '__main__':
    app.run(debug=True)
