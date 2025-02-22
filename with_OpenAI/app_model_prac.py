from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

class AppModel:
    def __init__(self):
        #환경변수 생성
        load_dotenv()
        #모델 초기화
        self.model = init_chat_model("gpt-4o-mini", model_provider="openai")
        system_template = "Translate the following from English into {language}"
        self.prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
        )

    def generate_response(self, message):
        response = self.model.invoke(message)
        return response

    def generate_prompt(self, language, text):
        prompt = self.prompt_template.invoke({'language': language, 'text': text})
        prompt.to_messages()
        return prompt