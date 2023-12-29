from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

class ChatGPTInterface:
    def __init__(self, api_key):
        self.chat_model = ChatOpenAI(api_key=api_key)

    def generate_response(self, message_list):
        # Use the Langchain client to generate a response
        context = [HumanMessage(content=msg) for msg in message_list]
        context.append(HumanMessage(content='Given the previous context, can you compare all the mortgages'))
        result = self.chat_model.predict_messages(context)
        
        return result
    
