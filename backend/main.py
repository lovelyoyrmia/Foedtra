import requests
from flask import Flask, request, jsonify
from model import Model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        base_image = 'https://firebasestorage.googleapis.com/v0/b/project-missing-app.appspot.com/o/image%2Fasdasda.JPG?alt=media&token=56ad8367-7ace-4954-8ff9-2c695e3eedfb'
        
        model = Model()
        prediction = model.predict(base_image)
        # convert server response into JSON format.
        return jsonify({'msg': 'success', 'prediction': prediction})
    except Exception as e:
        return jsonify({'msg': 'error', 'error': e})

# @app.route('/image', methods=['POST'])
# def process_image():
#     # base_image = 'https://firebasestorage.googleapis.com/v0/b/project-missing-app.appspot.com/o/image%2Fasdasda.JPG?alt=media&token=56ad8367-7ace-4954-8ff9-2c695e3eedfb'

#     return 

if __name__ == '__main__':
    app.run(debug=True)