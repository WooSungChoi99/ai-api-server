import with_OpenAI.app_model_prac as app_model_prac

model = app_model_prac.AppModel()

language = input("Pick a language which will be translated into: ")
text = input("Pick a sentence which will be translated: ")

prompt = model.generate_prompt(language, text)
response = model.generate_response(prompt)

print(response.content)