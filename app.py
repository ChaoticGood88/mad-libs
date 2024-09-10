from flask import Flask, render_template, request
from stories import story  # Import the 'story' instance from stories.py
from flask_debugtoolbar import DebugToolbarExtension  # Import Debug Toolbar

app = Flask(__name__)

# Secret key is required by Flask Debug Toolbar for security purposes
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Enable the debug toolbar
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Initialize the Debug Toolbar
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Display form to fill in story prompts dynamically."""
    prompts = story.prompts  # Get the list of prompts from the story instance
    return render_template("home.html", prompts=prompts)

@app.route('/story')
def show_story():
    """Generate and display the story with the user's answers."""
    # Get the answers from the form submission
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template("story.html", story_text=generated_story)

if __name__ == '__main__':
    app.run(debug=True)

