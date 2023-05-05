import openai

def summarize_article(article_text):
    openai.api_key = ''
    basic_prompt = '������ �� ������ ����� �Ϻθ� �����°ž�. �� ��縦 3�������� �������. ���������Ͽ� �ִ� 200�ڿ�����. �׸��� ����� ���� ��������. ���:'
    messages = []

    message = basic_prompt + article_text
    messages.append({"role": "system", "content": "You are a assistant who summarize articles."},)
    messages.append({"role": "user", "content": message})

    chat = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    return f'��� ���: {reply}'