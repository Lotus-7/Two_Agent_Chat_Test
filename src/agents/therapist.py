from .base_agent import BaseAgent

class TherapistAgent(BaseAgent):
    def __init__(self):
        super().__init__("prompts/therapist_prompt.yaml")

    def respond(self, dialogue_history):
        messages = [
            {"role": "system", "content": self.config["system_prompt"]}
        ]

        # 添加对话历史
        for entry in dialogue_history:
            if entry["speaker"] == "patient":
                messages.append({
                    "role": "user",  # 患者的话作为 user 输入
                    "content": entry["content"]
                })
            else:
                messages.append({
                    "role": "assistant",  # 医生自己的话作为 assistant
                    "content": entry["content"]
                })
        return self.generate_response(messages)