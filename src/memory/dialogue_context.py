class DialogueContext:
    def __init__(self):
        self.therapist_history = []  # 存储心理医生的说话内容
        self.patient_history = []    # 存储患者的说话内容
        self.full_dialogue = []      # 存储完整对话记录

    # 添加心理医生的说话内容
    def add_therapist_response(self, response):
        entry = {"speaker": "therapist", "content": response}
        self.therapist_history.append(entry)
        self.full_dialogue.append(entry)

    # 添加患者的说话内容
    def add_patient_response(self, response):
        entry = {"speaker": "patient", "content": response}
        self.patient_history.append(entry)
        self.full_dialogue.append(entry)

    # 获取患者的说话内容
    def get_patient_context(self):
        return self.patient_history

    # 获取心理医生的说话内容
    def get_therapist_context(self):
        return self.therapist_history

    # 获取完整对话记录
    def get_full_dialogue(self):
        return self.full_dialogue