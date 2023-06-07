import vertexai
from vertexai.preview.language_models import TextGenerationModel
import os
from flask_cors import CORS

from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app) #, origins='https://storage.googleapis.com/frontend-387614/index.html')

@app.route('/', methods=['GET', 'POST'])
def hello():
    return("Hello world!")

@app.route('/generate-story', methods=['POST'])
def generate_story():
    project_id = "ai-storytime-387614"
    model_name = "text-bison@001"
    temperature = 0.2
    max_decode_steps = 256
    top_p = 0.8
    top_k = 40
    location = "us-central1"

    # Get the request payload
    request_json = request.get_json()
    if request_json and 'prompt' in request_json:
        prompt = request_json['prompt']
        prompt = "Act like a story writer for childrens books. Write me a childrens story, that's very imaginative, that I will be able to take text from and convert to images, about " + prompt
    else:
        return 'Error: Invalid request payload.', 400

    # Initialize the Vertex AI SDK
    vertexai.init(project=project_id, location=location)

    # Create the Text Generation model
    model = TextGenerationModel.from_pretrained(model_name)

    # Generate the story using the provided prompt
    response = model.predict(
        prompt,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,
    )

    generated_story = response.text

    # Set CORS headers
    response = jsonify({'generated_story': generated_story})

    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
