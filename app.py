from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return render_template('generate.html')

@app.route('/about')
def about():
    return render_template('about.html')