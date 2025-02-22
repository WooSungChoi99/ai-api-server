from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

from langchain_core.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("Hi"),
]

response = model.invoke(messages)

print(response.content)

# print(model.invoke("Hi").content)
# print(model.invoke([{'role': 'user', 'content': 'Hi'}]).content)
# print(model.invoke([HumanMessage("Hi")]).content)

from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [('system', system_template), ('user', '{text}')]
)

prompt = prompt_template.invoke({'language': 'Spanish', 'text': 'hi'})
prompt.to_messages()
response = model.invoke(prompt)
print(response.content)