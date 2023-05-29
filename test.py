import vertexai
from vertexai.preview.language_models import TextGenerationModel
from enum import Enum

class StoryLength(Enum):
    SHORT = 5
    MEDIUM = 7
    LONG = 10


def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: dict,
    location: str = "us-central1",
    tuned_model_name: str = ""
):
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
        model = model.get_tuned_model(tuned_model_name)

    # Construct the full prompt with injected user information
    user_input = input("What should the story be about? ")
    full_prompt = f"The children's story is about a {content['age']}-year-old {content['gender']} with {content['hair_color']} hair. The child's name is {content['name']} and the story should be {content['length']} paragraphs long. " + user_input

    response = model.predict(
        full_prompt,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,
    )
    return response.text

def main():
    project_id = "ai-storytime-387614"
    model_name = "text-bison@001"
    temperature = 0.2
    max_decode_steps = 256
    top_p = 0.8
    top_k = 40
    location = "us-central1"

    # Get user input for the story details
    age = input("Enter the child's age: ")
    name = input("What's the child's name? ")
    gender = input("Enter the child's gender: ")
    hair_color = input("Enter the child's hair color: ")
    length = input("Enter number of pages: ")

    # Store the user-provided information in a dictionary
    content = {
        'age': age,
        'name': name,
        'gender': gender,
        'hair_color': hair_color,
        'length': length,
    }

    generated_story = predict_large_language_model_sample(
        project_id,
        model_name,
        temperature,
        max_decode_steps,
        top_p,
        top_k,
        content,
        location,
    )

    print("Generated Story:")
    print(generated_story)

if __name__ == "__main__":
    main()
