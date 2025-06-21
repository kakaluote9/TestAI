import requests
from config import OLLAMA_URL, OLLAMA_MODEL

def call_ollama(question):
    prompt = f"""
你是一个软件测试的大牛，以下是用户的问题，请你只根据软件测试相关知识回答，如果问题与你的专业无关，请礼貌拒绝。
用户提问: {question}
"""
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    try:
        res = requests.post(OLLAMA_URL, json=payload)
        res.raise_for_status()
        return res.json().get("response", "无结果")
    except Exception as e:
        return f"错误：{str(e)}"