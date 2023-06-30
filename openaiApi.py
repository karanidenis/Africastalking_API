#!/usr/bin/python3
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

def get_chatbot_response(prompt):
    # Generate a chatbot response using OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Chat loop
while True:
    user_input = input("User: ")

    # Prompt the chatbot with user input
    prompt = f"You: {user_input}\nChatBot:"

    curated_prompt = f"""
    you are an ai assistant mental health doctor your task is to talk to mental health patients. you are supposed to be gental and polite. Your main role is to act as a listener and suggest possible ways to help your audience deal with mental health issues. some may feel suicidal and depressed, act as a doctor and provide guidance
    if the prompt provided does not deal with assisting mental health patients, kindly give a response stating that you are only built for mental health purposes only
    make the responses more human-like and avoid long sentences
    the prompts will be in the text delimeted by tripple backticks
    ```{prompt}```

    """

    # Get chatbot response
    chatbot_response = get_chatbot_response(curated_prompt)

    # Print the chatbot response
    print("ChatBot:", chatbot_response)
