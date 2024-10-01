# Import Flask module
from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Define the default route that returns "Hello Foodics!"
@app.route('/')
def home():
    return "Hello Foodics!"

# Run the application on host 0.0.0.0 and port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)