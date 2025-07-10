from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Chatbot interface
@app.route('/chat')
def chat():
    return render_template('chat.html')

# API endpoint for chatbot (you'll connect this to your existing chatbot)
@app.route('/api/chat', methods=['POST'])
def chat_api():
    user_message = request.json.get('message')
    location = request.json.get('location')
    
    # Here you would connect to your existing chatbot
    # For now, we'll return a mock response
    response = {
        "response": f"Mock response for '{user_message}' regarding {location}",
        "data": {
            "temperature": "22°C",
            "humidity": "65%",
            "soil_moisture": "Optimal"
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)