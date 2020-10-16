from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')

app.run(host='0.0.0.0', port=80, debug=True)