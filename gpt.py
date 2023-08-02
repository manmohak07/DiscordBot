import openai
api_key = ""#"" the key has not been pasted due to security purposes.
openai.api_key = api_key

def chatGPTResponse(conversation):
    try:
        response = openai.ChatCompletion.create(
            model= 'gpt-3.5-turbo',
            messages = conversation
        )
    except openai.error.APIConnectionError:
        return None    
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = chatGPTResponse(conversation)


 #response   
def getResponse(prompt):
    global conversation
    conversation = chatGPTResponse(conversation)

    return conversation[-1]['content'].strip()
