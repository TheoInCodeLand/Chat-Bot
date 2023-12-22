# main.py

from flask import Flask, render_template, request
from chat_rules import get_bot_response

app = Flask(__name__)

# Define the Flask route
@app.route('/', methods=['GET', 'POST'])
def index():
    chat_history = []

    if request.method == 'POST':
        user_message = request.form['user_message']
        try:
            bot_response = get_bot_response(user_message)
            chat_history.append({'user': user_message, 'bot': bot_response})
        except Exception as e:
            # Log the error or take appropriate action
            print(f"Error processing user input: {str(e)}")
            # Return a friendly error message
            chat_history.append({'user': user_message, 'bot': "Sorry, there was an error processing your request."})

    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)