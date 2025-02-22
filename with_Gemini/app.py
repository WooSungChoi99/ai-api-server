# from dotenv import load_dotenv
# import os

# # 환경변수 로드 (.env 파일)
# load_dotenv()

# # GEMINI_API_KEY를 환경변수에서 불러옵니다.
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if gemini_api_key is None:
#     raise ValueError("GEMINI_API_KEY가 .env 파일에 설정되어 있지 않습니다.")

# # Gemini 모델 초기화 (model_provider는 'google'로 지정)
# from langchain.chat_models import init_chat_model
# model = init_chat_model("gemini-model", model_provider="google_genai", api_key=gemini_api_key)

# # 예시: 메시지 리스트 생성 및 모델 호출
# from langchain_core.messages import HumanMessage, SystemMessage
# messages = [
#     SystemMessage("Translate the following from English into Italian"),
#     HumanMessage("Hi"),
# ]

# response = model.invoke(messages)
# print(response.content)

# # 예시: 프롬프트 템플릿 활용
# from langchain_core.prompts import ChatPromptTemplate

# system_template = "Translate the following from English into {language}"
# prompt_template = ChatPromptTemplate.from_messages(
#     [('system', system_template), ('user', '{text}')]
# )

# # 'Spanish'로 번역하는 예시
# prompt = prompt_template.invoke({'language': 'Spanish', 'text': 'Hi'})
# # prompt.to_messages()를 호출하여 메시지 리스트로 변환한 후 모델에 전달
# response = model.invoke(prompt.to_messages())
# print(response.content)

# Ensure your VertexAI credentials are configured

# from dotenv import load_dotenv
# load_dotenv()

# from langchain.chat_models import init_chat_model
# model = init_chat_model("gemini-1.5-flash", model_provider="google_genai")

# from langchain_core.messages import HumanMessage, SystemMessage

# messages = [
#     SystemMessage("Translate the following from English into Italian"),
#     HumanMessage("hi!"),
# ]

# model.invoke(messages)

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

#GOOGLE_API_KEY를 환경변수에서 가져옵니다.
google_api_key = os.getenv("GOOGLE_API_KEY")

# ChatGoogleGenerativeAI를 사용하여 모델을 초기화합니다.
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

response = model.invoke(messages)
print(response.content)