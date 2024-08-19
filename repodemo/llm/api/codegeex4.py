import json
from openai import OpenAI
import requests
import os

def codegeex4(messages_list, temperature=0.2, top_p=0.95):
    openai_api_key = os.getenv('openai_api_key')
    openai_api_base = os.getenv('openai_api_base')
    model_name = os.getenv('model_name')

    if not openai_api_key:
        raise EnvironmentError('Missing environment variable: openai_api_key')
    if not openai_api_base:
        raise EnvironmentError('Missing environment variable: openai_api_base')
    if not model_name:
        raise EnvironmentError('Missing environment variable: model_name')

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    chat_response = client.chat.completions.create(
        model=model_name,
        messages=messages_list,
        temperature=temperature,
        top_p=top_p
    )
    return chat_response.choices[0].message.content

