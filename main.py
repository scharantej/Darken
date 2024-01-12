 
# Import necessary libraries
from flask import Flask, render_template, redirect, request

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the index.html file
    return render_template('index.html')

# Define the route for the black page
@app.route('/black')
def black():
    # Render the black.html file
    return render_template('black.html')

# Define the route for the button click
@app.route('/click', methods=['POST'])
def click():
    # Redirect to the black page
    return redirect('/black')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
