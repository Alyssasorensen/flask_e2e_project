from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load data using Pandas (Optional)
data = pd.DataFrame({
    "Category": ["Reproductive Health", "Mental Well-being", "Fitness"],
    "Information": [
        "Information about reproductive health",
        "Tips for mental well-being",
        "Fitness routines",
    ],
})

@app.route('/')
def home():
    return render_template('base.html', data=data)

@app.route('/reproductive')
def reproductive():
    return render_template('pages/reproductive.html', data=data)

@app.route('/mental')
def mental():
    return render_template('pages/mental.html', data=data)

@app.route('/fitness')
def fitness():
    return render_template('pages/fitness.html', data=data)

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Process the form data (e.g., send an email, store in a database)

    # Redirect to a thank-you page or the contact page
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('pages/thank_you.html', data=data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
