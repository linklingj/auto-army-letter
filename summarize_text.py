import openai

def summarize_article(article_text):
    openai.api_key = ''
    basic_prompt = '앞으로 쓸 내용은 기사의 일부를 가져온거야. 이 기사를 3문장으로 요약해줘. 공백포함하여 최대 200자여야해. 그리고 어려운 용어는 지양해줘. 기사:'
    messages = []

    message = basic_prompt + article_text
    messages.append({"role": "system", "content": "You are a assistant who summarize articles."},)
    messages.append({"role": "user", "content": message})

    chat = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return f'기사 요약: {reply}'