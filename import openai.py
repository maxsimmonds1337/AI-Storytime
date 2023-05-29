import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define your prompt
prompt = "Tell me a joke."

# Generate completion
response = openai.Completion.create(
    engine='text-davinci-003',  # Choose the engine that suits your needs
    prompt=prompt,
    max_tokens=50  # Adjust the desired length of the completion
)

# Get the generated text from the response
completion_text = response.choices[0].text.strip()

# Print the generated completion
print(completion_text)
