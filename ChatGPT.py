import openai
import os
from dotenv import load_dotenv

class ChatGPT:

    def __init__(self):

        load_dotenv()

        openai.organization = "org-yGLg9GxNiGIO98pH81JJaGEn"
        openai.api_key = os.getenv("GPT_KEY")

        self.model = "text-davinci-002"

        # prompt = "Write a paragraph about dogs."

    def askChat(self, msg):
        
        response = openai.Completion.create(
            engine=self.model,
            prompt=msg,
            max_tokens=2048 # If the responses are too slow, you can lower this number
        )

        # completion_response = OpenAICompletionResponse(response)
        return response.choices[0].text
        # print(completion_response.choices[0].text)


