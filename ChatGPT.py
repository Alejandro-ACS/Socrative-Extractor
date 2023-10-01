import openai


def get_response(api_key, question):
    openai.api_key = api_key
    openai.Model.list()
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Por favor responde de forma concisa: " + question}
        ]
    )
    return completion.choices[0].message["content"]
