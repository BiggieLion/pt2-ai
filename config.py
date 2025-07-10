import joblib
import pandas as pd
from flask import Flask
from flask_cors import CORS

model = joblib.load('model.pkl')
app = Flask(__name__)
CORS(app, origins='*', methods=['GET', 'POST'])