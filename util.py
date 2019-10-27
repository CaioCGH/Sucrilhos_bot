import requests

def get_arg(text):
    for i in range(len(text)):
        if text[i] == ' ':
            return text[i+1:]
    return ""

def get(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content