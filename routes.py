from config import app
from controller import predict_controller


@app.get('/')
def hello_world():
	return 'Healthy'


@app.post('/predict')
def predict():
	return predict_controller()