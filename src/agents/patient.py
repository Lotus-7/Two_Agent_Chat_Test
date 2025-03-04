from .base_agent import BaseAgent

class PatientAgent(BaseAgent):
    def __init__(self):
        super().__init__("prompts/patient_prompt.yaml")

    def start_conversation(self):
        # 第一轮对话
        messages = [
            {"role": "system", "content": self.config["system_prompt"]},
            {"role": "user", "content": self.config["user_prompt"]}
        ]
        return self.generate_response(messages)

    def respond(self, dialogue_history):
        messages = [
            {"role": "system", "content": self.config["system_prompt"]}
        ]

        # 添加对话历史
        for entry in dialogue_history:
            if entry["speaker"] == "therapist":
                messages.append({
                    "role": "assistant",  # 医生的回复作为 assistant
                    "content": entry["content"]
                })
            else:
                messages.append({
                    "role": "user",  # 患者自己的话作为 user
                    "content": entry["content"]
                })
        return self.generate_response(messages)