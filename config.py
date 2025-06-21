import os
import importlib

UPLOAD_FOLDER = 'uploads'
JSON_FILE = 'questions.json'
HISTORY_FILE = 'history.csv'
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5"

# 检查Excel依赖状态
def check_excel_deps():
    try:
        importlib.import_module('openpyxl')
        return True
    except ImportError:
        return False

EXCEL_DEPENDENCY_FIXED = check_excel_deps()

os.makedirs(UPLOAD_FOLDER, exist_ok=True)