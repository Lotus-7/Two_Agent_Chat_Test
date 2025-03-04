import yaml
from openai import OpenAI

class BaseAgent:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self.client = OpenAI(
            api_key="YOUR_API_KEY", # 请填写你的 API Key
            base_url="https://api.deepseek.com"
        )

    def _load_config(self, config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def generate_response(self, messages):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        return response.choices[0].message.content