from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Main landing page with the proposal question"""
    return render_template('index.html')

@app.route('/yes')
def success():
    """Success page when she clicks Yes"""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
