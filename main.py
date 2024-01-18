import openai
from baseclass import Methods
from Connections.connectionwithOpenAI import  ConnectionWithOpenAI

class MainClass:
    chatGpt = ConnectionWithOpenAI()
    client = chatGpt.connectwithOpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hey"}
        ]
    )

    print(response)
