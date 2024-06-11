from flask import Flask, request, jsonify, render_template
from blenderbot import BlenderBot

app = Flask(__name__)

model_name = 'facebook/blenderbot-400M-distill'
model_path = 'model/blenderBot'
print("model is loading...")
bot = BlenderBot(model_name, model_path)
print("model is loaded")


@app.route('/')
def home():
    return render_template('index.html')

# def get_chatbot_response(user_input, bot):
#     respone =bot(user_input)
#     return respone

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    if user_input:
        response = bot(user_input)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)