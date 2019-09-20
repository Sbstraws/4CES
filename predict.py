# predict.py
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from google.protobuf.json_format import MessageToJson
import json
import sys


def get_prediction(content, project_id, model_id):
	prediction_client = automl_v1beta1.PredictionServiceClient()
	name = f'projects/{project_id}/locations/us-central1/models/{model_id}'
	payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
	params = {}
	request = prediction_client.predict(name, payload, params)
	serialized = json.loads(MessageToJson(request))

	return serialized
