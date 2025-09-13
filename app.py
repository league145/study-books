from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BOOKS_FOLDER = os.path.join('static', 'books')

@app.route('/')
def index():
    books = [f for f in os.listdir(BOOKS_FOLDER) if f.lower().endswith('.pdf')]
    return render_template('index.html', books=books)

@app.route('/books/<filename>')
def book(filename):
    return send_from_directory(BOOKS_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)