import g4f
from g4f import ChatCompletion


def ask_gpt(prompt: str)->str:
    response = ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{'role':'user', 'content': prompt}],
    )
    return response

print(ask_gpt('Напиши hello world на c++'))