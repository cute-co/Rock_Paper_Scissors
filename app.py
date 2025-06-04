from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define choices
CHOICES = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'R' and computer == 'S') or \
         (user == 'P' and computer == 'R') or \
         (user == 'S' and computer == 'P'):
        return "You win!"
    else:
        return "You lose!"

# Route for handling the game
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_choice = None
    computer_choice = None

    if request.method == 'POST':
        user_choice = request.form.get('choice')
        if user_choice not in CHOICES:
            result = "Invalid choice."
        else:
            computer_choice = random.choice(list(CHOICES.keys()))
            result = determine_winner(user_choice, computer_choice)

    return render_template('index.html',
                           result=result,
                           user_choice=CHOICES.get(user_choice),
                           computer_choice=CHOICES.get(computer_choice))

if __name__ == '__main__':
    app.run(debug=True)
