from flask import Flask
from predict import get_prediction


app = Flask(__name__)


@app.route('/')
def hello_world():
	project_id = 'ml-emotional-model'
	model_id = 'TCN3814280993916302163'
	content = 'Hello World!'
	data = get_prediction(content, project_id, model_id)
	return data


if __name__ == '__main__':
	app.run()
