import openai

class ConnectionWithOpenAI:

    def connectwithOpenAI(self):
        api_key = open("Files/API_KEY", "r").read()
        openai.api_key = api_key
        client = openai
        return client
