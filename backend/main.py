import tensorflow as tf
from keras.models import load_model
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hello world'

if __name__ == '__main__':
    app.run()