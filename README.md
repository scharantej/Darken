 ## Flask Application Design

### HTML Files

**index.html**
- This is the main HTML file that will be rendered when the user accesses the root URL of the application.
- It will contain the following elements:
  - A sky blue background color.
  - A single button in the center of the page with the text "Don't click me!" and an id of "button".

**black.html**
- This HTML file will be rendered when the button is clicked.
- It will contain the following elements:
  - A black background color.
  - No button.

### Routes

**@app.route('/')**
- This route will handle requests to the root URL of the application.
- It will render the index.html file.

**@app.route('/black')**
- This route will handle requests to the '/black' URL of the application.
- It will render the black.html file.

**@app.route('/click', methods=['POST'])**
- This route will handle POST requests to the '/click' URL of the application.
- It will be triggered when the button is clicked.
- It will redirect the user to the '/black' URL.